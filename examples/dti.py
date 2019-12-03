# -*- coding: utf-8 -*-

import os
import numpy as np
from sklearn.pipeline import Pipeline
from libkge.embedding import TransE, DistMult, ComplEx, TriModel, DistMult_MCL, ComplEx_MCL, TriModel_MCL
from libkge import KgDataset


def main():
    seed = 1234
    data_name = "dti"
    kg_dp_path = "../data/dti"

    drugbank_kg_fd = open(os.path.join(kg_dp_path, "drugbank_facts.txt"))
    uniprot_kg_fd = open(os.path.join(kg_dp_path, "uniprot_kg.txt"))

    drugbank_raw = np.array([l.strip().split() for l in drugbank_kg_fd.readlines()])
    uniprot_raw = np.array([l.strip().split() for l in uniprot_kg_fd.readlines()])

    dataset = KgDataset(name=data_name)
    dataset.load_triples(drugbank_raw, tag="drugbank")
    dataset.load_triples(uniprot_raw, tag="uniprot")

    nb_entities = dataset.get_ents_count()
    nb_relations = dataset.get_rels_count()

    # grouping side effect information by the side effect type
    drugbank_data = dataset.data["drugbank"]
    uniprot_data = dataset.data["uniprot"]

    all_data = np.concatenate([drugbank_data, uniprot_data])

    print("Initializing the knowledge graph embedding model... ")
    # model pipeline definition
    model = TransE(seed=seed, verbose=2)
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
    pipe_model.fit(X=all_data, y=None)

    # you can then use the model to predict whatever fact you want using the predict interface as follows:

    example_facts = np.array([
        ["P61026", "INTERACT_WITH", "Q9H0K6"],
        ["DB00008", "DRUG_TARGET", "Q9H0K6"]
    ])

    scores = pipe_model.predict(example_facts)


if __name__ == '__main__':
    main()

