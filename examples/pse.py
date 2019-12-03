# -*- coding: utf-8 -*-

import os
import itertools
import gzip
import numpy as np
from sklearn.pipeline import Pipeline
from tqdm import tqdm
from libkge.embedding import TransE, DistMult, ComplEx, TriModel, DistMult_MCL, ComplEx_MCL, TriModel_MCL
from libkge import KgDataset
from libkge.metrics.classification import auc_roc, auc_pr
from libkge.metrics.ranking import precision_at_k, average_precision
from libkge.metrics.classification import auc_pr, auc_roc


def main():
    seed = 1234
    nb_epochs_then_check = None
    data_name = "pse"
    kg_dp_path = "../data/pse"

    se_map_raw = [l.strip().split("\t") for l in open(os.path.join(kg_dp_path, "se_maps.txt")).readlines()]
    se_mapping = {k: v for k, v in se_map_raw}

    print("Importing dataset files ... ")
    benchmark_train_fd = gzip.open(os.path.join(kg_dp_path, "ploypharmacy_facts_train.txt.gz"), "rt")
    benchmark_valid_fd = gzip.open(os.path.join(kg_dp_path, "ploypharmacy_facts_valid.txt.gz"), "rt")
    benchmark_test_fd = gzip.open(os.path.join(kg_dp_path, "ploypharmacy_facts_test.txt.gz"), "rt")

    benchmark_train = np.array([l.strip().split() for l in benchmark_train_fd.readlines()])
    benchmark_valid = np.array([l.strip().split() for l in benchmark_valid_fd.readlines()])
    benchmark_test = np.array([l.strip().split() for l in benchmark_test_fd.readlines()])

    benchmark_triples = np.array([[d1, se, d2] for d1, se, d2 in
                                  np.concatenate([benchmark_train, benchmark_valid, benchmark_test])])

    pse_drugs = list(set(list(np.concatenate([benchmark_triples[:, 0], benchmark_triples[:, 2]]))))
    pse_list = set(list(benchmark_triples[:, 1]))

    rel_dict = dict()
    for s, p, o in benchmark_triples:
        if p not in rel_dict:
            rel_dict[p] = 1
        else:
            rel_dict[p] += 1

    pair_dict = dict()
    for s, p, o in benchmark_triples:
        if s > o:
            pair = (s, o)
        else:
            pair = (o, s)
        if pair not in rel_dict:
            pair_dict[pair] = 1
        else:
            pair_dict[pair] += 1

    drug_combinations = np.array([[d1, d2] for d1, d2 in list(itertools.product(pse_drugs, pse_drugs)) if d1 != d2])

    print("Processing dataset files to generate a knowledge graph ... ")
    # delete raw polypharmacy data
    del benchmark_triples
    dataset = KgDataset(name=data_name)
    dataset.load_triples(benchmark_train, tag="bench_train")
    dataset.load_triples(benchmark_valid, tag="bench_valid")
    dataset.load_triples(benchmark_test, tag="bench_test")

    del benchmark_train
    del benchmark_valid
    del benchmark_test

    nb_entities = dataset.get_ents_count()
    nb_relations = dataset.get_rels_count()
    pse_indices = dataset.get_rel_indices(list(pse_list))

    d1 = np.array(dataset.get_ent_indices(list(drug_combinations[:, 0]))).reshape([-1, 1])
    d2 = np.array(dataset.get_ent_indices(list(drug_combinations[:, 1]))).reshape([-1, 1])
    drug_combinations = np.concatenate([d1, d2], axis=1)
    del d1
    del d2

    # grouping side effect information by the side effect type
    train_data = dataset.data["bench_train"]
    valid_data = dataset.data["bench_valid"]
    test_data = dataset.data["bench_test"]

    bench_idx_data = np.concatenate([train_data, valid_data, test_data])
    se_facts_full_dict = {se: set() for se in pse_indices}

    for s, p, o in bench_idx_data:
        se_facts_full_dict[p].add((s, p, o))

    print("Initializing the knowledge graph embedding model... ")
    # model pipeline definition
    model = TriModel(seed=seed, verbose=2)
    pipe_model = Pipeline([('kge_model', model)])

    # set model parameters
    model_params = {
        'kge_model__em_size': 100,
        'kge_model__lr': 0.01,
        'kge_model__optimiser': "AMSgrad",
        'kge_model__log_interval': 10,
        'kge_model__nb_epochs': 100,
        'kge_model__nb_negs': 6,
        'kge_model__batch_size': 5000,
        'kge_model__initialiser': 'xavier_uniform',
        'kge_model__nb_ents': nb_entities,
        'kge_model__nb_rels': nb_relations
    }

    # add parameters to the model then call fit method
    pipe_model.set_params(**model_params)

    print("Training ... ")
    pipe_model.fit(X=train_data, y=None)

    metrics_per_se = {se_idx: {"ap": .0, "auc-roc": .0, "auc-pr": .0, "p@50": .0} for se_idx in pse_indices}

    se_ap_list = []
    se_auc_roc_list = []
    se_auc_pr_list = []
    se_p50_list = []

    print("================================================================================")
    for se in tqdm(pse_indices, desc="Evaluating test data for each side-effect"):
        se_name = dataset.get_rel_labels([se])[0]
        se_all_facts_set = se_facts_full_dict[se]
        se_test_facts_pos = np.array([[s, p, o] for s, p, o in test_data if p == se])
        se_test_facts_pos_size = len(se_test_facts_pos)

        se_test_facts_neg = np.array([[d1, se, d2] for d1, d2 in drug_combinations
                                      if (d1, se, d2) not in se_all_facts_set
                                      and (d2, se, d1) not in se_all_facts_set])

        # shuffle and keep negatives with size equal to positive instances so positive to negative ratio is 1:1
        np.random.shuffle(se_test_facts_neg)
        se_test_facts_neg = se_test_facts_neg[:se_test_facts_pos_size, :]

        set_test_facts_all = np.concatenate([se_test_facts_pos, se_test_facts_neg])
        se_test_facts_labels = np.concatenate([np.ones([len(se_test_facts_pos)]), np.zeros([len(se_test_facts_neg)])])
        se_test_facts_scores = model.predict(set_test_facts_all)

        se_ap = average_precision(se_test_facts_labels, se_test_facts_scores)
        se_p50 = precision_at_k(se_test_facts_labels, se_test_facts_scores, k=50)
        se_auc_pr = auc_pr(se_test_facts_labels, se_test_facts_scores)
        se_auc_roc = auc_roc(se_test_facts_labels, se_test_facts_scores)

        se_ap_list.append(se_ap)
        se_auc_roc_list.append(se_auc_roc)
        se_auc_pr_list.append(se_auc_pr)
        se_p50_list.append(se_p50)

        se_code = se_name.replace("SE:", "")
        metrics_per_se[se] = {"ap": se_ap, "auc-roc": se_auc_roc, "auc-pr": se_auc_pr, "p@50": se_p50}
        print("AP: %1.4f - AUC-ROC: %1.4f - AUC-PR: %1.4f - P@50: %1.4f > %s: %s" %
              (se_ap, se_auc_roc, se_auc_pr, se_p50, se_code, se_mapping[se_code]), flush=True)

    se_ap_list_avg = np.average(se_ap_list)
    se_auc_roc_list_avg = np.average(se_auc_roc_list)
    se_auc_pr_list_avg = np.average(se_auc_pr_list)
    se_p50_list_avg = np.average(se_p50_list)

    print("================================================================================")
    print("[AVERAGE] AP: %1.4f - AUC-ROC: %1.4f - AUC-PR: %1.4f - P@50: %1.4f" %
          (se_ap_list_avg, se_auc_roc_list_avg, se_auc_pr_list_avg, se_p50_list_avg), flush=True)
    print("================================================================================")


if __name__ == '__main__':
    main()

