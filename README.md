# Biological Applications of KGE Models

Example biological applications of knowledge graph embedding models




### Installation
First, you need to install the LibKGE library in it as follow:

```bash
git clone https://github.com/samehkamaleldin/libkge.git
cd libkge
pip install -r requirements.txt
# change tensorflow version it to the gup version if you want to use GPUs for accelerated computation
pip install tensorflow==1.14 
python setup.py install
```

You are then ready to use the example script in this repository. For example, you can run the polypharmacy side-effects model training using its script as follows:
``` bash
cd examples
python pse.py
``` 

This will initialise the training and evaluation process and will report it as follows:
```
Importing dataset files ... 
Processing dataset files to generate a knowledge graph ... 
Initializing the knowledge graph embedding model... 
Training ... 
2019-12-03 13:20:39,553 - ComplEx - DEBUG - Logging model parameters ...
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] _predict_pipeline_on: False
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] batch_size          : 5000
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] em_size             : 100
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] initialiser         : xavier_uniform
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] log_interval        : 10
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] loss                : default
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] lr                  : 0.01
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] nb_ents             : 645
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] nb_epochs           : 100
2019-12-03 13:20:39,553 - ComplEx - DEBUG - [Parameter] nb_negs             : 6
2019-12-03 13:20:39,554 - ComplEx - DEBUG - [Parameter] nb_rels             : 963
2019-12-03 13:20:39,554 - ComplEx - DEBUG - [Parameter] optimiser           : AMSgrad
2019-12-03 13:20:39,554 - ComplEx - DEBUG - [Parameter] predict_batch_size  : 40000
2019-12-03 13:20:39,554 - ComplEx - DEBUG - [Parameter] reg_wt              : 0.01
2019-12-03 13:20:39,554 - ComplEx - DEBUG - [Parameter] seed                : 1234
2019-12-03 13:20:39,554 - ComplEx - DEBUG - [Parameter] verbose             : 2
2019-12-03 13:20:39,554 - ComplEx - DEBUG - Model training started ...
2019-12-03 13:20:39,554 - ComplEx - DEBUG - Training model [ 3661895 #Instances - 645 #Entities - 963 #Relations ]
2019-12-03 13:20:40,020 - ComplEx - DEBUG - Initialising tensorflow session
2019-12-03 13:20:40,307 - ComplEx - DEBUG - Executing tensorflow global variable initialiser
2019-12-03 13:20:51,793 - ComplEx - DEBUG - [Training] Epoch # 1    - Speed: 319.520 (k. record/sec) - Loss: 0.5351 - Avg(Loss): 0.5351 - Std(Loss): 0.0536
2019-12-03 13:22:33,490 - ComplEx - DEBUG - [Training] Epoch # 10   - Speed: 323.647 (k. record/sec) - Loss: 0.4598 - Avg(Loss): 0.4739 - Std(Loss): 0.0277
2019-12-03 13:24:26,673 - ComplEx - DEBUG - [Training] Epoch # 20   - Speed: 322.797 (k. record/sec) - Loss: 0.4553 - Avg(Loss): 0.4654 - Std(Loss): 0.0215
2019-12-03 13:26:19,876 - ComplEx - DEBUG - [Training] Epoch # 30   - Speed: 324.329 (k. record/sec) - Loss: 0.4536 - Avg(Loss): 0.4617 - Std(Loss): 0.0184
2019-12-03 13:28:13,069 - ComplEx - DEBUG - [Training] Epoch # 40   - Speed: 322.653 (k. record/sec) - Loss: 0.4524 - Avg(Loss): 0.4595 - Std(Loss): 0.0165
2019-12-03 13:30:06,160 - ComplEx - DEBUG - [Training] Epoch # 50   - Speed: 323.212 (k. record/sec) - Loss: 0.4516 - Avg(Loss): 0.4580 - Std(Loss): 0.0152
2019-12-03 13:31:59,192 - ComplEx - DEBUG - [Training] Epoch # 60   - Speed: 322.866 (k. record/sec) - Loss: 0.4510 - Avg(Loss): 0.4569 - Std(Loss): 0.0142
2019-12-03 13:33:52,227 - ComplEx - DEBUG - [Training] Epoch # 70   - Speed: 323.465 (k. record/sec) - Loss: 0.4506 - Avg(Loss): 0.4560 - Std(Loss): 0.0134
2019-12-03 13:35:45,443 - ComplEx - DEBUG - [Training] Epoch # 80   - Speed: 323.294 (k. record/sec) - Loss: 0.4502 - Avg(Loss): 0.4553 - Std(Loss): 0.0127
2019-12-03 13:37:38,707 - ComplEx - DEBUG - [Training] Epoch # 90   - Speed: 323.935 (k. record/sec) - Loss: 0.4498 - Avg(Loss): 0.4547 - Std(Loss): 0.0121
2019-12-03 13:39:31,779 - ComplEx - DEBUG - [Training] Epoch # 100  - Speed: 324.690 (k. record/sec) - Loss: 0.4498 - Avg(Loss): 0.4542 - Std(Loss): 0.0117
2019-12-03 13:39:31,787 - ComplEx - DEBUG - [Reporting] Finished (100 Epochs) - Avg(Speed): 323.668 (k. record/sec) - Avg(Loss): 0.4542 - Std(Loss): 0.0117
================================================================================
AP: 0.9402 - AUC-ROC: 0.9402 - AUC-PR: 0.9651 - P@50: 0.9400 > C0221264: cheilosis
AP: 0.9417 - AUC-ROC: 0.9417 - AUC-PR: 0.9583 - P@50: 0.9600 > C0018824: cardiac valvulopathy
AP: 0.8296 - AUC-ROC: 0.8296 - AUC-PR: 0.8947 - P@50: 0.8000 > C0002792: anaphylactic reaction
AP: 0.9533 - AUC-ROC: 0.9533 - AUC-PR: 0.9738 - P@50: 0.9800 > C0005818: platelet disorder
AP: 0.9036 - AUC-ROC: 0.9036 - AUC-PR: 0.9278 - P@50: 0.9600 > C0023895: disease of liver
AP: 0.9455 - AUC-ROC: 0.9455 - AUC-PR: 0.9555 - P@50: 0.9600 > C0034359: pyuria
AP: 0.9156 - AUC-ROC: 0.9156 - AUC-PR: 0.9626 - P@50: 0.9400 > C0020514: Hyperprolactinaemia
AP: 0.9343 - AUC-ROC: 0.9343 - AUC-PR: 0.9818 - P@50: 0.9800 > C0032633: dyshidrosis
AP: 0.8970 - AUC-ROC: 0.8970 - AUC-PR: 0.9345 - P@50: 0.8600 > C0030193: Pain
AP: 0.9708 - AUC-ROC: 0.9708 - AUC-PR: 0.9772 - P@50: 0.9800 > C0040485: retrocollis
AP: 0.9030 - AUC-ROC: 0.9030 - AUC-PR: 0.9373 - P@50: 0.9400 > C0242184: hypoxia
AP: 0.9419 - AUC-ROC: 0.9419 - AUC-PR: 0.9550 - P@50: 0.9800 > C0039503: Tendinitis
AP: 0.8944 - AUC-ROC: 0.8944 - AUC-PR: 0.9322 - P@50: 0.9000 > C0021141: ADH inappropriate
AP: 0.8808 - AUC-ROC: 0.8808 - AUC-PR: 0.9248 - P@50: 0.8800 > C0836924: increased platelet count
AP: 0.9167 - AUC-ROC: 0.9167 - AUC-PR: 0.9398 - P@50: 0.9800 > C1527344: dysphonia
AP: 0.9378 - AUC-ROC: 0.9378 - AUC-PR: 0.9511 - P@50: 0.9200 > C0006271: bronchiolitis
AP: 0.9356 - AUC-ROC: 0.9356 - AUC-PR: 0.9528 - P@50: 0.9200 > C0553723: squamous cell carcinoma of skin
AP: 0.9881 - AUC-ROC: 0.9881 - AUC-PR: 0.9885 - P@50: 0.9400 > C0025637: methaemoglobinaemia
AP: 0.9701 - AUC-ROC: 0.9701 - AUC-PR: 0.9767 - P@50: 0.9800 > C1136085: monoclonal gammopathy
AP: 0.9453 - AUC-ROC: 0.9453 - AUC-PR: 0.9635 - P@50: 0.9600 > C0037195: Sinus headache
AP: 0.8607 - AUC-ROC: 0.8607 - AUC-PR: 0.9112 - P@50: 0.9200 > C0039231: heart rate increased
AP: 0.9604 - AUC-ROC: 0.9604 - AUC-PR: 0.9678 - P@50: 0.9400 > C0037578: soft tissue injuries
AP: 0.8856 - AUC-ROC: 0.8856 - AUC-PR: 0.9382 - P@50: 0.8800 > C0027059: myocarditis
AP: 0.9310 - AUC-ROC: 0.9310 - AUC-PR: 0.9541 - P@50: 0.9400 > C0040425: tonsillitis
AP: 0.9215 - AUC-ROC: 0.9215 - AUC-PR: 0.9548 - P@50: 0.9400 > C0036689: Pharyngitis Streptococcal
AP: 0.9148 - AUC-ROC: 0.9148 - AUC-PR: 0.9428 - P@50: 0.9000 > C0042769: Infection Viral
AP: 0.9225 - AUC-ROC: 0.9225 - AUC-PR: 0.9527 - P@50: 0.9200 > C0162429: malnourished
AP: 0.9565 - AUC-ROC: 0.9565 - AUC-PR: 0.9660 - P@50: 0.9800 > C0024523: malabsorption
AP: 0.9735 - AUC-ROC: 0.9735 - AUC-PR: 0.9754 - P@50: 1.0000 > C0259817: xerosis
AP: 0.8961 - AUC-ROC: 0.8961 - AUC-PR: 0.9372 - P@50: 0.9000 > C0080274: bladder retention
AP: 0.9594 - AUC-ROC: 0.9594 - AUC-PR: 0.9734 - P@50: 0.9600 > C0085694: cholecystitis chronic
AP: 0.8860 - AUC-ROC: 0.8860 - AUC-PR: 0.9268 - P@50: 0.9000 > C0243026: sepsis
AP: 0.8935 - AUC-ROC: 0.8935 - AUC-PR: 0.9283 - P@50: 0.9800 > C0035078: kidney failure
AP: 0.9606 - AUC-ROC: 0.9606 - AUC-PR: 0.9735 - P@50: 0.9800 > C0016167: anal fissure
AP: 0.9156 - AUC-ROC: 0.9156 - AUC-PR: 0.9542 - P@50: 0.9200 > C0043246: laceration
AP: 0.9649 - AUC-ROC: 0.9649 - AUC-PR: 0.9664 - P@50: 1.0000 > C0014356: enterocolitis
AP: 0.9850 - AUC-ROC: 0.9850 - AUC-PR: 0.9849 - P@50: 0.9800 > C0740858: substance abuse
AP: 0.9739 - AUC-ROC: 0.9739 - AUC-PR: 0.9765 - P@50: 0.9800 > C0036830: serum sickness
AP: 0.9070 - AUC-ROC: 0.9070 - AUC-PR: 0.9434 - P@50: 0.9400 > C0043117: idiopathic thrombocytopenic purpura
AP: 0.9732 - AUC-ROC: 0.9732 - AUC-PR: 0.9810 - P@50: 0.9800 > C0014488: epicondylitis
AP: 0.9657 - AUC-ROC: 0.9657 - AUC-PR: 0.9754 - P@50: 0.9600 > C0018916: haemangioma
AP: 0.9277 - AUC-ROC: 0.9277 - AUC-PR: 0.9445 - P@50: 0.9600 > C0034155: thrombotic microangiopathy
AP: 0.8858 - AUC-ROC: 0.8858 - AUC-PR: 0.9284 - P@50: 0.9200 > C0022660: acute kidney failure
AP: 0.8662 - AUC-ROC: 0.8662 - AUC-PR: 0.9205 - P@50: 0.8600 > C0007787: transient ischaemic attack
AP: 0.9068 - AUC-ROC: 0.9068 - AUC-PR: 0.9391 - P@50: 0.9200 > C0242379: lung neoplasm malignant
AP: 0.9145 - AUC-ROC: 0.9145 - AUC-PR: 0.9495 - P@50: 0.9600 > C0029163: mouth bleeding
AP: 0.9329 - AUC-ROC: 0.9329 - AUC-PR: 0.9595 - P@50: 0.9600 > C0037052: sick sinus syndrome
AP: 0.8946 - AUC-ROC: 0.8946 - AUC-PR: 0.9334 - P@50: 0.9000 > C0035317: retinal bleeding
AP: 0.9263 - AUC-ROC: 0.9263 - AUC-PR: 0.9420 - P@50: 0.9400 > C0016658: bone fracture
AP: 0.9027 - AUC-ROC: 0.9027 - AUC-PR: 0.9303 - P@50: 0.9200 > C0040264: tinnitus
AP: 0.8874 - AUC-ROC: 0.8874 - AUC-PR: 0.9466 - P@50: 0.9000 > C0009946: conversion disorder
AP: 0.8686 - AUC-ROC: 0.8686 - AUC-PR: 0.9157 - P@50: 0.9000 > C0013604: edema
AP: 0.8811 - AUC-ROC: 0.8811 - AUC-PR: 0.9313 - P@50: 0.8200 > C0017152: gastric inflammation
AP: 0.8838 - AUC-ROC: 0.8838 - AUC-PR: 0.9232 - P@50: 0.9400 > C0013144: drowsiness
AP: 0.8860 - AUC-ROC: 0.8860 - AUC-PR: 0.9279 - P@50: 0.9200 > C0235974: pancreatic cancer
AP: 0.9565 - AUC-ROC: 0.9565 - AUC-PR: 0.9691 - P@50: 0.9800 > C0152018: esophageal cancer
AP: 0.9337 - AUC-ROC: 0.9337 - AUC-PR: 0.9522 - P@50: 0.9600 > C0018021: goiter
AP: 0.9432 - AUC-ROC: 0.9432 - AUC-PR: 0.9542 - P@50: 1.0000 > C0040435: tooth disease
AP: 0.8923 - AUC-ROC: 0.8923 - AUC-PR: 0.9357 - P@50: 0.8400 > C0917801: insomnia
AP: 0.9608 - AUC-ROC: 0.9608 - AUC-PR: 0.9675 - P@50: 0.9400 > C0040584: tracheitis
AP: 0.9071 - AUC-ROC: 0.9071 - AUC-PR: 0.9415 - P@50: 0.8800 > C0004604: Back Ache
AP: 0.8793 - AUC-ROC: 0.8793 - AUC-PR: 0.9264 - P@50: 0.8400 > C0003123: Anorexia
AP: 0.9112 - AUC-ROC: 0.9112 - AUC-PR: 0.9464 - P@50: 0.9400 > C0026821: cramp
AP: 0.9876 - AUC-ROC: 0.9876 - AUC-PR: 0.9878 - P@50: 1.0000 > C0155540: ear discharge
AP: 0.9011 - AUC-ROC: 0.9011 - AUC-PR: 0.9421 - P@50: 0.9000 > C0017160: gastroenteritis
AP: 0.9871 - AUC-ROC: 0.9871 - AUC-PR: 0.9884 - P@50: 0.9800 > C0016479: food poisoning
AP: 0.9451 - AUC-ROC: 0.9451 - AUC-PR: 0.9576 - P@50: 0.9600 > C0016436: folliculitis
AP: 0.8810 - AUC-ROC: 0.8810 - AUC-PR: 0.9295 - P@50: 0.8400 > C0021400: flu
AP: 0.8991 - AUC-ROC: 0.8991 - AUC-PR: 0.9404 - P@50: 0.8400 > C0031039: pericardial effusion
AP: 0.9805 - AUC-ROC: 0.9805 - AUC-PR: 0.9825 - P@50: 0.9800 > C0014175: endometriosis
AP: 0.9354 - AUC-ROC: 0.9354 - AUC-PR: 0.9557 - P@50: 0.9600 > C0020550: hyperthyroidism
AP: 0.9124 - AUC-ROC: 0.9124 - AUC-PR: 0.9538 - P@50: 0.8600 > C0028734: nocturia
AP: 0.9057 - AUC-ROC: 0.9057 - AUC-PR: 0.9366 - P@50: 0.9200 > C0035522: rib fracture
AP: 0.9393 - AUC-ROC: 0.9393 - AUC-PR: 0.9704 - P@50: 0.9600 > C0019189: chronic hepatitis
AP: 0.9010 - AUC-ROC: 0.9010 - AUC-PR: 0.9332 - P@50: 0.9400 > C0014742: erythema multiforme
AP: 0.8979 - AUC-ROC: 0.8979 - AUC-PR: 0.9388 - P@50: 0.9200 > C0005826: blood pressure abnormal
AP: 0.9248 - AUC-ROC: 0.9248 - AUC-PR: 0.9491 - P@50: 0.9000 > C0001546: adjustment disorder
AP: 0.9696 - AUC-ROC: 0.9696 - AUC-PR: 0.9732 - P@50: 0.9400 > C0010032: corneal abrasion
AP: 0.9152 - AUC-ROC: 0.9152 - AUC-PR: 0.9439 - P@50: 0.9400 > C0019209: enlarged liver
AP: 0.9817 - AUC-ROC: 0.9817 - AUC-PR: 0.9844 - P@50: 1.0000 > C0001430: adenoma
AP: 0.9584 - AUC-ROC: 0.9584 - AUC-PR: 0.9736 - P@50: 0.9600 > C0086438: hypogammaglobulinaemia
AP: 0.8821 - AUC-ROC: 0.8821 - AUC-PR: 0.9306 - P@50: 0.8400 > C0004238: AFIB
AP: 0.9428 - AUC-ROC: 0.9428 - AUC-PR: 0.9573 - P@50: 0.9800 > C0015469: facial palsy
AP: 0.9385 - AUC-ROC: 0.9385 - AUC-PR: 0.9649 - P@50: 0.9600 > C0012691: dislocation
AP: 0.8992 - AUC-ROC: 0.8992 - AUC-PR: 0.9387 - P@50: 0.8600 > C0013395: dyspepsia
AP: 0.9203 - AUC-ROC: 0.9203 - AUC-PR: 0.9557 - P@50: 0.9200 > C0014130: endocrine disorder
AP: 0.8691 - AUC-ROC: 0.8691 - AUC-PR: 0.9175 - P@50: 0.8600 > C0001122: Acidosis
AP: 0.8845 - AUC-ROC: 0.8845 - AUC-PR: 0.9326 - P@50: 0.8600 > C0023890: cirrhosis
AP: 0.9411 - AUC-ROC: 0.9411 - AUC-PR: 0.9718 - P@50: 0.9600 > C0262397: breast tenderness
AP: 0.9300 - AUC-ROC: 0.9300 - AUC-PR: 0.9611 - P@50: 0.9600 > C0030319: panic disorder
AP: 0.9335 - AUC-ROC: 0.9335 - AUC-PR: 0.9595 - P@50: 0.9400 > C0029927: Ovarian Cyst
AP: 0.9397 - AUC-ROC: 0.9397 - AUC-PR: 0.9569 - P@50: 0.9600 > C0006325: bruxism
AP: 0.9477 - AUC-ROC: 0.9477 - AUC-PR: 0.9712 - P@50: 0.9800 > C0018520: bad breath
AP: 0.8948 - AUC-ROC: 0.8948 - AUC-PR: 0.9365 - P@50: 0.8800 > C0007642: cellulitis
AP: 0.9168 - AUC-ROC: 0.9168 - AUC-PR: 0.9386 - P@50: 0.9600 > C0009319: colitis
AP: 0.9152 - AUC-ROC: 0.9152 - AUC-PR: 0.9382 - P@50: 0.9200 > C0149520: cholecystitis acute
AP: 0.8697 - AUC-ROC: 0.8697 - AUC-PR: 0.9168 - P@50: 0.8800 > C0018524: Hallucination
AP: 0.8924 - AUC-ROC: 0.8924 - AUC-PR: 0.9341 - P@50: 0.9000 > C0020461: Excess potassium
AP: 0.8984 - AUC-ROC: 0.8984 - AUC-PR: 0.9282 - P@50: 1.0000 > C0162297: pulmonary arrest
AP: 0.9514 - AUC-ROC: 0.9514 - AUC-PR: 0.9657 - P@50: 0.9400 > C0025874: Breakthrough bleeding
AP: 0.9690 - AUC-ROC: 0.9690 - AUC-PR: 0.9752 - P@50: 1.0000 > C0003564: Aphonia
AP: 0.9059 - AUC-ROC: 0.9059 - AUC-PR: 0.9557 - P@50: 0.9000 > C0031542: Phlebitis
AP: 0.9320 - AUC-ROC: 0.9320 - AUC-PR: 0.9465 - P@50: 1.0000 > C0017565: Bleeding gums
AP: 0.9921 - AUC-ROC: 0.9921 - AUC-PR: 0.9932 - P@50: 1.0000 > C0025345: Menstrual Disorder
AP: 0.9607 - AUC-ROC: 0.9607 - AUC-PR: 0.9731 - P@50: 0.9400 > C0008049: chicken pox
AP: 0.8932 - AUC-ROC: 0.8932 - AUC-PR: 0.9323 - P@50: 0.8800 > C0034886: proctalgia
AP: 0.9199 - AUC-ROC: 0.9199 - AUC-PR: 0.9539 - P@50: 0.9400 > C0278008: Altered Bowel Function
AP: 0.9371 - AUC-ROC: 0.9371 - AUC-PR: 0.9593 - P@50: 0.9800 > C0017658: glomerulonephritis
AP: 0.9223 - AUC-ROC: 0.9223 - AUC-PR: 0.9486 - P@50: 0.9400 > C0024141: disseminated lupus erythematosus
AP: 0.9454 - AUC-ROC: 0.9454 - AUC-PR: 0.9623 - P@50: 0.9600 > C0042909: Vitreous haemorrhage
AP: 0.8989 - AUC-ROC: 0.8989 - AUC-PR: 0.9411 - P@50: 0.8800 > C0043352: aptyalism
AP: 0.9232 - AUC-ROC: 0.9232 - AUC-PR: 0.9503 - P@50: 0.9600 > C0028259: nodule
AP: 0.9285 - AUC-ROC: 0.9285 - AUC-PR: 0.9578 - P@50: 0.9200 > C0032273: pneumoconiosis
AP: 0.9543 - AUC-ROC: 0.9543 - AUC-PR: 0.9661 - P@50: 0.9800 > C0022104: Colon Spastic
AP: 0.9117 - AUC-ROC: 0.9117 - AUC-PR: 0.9385 - P@50: 0.9400 > C0041296: Mycobacterium tuberculosis infection
AP: 0.9038 - AUC-ROC: 0.9038 - AUC-PR: 0.9364 - P@50: 0.9400 > C0015732: faecal incontinence
AP: 0.9196 - AUC-ROC: 0.9196 - AUC-PR: 0.9459 - P@50: 0.9000 > C0042420: syncope vasovagal
AP: 0.9208 - AUC-ROC: 0.9208 - AUC-PR: 0.9468 - P@50: 0.9600 > C0007117: basal cell carcinoma
AP: 0.9111 - AUC-ROC: 0.9111 - AUC-PR: 0.9398 - P@50: 0.9400 > C0036983: septic shock
AP: 0.9584 - AUC-ROC: 0.9584 - AUC-PR: 0.9617 - P@50: 0.9600 > C0042870: Vitamin D Deficiency
AP: 0.8896 - AUC-ROC: 0.8896 - AUC-PR: 0.9302 - P@50: 0.9000 > C0018926: haematemesis
AP: 0.9816 - AUC-ROC: 0.9816 - AUC-PR: 0.9869 - P@50: 0.9800 > C0262365: abnormal mammogram
AP: 0.8391 - AUC-ROC: 0.8391 - AUC-PR: 0.9000 - P@50: 0.8200 > C0011615: allergic dermatitis
AP: 0.8857 - AUC-ROC: 0.8857 - AUC-PR: 0.9417 - P@50: 0.9000 > C0035854: acne rosacea
AP: 0.8768 - AUC-ROC: 0.8768 - AUC-PR: 0.9202 - P@50: 0.9000 > C0149925: SCLC
AP: 0.9448 - AUC-ROC: 0.9448 - AUC-PR: 0.9539 - P@50: 0.9800 > C0178879: obstructive uropathy
AP: 0.9553 - AUC-ROC: 0.9553 - AUC-PR: 0.9704 - P@50: 0.9600 > C0424230: motor retardation
AP: 0.8892 - AUC-ROC: 0.8892 - AUC-PR: 0.9399 - P@50: 0.8600 > C0151632: elevated erythrocyte sedimentation rate
AP: 0.9467 - AUC-ROC: 0.9467 - AUC-PR: 0.9613 - P@50: 0.9600 > C0007280: carotid bruit
AP: 0.9521 - AUC-ROC: 0.9521 - AUC-PR: 0.9670 - P@50: 0.9400 > C0037998: Splenic infarction
AP: 0.9197 - AUC-ROC: 0.9197 - AUC-PR: 0.9498 - P@50: 0.9200 > C0041912: Infection Upper Respiratory
AP: 0.9371 - AUC-ROC: 0.9371 - AUC-PR: 0.9566 - P@50: 0.9600 > C0037023: salivary gland inflammation
AP: 0.9145 - AUC-ROC: 0.9145 - AUC-PR: 0.9557 - P@50: 0.8600 > C1269683: major depression
AP: 0.8848 - AUC-ROC: 0.8848 - AUC-PR: 0.9316 - P@50: 0.9200 > C0032781: Post nasal drip
AP: 0.9426 - AUC-ROC: 0.9426 - AUC-PR: 0.9575 - P@50: 0.9800 > C0028081: night sweat
AP: 0.9439 - AUC-ROC: 0.9439 - AUC-PR: 0.9624 - P@50: 0.9600 > C0027339: Nail disorder
AP: 0.9104 - AUC-ROC: 0.9104 - AUC-PR: 0.9406 - P@50: 0.9200 > C0013473: eating disorder
AP: 0.9112 - AUC-ROC: 0.9112 - AUC-PR: 0.9469 - P@50: 0.9000 > C0011616: contact dermatitis
AP: 0.9749 - AUC-ROC: 0.9749 - AUC-PR: 0.9792 - P@50: 0.9400 > C0002884: anaemia hypochromic
AP: 0.8526 - AUC-ROC: 0.8526 - AUC-PR: 0.9309 - P@50: 0.9000 > C0079035: Bradyarrhythmia
AP: 0.8850 - AUC-ROC: 0.8850 - AUC-PR: 0.9228 - P@50: 0.9200 > C0014553: petit mal
AP: 0.9415 - AUC-ROC: 0.9415 - AUC-PR: 0.9643 - P@50: 0.9600 > C0080194: muscle strain
AP: 0.9099 - AUC-ROC: 0.9099 - AUC-PR: 0.9520 - P@50: 0.9200 > C0014394: Enuresis
AP: 0.9075 - AUC-ROC: 0.9075 - AUC-PR: 0.9450 - P@50: 0.9200 > C0011127: decubitus ulcer
AP: 0.9665 - AUC-ROC: 0.9665 - AUC-PR: 0.9716 - P@50: 0.9800 > C0264545: pleural fibrosis
AP: 0.9182 - AUC-ROC: 0.9182 - AUC-PR: 0.9462 - P@50: 0.9400 > C0029882: otitis media
AP: 0.9205 - AUC-ROC: 0.9205 - AUC-PR: 0.9495 - P@50: 0.9200 > C0014724: belching
AP: 0.8794 - AUC-ROC: 0.8794 - AUC-PR: 0.9268 - P@50: 0.8600 > C0232492: abdominal pain upper
AP: 0.8873 - AUC-ROC: 0.8873 - AUC-PR: 0.9415 - P@50: 0.9000 > C0018939: Blood disorder
AP: 0.9341 - AUC-ROC: 0.9341 - AUC-PR: 0.9544 - P@50: 0.9600 > C0003708: Arachnoiditis
AP: 0.9844 - AUC-ROC: 0.9844 - AUC-PR: 0.9846 - P@50: 1.0000 > C0016034: breast dysplasia
AP: 0.9224 - AUC-ROC: 0.9224 - AUC-PR: 0.9601 - P@50: 0.9400 > C0149726: pulmonary mass
AP: 0.9201 - AUC-ROC: 0.9201 - AUC-PR: 0.9462 - P@50: 0.9800 > C0575081: Abnormal Gait
AP: 0.8809 - AUC-ROC: 0.8809 - AUC-PR: 0.9400 - P@50: 0.8800 > C0037036: excessive salivation
AP: 0.9361 - AUC-ROC: 0.9361 - AUC-PR: 0.9657 - P@50: 0.9400 > C0024205: adenitis
AP: 0.8820 - AUC-ROC: 0.8820 - AUC-PR: 0.9380 - P@50: 0.8600 > C0277925: Cold extremities
AP: 0.9454 - AUC-ROC: 0.9454 - AUC-PR: 0.9661 - P@50: 0.9400 > C0156369: Uterine polyp
AP: 0.9563 - AUC-ROC: 0.9563 - AUC-PR: 0.9656 - P@50: 0.9800 > C0242301: furuncle
AP: 0.9353 - AUC-ROC: 0.9353 - AUC-PR: 0.9601 - P@50: 0.9400 > C0085619: orthopnea
AP: 0.8693 - AUC-ROC: 0.8693 - AUC-PR: 0.9277 - P@50: 0.8400 > C0037299: cutaneous ulcer
AP: 0.9393 - AUC-ROC: 0.9393 - AUC-PR: 0.9594 - P@50: 0.9400 > C0032617: polyuria
AP: 0.9225 - AUC-ROC: 0.9225 - AUC-PR: 0.9407 - P@50: 0.9400 > C0018418: gynaecomastia
AP: 0.8991 - AUC-ROC: 0.8991 - AUC-PR: 0.9338 - P@50: 0.9200 > C0018808: cardiac murmur
AP: 0.9644 - AUC-ROC: 0.9644 - AUC-PR: 0.9676 - P@50: 1.0000 > C0003872: psoriatic arthritis
AP: 0.9493 - AUC-ROC: 0.9493 - AUC-PR: 0.9673 - P@50: 0.9600 > C0001126: renal tubular acidosis
AP: 0.9653 - AUC-ROC: 0.9653 - AUC-PR: 0.9686 - P@50: 0.9800 > C0034072: Cor pulmonale
AP: 0.9373 - AUC-ROC: 0.9373 - AUC-PR: 0.9654 - P@50: 0.9000 > C0007286: carpal tunnel
AP: 0.9322 - AUC-ROC: 0.9322 - AUC-PR: 0.9520 - P@50: 1.0000 > C0029443: osteomyelitis
AP: 0.8958 - AUC-ROC: 0.8958 - AUC-PR: 0.9367 - P@50: 0.9000 > C0034067: emphysema
AP: 0.9400 - AUC-ROC: 0.9400 - AUC-PR: 0.9559 - P@50: 0.9600 > C0242422: Parkinson
AP: 0.8990 - AUC-ROC: 0.8990 - AUC-PR: 0.9355 - P@50: 0.9000 > C0033975: psychoses
AP: 0.9122 - AUC-ROC: 0.9122 - AUC-PR: 0.9403 - P@50: 0.9400 > C1456784: paranoia
AP: 0.8747 - AUC-ROC: 0.8747 - AUC-PR: 0.9246 - P@50: 0.8400 > C0026919: atypical mycobacterial infection
AP: 0.9168 - AUC-ROC: 0.9168 - AUC-PR: 0.9523 - P@50: 0.9400 > C0034880: hyperacusia
AP: 0.9463 - AUC-ROC: 0.9463 - AUC-PR: 0.9613 - P@50: 0.9400 > C0006846: cutaneous candidiasis
AP: 0.8973 - AUC-ROC: 0.8973 - AUC-PR: 0.9373 - P@50: 0.8800 > C0151744: Cardiac ischemia
AP: 0.9461 - AUC-ROC: 0.9461 - AUC-PR: 0.9555 - P@50: 0.9400 > C0019693: HIV disease
AP: 0.9352 - AUC-ROC: 0.9352 - AUC-PR: 0.9482 - P@50: 0.9200 > C0032305: Pneumocystis carinii pneumonia
AP: 0.9268 - AUC-ROC: 0.9268 - AUC-PR: 0.9480 - P@50: 0.9600 > C0019270: hernia
AP: 0.8905 - AUC-ROC: 0.8905 - AUC-PR: 0.9317 - P@50: 0.8600 > C0018802: Cardiac decompensation
AP: 0.8967 - AUC-ROC: 0.8967 - AUC-PR: 0.9400 - P@50: 0.8600 > C0043144: wheeze
AP: 0.9355 - AUC-ROC: 0.9355 - AUC-PR: 0.9570 - P@50: 0.9600 > C0029408: Osteoarthritis
AP: 0.9116 - AUC-ROC: 0.9116 - AUC-PR: 0.9412 - P@50: 0.9200 > C0001824: agranulocytoses
AP: 0.9600 - AUC-ROC: 0.9600 - AUC-PR: 0.9595 - P@50: 0.9800 > C0011630: Cutaneous mycosis
AP: 0.8963 - AUC-ROC: 0.8963 - AUC-PR: 0.9386 - P@50: 0.8200 > C0398353: Hypoventilation
AP: 0.9376 - AUC-ROC: 0.9376 - AUC-PR: 0.9566 - P@50: 0.9600 > C0036421: Scleroderma
AP: 0.9311 - AUC-ROC: 0.9311 - AUC-PR: 0.9542 - P@50: 0.9400 > C0024050: lower GI bleeding
AP: 0.9612 - AUC-ROC: 0.9612 - AUC-PR: 0.9805 - P@50: 0.9600 > C0006386: Bunion
AP: 0.9260 - AUC-ROC: 0.9260 - AUC-PR: 0.9567 - P@50: 0.9400 > C0020557: elevated triglycerides
AP: 0.9308 - AUC-ROC: 0.9308 - AUC-PR: 0.9461 - P@50: 0.9600 > C0026858: musculoskeletal pain
AP: 0.9086 - AUC-ROC: 0.9086 - AUC-PR: 0.9420 - P@50: 0.8800 > C0034212: pyoderma
AP: 0.9082 - AUC-ROC: 0.9082 - AUC-PR: 0.9466 - P@50: 0.9400 > C0009782: connective tissue disease
AP: 0.9075 - AUC-ROC: 0.9075 - AUC-PR: 0.9462 - P@50: 0.9200 > C0006118: brain neoplasm
AP: 0.9563 - AUC-ROC: 0.9563 - AUC-PR: 0.9632 - P@50: 1.0000 > C1253936: joint effusion
AP: 0.9049 - AUC-ROC: 0.9049 - AUC-PR: 0.9355 - P@50: 0.9200 > C0020433: Bilirubinaemia
AP: 0.9480 - AUC-ROC: 0.9480 - AUC-PR: 0.9580 - P@50: 0.9800 > C0016242: floaters
AP: 0.9577 - AUC-ROC: 0.9577 - AUC-PR: 0.9568 - P@50: 0.9400 > C0085786: fibrosing alveolitis
AP: 0.9517 - AUC-ROC: 0.9517 - AUC-PR: 0.9695 - P@50: 0.9600 > C0700594: radiculopathy
AP: 0.9627 - AUC-ROC: 0.9627 - AUC-PR: 0.9666 - P@50: 1.0000 > C0162834: hyperpigmentation
AP: 0.9266 - AUC-ROC: 0.9266 - AUC-PR: 0.9454 - P@50: 0.9800 > C0086543: cataract
AP: 0.8869 - AUC-ROC: 0.8869 - AUC-PR: 0.9250 - P@50: 0.9200 > C0040034: thrombocytopenia
AP: 0.9707 - AUC-ROC: 0.9707 - AUC-PR: 0.9750 - P@50: 1.0000 > C0015403: eye infection
AP: 0.9123 - AUC-ROC: 0.9123 - AUC-PR: 0.9431 - P@50: 0.9400 > C0020676: hypothyroid
AP: 0.9136 - AUC-ROC: 0.9136 - AUC-PR: 0.9470 - P@50: 0.9200 > C0042373: angiopathy
AP: 0.9700 - AUC-ROC: 0.9700 - AUC-PR: 0.9740 - P@50: 1.0000 > C0030353: optic disc edema
AP: 0.9548 - AUC-ROC: 0.9548 - AUC-PR: 0.9760 - P@50: 0.9600 > C0006012: borderline personality disorder
AP: 0.9104 - AUC-ROC: 0.9104 - AUC-PR: 0.9500 - P@50: 0.9000 > C0040136: thyroid neoplasia
AP: 0.9597 - AUC-ROC: 0.9597 - AUC-PR: 0.9683 - P@50: 1.0000 > C0026267: mitral valve prolapse
AP: 0.9592 - AUC-ROC: 0.9592 - AUC-PR: 0.9652 - P@50: 1.0000 > C0016059: fib
AP: 0.9814 - AUC-ROC: 0.9814 - AUC-PR: 0.9806 - P@50: 0.9600 > C0302592: carcinoma of the cervix
AP: 0.9341 - AUC-ROC: 0.9341 - AUC-PR: 0.9569 - P@50: 0.9800 > C0178415: elevated prostate specific antigen
AP: 0.8787 - AUC-ROC: 0.8787 - AUC-PR: 0.9385 - P@50: 0.9000 > C0750876: phlebitis superficial
AP: 0.9130 - AUC-ROC: 0.9130 - AUC-PR: 0.9374 - P@50: 0.9600 > C0034069: lung fibrosis
AP: 0.9119 - AUC-ROC: 0.9119 - AUC-PR: 0.9432 - P@50: 0.9400 > C0018674: head injury
AP: 0.9400 - AUC-ROC: 0.9400 - AUC-PR: 0.9546 - P@50: 0.9600 > C0029134: OPTIC NEURITIS
AP: 0.9508 - AUC-ROC: 0.9508 - AUC-PR: 0.9510 - P@50: 0.9800 > C0341163: Gastric ulcer perforated
AP: 0.9759 - AUC-ROC: 0.9759 - AUC-PR: 0.9788 - P@50: 0.9800 > C0023646: lichen planus
AP: 0.9392 - AUC-ROC: 0.9392 - AUC-PR: 0.9632 - P@50: 0.9800 > C0178282: Abdominal hernia
AP: 0.9280 - AUC-ROC: 0.9280 - AUC-PR: 0.9544 - P@50: 0.9400 > C0035302: Retinal artery occlusion
AP: 0.8828 - AUC-ROC: 0.8828 - AUC-PR: 0.9319 - P@50: 0.8200 > C0018800: cardiac enlargement
AP: 0.8617 - AUC-ROC: 0.8617 - AUC-PR: 0.9284 - P@50: 0.8400 > C0032308: pneumonia staphylococcal
AP: 0.9875 - AUC-ROC: 0.9875 - AUC-PR: 0.9877 - P@50: 1.0000 > C0271468: Eustachian tube disorder
AP: 0.8783 - AUC-ROC: 0.8783 - AUC-PR: 0.9178 - P@50: 0.9400 > C0018818: ventricular septal defect
AP: 0.9088 - AUC-ROC: 0.9088 - AUC-PR: 0.9445 - P@50: 0.9200 > C0003504: aortic regurgitation
AP: 0.9022 - AUC-ROC: 0.9022 - AUC-PR: 0.9365 - P@50: 0.9400 > C0020255: hydrocephalus
AP: 0.9543 - AUC-ROC: 0.9543 - AUC-PR: 0.9615 - P@50: 0.9800 > C0558489: kidney pain
AP: 0.9239 - AUC-ROC: 0.9239 - AUC-PR: 0.9473 - P@50: 0.9600 > C0035309: Disorder Retinal
AP: 0.8836 - AUC-ROC: 0.8836 - AUC-PR: 0.9246 - P@50: 0.9200 > C0018965: blood in urine
AP: 0.9574 - AUC-ROC: 0.9574 - AUC-PR: 0.9679 - P@50: 0.9200 > C0262414: cervical vertebral fracture
AP: 0.8941 - AUC-ROC: 0.8941 - AUC-PR: 0.9341 - P@50: 0.9200 > C0022661: Chronic Kidney Disease
AP: 0.9582 - AUC-ROC: 0.9582 - AUC-PR: 0.9734 - P@50: 0.9600 > C0085580: essential hypertension
AP: 0.9301 - AUC-ROC: 0.9301 - AUC-PR: 0.9545 - P@50: 0.9400 > C0014335: enteritis
AP: 0.9394 - AUC-ROC: 0.9394 - AUC-PR: 0.9566 - P@50: 0.9400 > C0242172: Pelvic Inflammatory Disease
AP: 0.9070 - AUC-ROC: 0.9070 - AUC-PR: 0.9400 - P@50: 0.9400 > C0027121: muscle inflammation
AP: 0.9078 - AUC-ROC: 0.9078 - AUC-PR: 0.9447 - P@50: 0.8600 > C0522055: abnormal ECG
AP: 0.9536 - AUC-ROC: 0.9536 - AUC-PR: 0.9613 - P@50: 0.9600 > C0011881: Diabetic Nephropathy
AP: 0.9123 - AUC-ROC: 0.9123 - AUC-PR: 0.9398 - P@50: 0.9400 > C0003486: aortic aneurysm
AP: 0.9196 - AUC-ROC: 0.9196 - AUC-PR: 0.9484 - P@50: 0.9600 > C0005747: Blepharospasm
AP: 0.9003 - AUC-ROC: 0.9003 - AUC-PR: 0.9353 - P@50: 0.9200 > C0032227: Pleural Effusion
AP: 0.9941 - AUC-ROC: 0.9941 - AUC-PR: 0.9938 - P@50: 1.0000 > C0476427: abnormal cervical smear
AP: 0.8947 - AUC-ROC: 0.8947 - AUC-PR: 0.9338 - P@50: 0.8800 > C0344232: blurred vision
AP: 0.9893 - AUC-ROC: 0.9893 - AUC-PR: 0.9904 - P@50: 0.9600 > C0004690: balanitis
AP: 0.9594 - AUC-ROC: 0.9594 - AUC-PR: 0.9712 - P@50: 0.9800 > C0020505: hyperalimentation
AP: 0.8905 - AUC-ROC: 0.8905 - AUC-PR: 0.9351 - P@50: 0.8400 > C1145670: respiratory failure
AP: 0.9278 - AUC-ROC: 0.9278 - AUC-PR: 0.9742 - P@50: 0.9600 > C0009375: colon neoplasm
AP: 0.8971 - AUC-ROC: 0.8971 - AUC-PR: 0.9364 - P@50: 0.9200 > C0008033: pleural pain
AP: 0.8896 - AUC-ROC: 0.8896 - AUC-PR: 0.9224 - P@50: 0.9200 > C0151798: hepatic necrosis
AP: 0.9949 - AUC-ROC: 0.9949 - AUC-PR: 0.9946 - P@50: 1.0000 > C0007860: cervicitis
AP: 0.9648 - AUC-ROC: 0.9648 - AUC-PR: 0.9727 - P@50: 0.9800 > C0027531: injury of neck
AP: 0.9420 - AUC-ROC: 0.9420 - AUC-PR: 0.9553 - P@50: 1.0000 > C0016199: flank pain
AP: 0.9142 - AUC-ROC: 0.9142 - AUC-PR: 0.9436 - P@50: 0.9600 > C0243010: encephalitis viral
AP: 0.9690 - AUC-ROC: 0.9690 - AUC-PR: 0.9759 - P@50: 0.9800 > C0002064: respiratory alkalosis
AP: 0.9392 - AUC-ROC: 0.9392 - AUC-PR: 0.9502 - P@50: 0.9800 > C1510475: diverticulosis
AP: 0.8816 - AUC-ROC: 0.8816 - AUC-PR: 0.9272 - P@50: 0.9000 > C0038450: stridor
AP: 0.8796 - AUC-ROC: 0.8796 - AUC-PR: 0.9238 - P@50: 0.9200 > C0043096: loss of weight
AP: 0.8676 - AUC-ROC: 0.8676 - AUC-PR: 0.9261 - P@50: 0.8400 > C0024312: Lymphocytes decreased
AP: 0.9625 - AUC-ROC: 0.9625 - AUC-PR: 0.9634 - P@50: 0.9800 > C0040590: tracheostomy
AP: 0.9317 - AUC-ROC: 0.9317 - AUC-PR: 0.9530 - P@50: 0.9400 > C0020502: hyperparathyroidism
AP: 0.9360 - AUC-ROC: 0.9360 - AUC-PR: 0.9543 - P@50: 0.9600 > C0151825: bone pain
AP: 0.8884 - AUC-ROC: 0.8884 - AUC-PR: 0.9341 - P@50: 0.8400 > C0020621: hypokalaemia
AP: 0.9086 - AUC-ROC: 0.9086 - AUC-PR: 0.9362 - P@50: 0.9400 > C0005779: Clotting
AP: 0.9944 - AUC-ROC: 0.9944 - AUC-PR: 0.9948 - P@50: 1.0000 > C0276143: Viral Pharyngitis
AP: 0.9172 - AUC-ROC: 0.9172 - AUC-PR: 0.9365 - P@50: 0.9600 > C0522224: palsies
AP: 0.9380 - AUC-ROC: 0.9380 - AUC-PR: 0.9544 - P@50: 0.9600 > C0027424: nasal congestion
AP: 0.9245 - AUC-ROC: 0.9245 - AUC-PR: 0.9468 - P@50: 0.9600 > C0036454: scotoma
AP: 0.9121 - AUC-ROC: 0.9121 - AUC-PR: 0.9343 - P@50: 0.9800 > C0003850: arteriosclerosis
AP: 0.9386 - AUC-ROC: 0.9386 - AUC-PR: 0.9530 - P@50: 0.9800 > C0600139: Carcinoma of Prostate
AP: 0.9320 - AUC-ROC: 0.9320 - AUC-PR: 0.9528 - P@50: 0.9600 > C0028738: nystagmus
AP: 0.8989 - AUC-ROC: 0.8989 - AUC-PR: 0.9340 - P@50: 0.9000 > C0020437: Blood Calcium Increased
AP: 0.9079 - AUC-ROC: 0.9079 - AUC-PR: 0.9339 - P@50: 0.9000 > C0011848: diabetes insipidus
AP: 0.9292 - AUC-ROC: 0.9292 - AUC-PR: 0.9548 - P@50: 0.9600 > C0022679: renal cyst
AP: 0.9194 - AUC-ROC: 0.9194 - AUC-PR: 0.9486 - P@50: 0.9600 > C0005001: benign prostatic hyperplasia
AP: 0.9249 - AUC-ROC: 0.9249 - AUC-PR: 0.9598 - P@50: 0.9400 > C0015423: eyelid diseases
AP: 0.9216 - AUC-ROC: 0.9216 - AUC-PR: 0.9462 - P@50: 0.9400 > C0009241: cognitive disorder
AP: 0.9273 - AUC-ROC: 0.9273 - AUC-PR: 0.9547 - P@50: 0.9400 > C0236048: gastric polyps
AP: 0.9031 - AUC-ROC: 0.9031 - AUC-PR: 0.9447 - P@50: 0.9200 > C0035258: Ekbom Syndrome
AP: 0.9795 - AUC-ROC: 0.9795 - AUC-PR: 0.9802 - P@50: 1.0000 > C0039520: Tenosynovitis
AP: 0.9317 - AUC-ROC: 0.9317 - AUC-PR: 0.9552 - P@50: 0.9200 > C0020162: humerus fracture
AP: 0.9648 - AUC-ROC: 0.9648 - AUC-PR: 0.9720 - P@50: 0.9600 > C0151971: intestinal ulcer
AP: 0.9210 - AUC-ROC: 0.9210 - AUC-PR: 0.9464 - P@50: 0.9200 > C0149696: food intolerance
AP: 0.9144 - AUC-ROC: 0.9144 - AUC-PR: 0.9502 - P@50: 0.9600 > C0033038: Ejaculation Premature
AP: 0.9520 - AUC-ROC: 0.9520 - AUC-PR: 0.9539 - P@50: 0.9000 > C1527407: eosinophilic pneumonia
AP: 0.8668 - AUC-ROC: 0.8668 - AUC-PR: 0.9207 - P@50: 0.8200 > C0085593: chill
AP: 0.9462 - AUC-ROC: 0.9462 - AUC-PR: 0.9641 - P@50: 0.9800 > C0011124: Decreased Libido
AP: 0.9389 - AUC-ROC: 0.9389 - AUC-PR: 0.9588 - P@50: 0.9400 > C0003079: Anisocoria
AP: 0.9728 - AUC-ROC: 0.9728 - AUC-PR: 0.9737 - P@50: 0.9200 > C0238154: epidural hematoma
AP: 0.9610 - AUC-ROC: 0.9610 - AUC-PR: 0.9689 - P@50: 0.9400 > C0178428: sinus arrest
AP: 0.8660 - AUC-ROC: 0.8660 - AUC-PR: 0.9257 - P@50: 0.8600 > C0267596: haemorrhage rectum
AP: 0.9384 - AUC-ROC: 0.9384 - AUC-PR: 0.9644 - P@50: 0.9600 > C0015468: face pain
AP: 0.9137 - AUC-ROC: 0.9137 - AUC-PR: 0.9408 - P@50: 0.9800 > C0017601: glaucoma
AP: 0.9489 - AUC-ROC: 0.9489 - AUC-PR: 0.9578 - P@50: 0.9800 > C0037928: myelopathy
AP: 0.9104 - AUC-ROC: 0.9104 - AUC-PR: 0.9378 - P@50: 0.9800 > C0008350: cholelithiasis
AP: 0.9493 - AUC-ROC: 0.9493 - AUC-PR: 0.9589 - P@50: 0.9000 > C0015645: fasciitis
AP: 0.9062 - AUC-ROC: 0.9062 - AUC-PR: 0.9403 - P@50: 0.9200 > C0004245: atrioventricular block
AP: 0.9226 - AUC-ROC: 0.9226 - AUC-PR: 0.9554 - P@50: 0.9600 > C0025202: malignant melanoma
AP: 0.9990 - AUC-ROC: 0.9990 - AUC-PR: 0.9989 - P@50: 1.0000 > C0600327: toxic shock
AP: 0.9165 - AUC-ROC: 0.9165 - AUC-PR: 0.9407 - P@50: 0.9000 > C0221245: Rhagades
AP: 0.9019 - AUC-ROC: 0.9019 - AUC-PR: 0.9362 - P@50: 0.9400 > C0003962: ascites
AP: 0.9186 - AUC-ROC: 0.9186 - AUC-PR: 0.9505 - P@50: 0.9600 > C0035305: Detached retina
AP: 0.9549 - AUC-ROC: 0.9549 - AUC-PR: 0.9635 - P@50: 1.0000 > C0022602: actinic keratosis
AP: 0.9096 - AUC-ROC: 0.9096 - AUC-PR: 0.9465 - P@50: 0.8800 > C0003864: arthritis
AP: 0.9276 - AUC-ROC: 0.9276 - AUC-PR: 0.9559 - P@50: 0.9200 > C0025289: meningitides
AP: 0.9134 - AUC-ROC: 0.9134 - AUC-PR: 0.9445 - P@50: 0.9000 > C0002622: Amnesia
AP: 0.9413 - AUC-ROC: 0.9413 - AUC-PR: 0.9682 - P@50: 0.9400 > C0262431: Spinal Compression Fracture
AP: 0.8691 - AUC-ROC: 0.8691 - AUC-PR: 0.9259 - P@50: 0.7600 > C0009938: bruise
AP: 0.9317 - AUC-ROC: 0.9317 - AUC-PR: 0.9526 - P@50: 0.9800 > C0042384: angiitis
AP: 0.9188 - AUC-ROC: 0.9188 - AUC-PR: 0.9465 - P@50: 0.9400 > C0018944: haematoma
AP: 0.9290 - AUC-ROC: 0.9290 - AUC-PR: 0.9557 - P@50: 0.9200 > C0035455: Rhinitis
AP: 0.9056 - AUC-ROC: 0.9056 - AUC-PR: 0.9367 - P@50: 0.9000 > C0311394: difficulty in walking
AP: 0.9554 - AUC-ROC: 0.9554 - AUC-PR: 0.9698 - P@50: 0.9800 > C0025323: heavy menstrual period
AP: 0.9694 - AUC-ROC: 0.9694 - AUC-PR: 0.9739 - P@50: 0.9400 > C0027430: nasal polyp
AP: 0.9556 - AUC-ROC: 0.9556 - AUC-PR: 0.9731 - P@50: 0.9800 > C0013146: abuse
AP: 0.9082 - AUC-ROC: 0.9082 - AUC-PR: 0.9457 - P@50: 0.8400 > C0013428: dysuria
AP: 0.9080 - AUC-ROC: 0.9080 - AUC-PR: 0.9458 - P@50: 0.8800 > C0017672: glossodynia
AP: 0.8975 - AUC-ROC: 0.8975 - AUC-PR: 0.9329 - P@50: 0.9400 > C0008031: chest pain
AP: 0.9458 - AUC-ROC: 0.9458 - AUC-PR: 0.9545 - P@50: 0.9800 > C0262385: autonomic instability
AP: 0.9675 - AUC-ROC: 0.9675 - AUC-PR: 0.9678 - P@50: 0.9400 > C0008312: primary biliary cirrhosis
AP: 0.8737 - AUC-ROC: 0.8737 - AUC-PR: 0.9207 - P@50: 0.8400 > C0497247: arterial pressure NOS increased
AP: 0.9621 - AUC-ROC: 0.9621 - AUC-PR: 0.9718 - P@50: 1.0000 > C0435630: wrist fracture
AP: 0.8816 - AUC-ROC: 0.8816 - AUC-PR: 0.9245 - P@50: 0.8600 > C0033687: proteinuria
AP: 0.8874 - AUC-ROC: 0.8874 - AUC-PR: 0.9027 - P@50: 0.8600 > C0152169: renal colic
AP: 0.9273 - AUC-ROC: 0.9273 - AUC-PR: 0.9496 - P@50: 0.9600 > C0017675: Glossitis
AP: 0.9302 - AUC-ROC: 0.9302 - AUC-PR: 0.9574 - P@50: 0.9200 > C0151723: Hypomagnesaemia
AP: 0.9103 - AUC-ROC: 0.9103 - AUC-PR: 0.9493 - P@50: 0.8800 > C0162298: joint stiffness
AP: 0.9177 - AUC-ROC: 0.9177 - AUC-PR: 0.9398 - P@50: 0.9800 > C0038002: enlarged spleen
AP: 0.9139 - AUC-ROC: 0.9139 - AUC-PR: 0.9422 - P@50: 0.9200 > C0024121: lung neoplasms
AP: 0.9200 - AUC-ROC: 0.9200 - AUC-PR: 0.9553 - P@50: 0.9000 > C0159877: ankle fracture
AP: 0.9785 - AUC-ROC: 0.9785 - AUC-PR: 0.9816 - P@50: 0.9800 > C0003868: gouty arthritis
AP: 0.8932 - AUC-ROC: 0.8932 - AUC-PR: 0.9407 - P@50: 0.8200 > C0028084: nightmare
AP: 0.9042 - AUC-ROC: 0.9042 - AUC-PR: 0.9497 - P@50: 0.9000 > C0085682: Hypophosphataemia
AP: 0.9561 - AUC-ROC: 0.9561 - AUC-PR: 0.9684 - P@50: 0.9800 > C0004601: back injury
AP: 0.9238 - AUC-ROC: 0.9238 - AUC-PR: 0.9521 - P@50: 0.9400 > C0031538: phimosis
AP: 0.8941 - AUC-ROC: 0.8941 - AUC-PR: 0.9341 - P@50: 0.8800 > C0032290: aspiration pneumonia
AP: 0.9334 - AUC-ROC: 0.9334 - AUC-PR: 0.9622 - P@50: 0.9600 > C0042164: intraocular inflammation
AP: 0.9571 - AUC-ROC: 0.9571 - AUC-PR: 0.9644 - P@50: 0.9200 > C0016412: folate deficiency
AP: 0.8964 - AUC-ROC: 0.8964 - AUC-PR: 0.9286 - P@50: 0.9200 > C0027707: Interstitial nephritis
AP: 0.8779 - AUC-ROC: 0.8779 - AUC-PR: 0.9252 - P@50: 0.8400 > C0039239: sinus tachycardia
AP: 0.9247 - AUC-ROC: 0.9247 - AUC-PR: 0.9578 - P@50: 0.8800 > C0028754: obesity
AP: 0.9013 - AUC-ROC: 0.9013 - AUC-PR: 0.9409 - P@50: 0.8800 > C0152031: joint swelling
AP: 0.9428 - AUC-ROC: 0.9428 - AUC-PR: 0.9617 - P@50: 0.9800 > C0005586: bipolar disorder
AP: 0.8955 - AUC-ROC: 0.8955 - AUC-PR: 0.9352 - P@50: 0.8800 > C0008767: Scar
AP: 0.8922 - AUC-ROC: 0.8922 - AUC-PR: 0.9341 - P@50: 0.8800 > C0009806: constipated
AP: 0.9855 - AUC-ROC: 0.9855 - AUC-PR: 0.9858 - P@50: 1.0000 > C0021345: infectious mononucleosis
AP: 0.8835 - AUC-ROC: 0.8835 - AUC-PR: 0.9312 - P@50: 0.8400 > C0151786: muscle weakness
AP: 0.9612 - AUC-ROC: 0.9612 - AUC-PR: 0.9727 - P@50: 0.9800 > C0006444: bursitis
AP: 0.9639 - AUC-ROC: 0.9639 - AUC-PR: 0.9717 - P@50: 0.9800 > C0016807: intestinal functional disorder
AP: 0.9348 - AUC-ROC: 0.9348 - AUC-PR: 0.9605 - P@50: 0.9400 > C0025286: meningioma
AP: 0.9419 - AUC-ROC: 0.9419 - AUC-PR: 0.9653 - P@50: 0.9600 > C0205929: Anal fistula
AP: 0.8546 - AUC-ROC: 0.8546 - AUC-PR: 0.9309 - P@50: 0.8800 > C0030299: pancreatic pseudocyst
AP: 0.9202 - AUC-ROC: 0.9202 - AUC-PR: 0.9489 - P@50: 0.9400 > C0027769: nervous tension
AP: 0.9093 - AUC-ROC: 0.9093 - AUC-PR: 0.9390 - P@50: 0.9800 > C0438215: Abnormal Laboratory Findings
AP: 0.8790 - AUC-ROC: 0.8790 - AUC-PR: 0.9199 - P@50: 0.8800 > C0023418: Leukaemia
AP: 0.9075 - AUC-ROC: 0.9075 - AUC-PR: 0.9424 - P@50: 0.8600 > C0029456: osteoporosis
AP: 0.8998 - AUC-ROC: 0.8998 - AUC-PR: 0.9387 - P@50: 0.9600 > C0699791: Gastric Cancer
AP: 0.9390 - AUC-ROC: 0.9390 - AUC-PR: 0.9576 - P@50: 0.9400 > C0239739: gingival pain
AP: 0.9208 - AUC-ROC: 0.9208 - AUC-PR: 0.9481 - P@50: 0.9400 > C0021845: intestinal perforation
AP: 0.9178 - AUC-ROC: 0.9178 - AUC-PR: 0.9557 - P@50: 0.9400 > C0262627: Seroma
AP: 0.8555 - AUC-ROC: 0.8555 - AUC-PR: 0.9179 - P@50: 0.8200 > C0013182: Drug hypersensitivity
AP: 0.9508 - AUC-ROC: 0.9508 - AUC-PR: 0.9664 - P@50: 0.9400 > C0020619: hypogonadism
AP: 0.8873 - AUC-ROC: 0.8873 - AUC-PR: 0.9259 - P@50: 0.9200 > C0018790: asystole
AP: 0.8973 - AUC-ROC: 0.8973 - AUC-PR: 0.9362 - P@50: 0.9000 > C0001418: adenocarcinoma
AP: 0.8914 - AUC-ROC: 0.8914 - AUC-PR: 0.9311 - P@50: 0.9000 > C0018932: haematochezia
AP: 0.9698 - AUC-ROC: 0.9698 - AUC-PR: 0.9756 - P@50: 0.9600 > C0038833: superior vena cava syndrome
AP: 0.9211 - AUC-ROC: 0.9211 - AUC-PR: 0.9400 - P@50: 0.9200 > C0019521: hiccough
AP: 0.9131 - AUC-ROC: 0.9131 - AUC-PR: 0.9439 - P@50: 0.9600 > C0038358: gastric ulcer
AP: 0.9038 - AUC-ROC: 0.9038 - AUC-PR: 0.9391 - P@50: 0.8800 > C0016204: flatulence
AP: 0.9671 - AUC-ROC: 0.9671 - AUC-PR: 0.9740 - P@50: 0.9800 > C0007462: causalgia
AP: 0.9777 - AUC-ROC: 0.9777 - AUC-PR: 0.9811 - P@50: 0.9800 > C0002726: amyloidosis
AP: 0.9130 - AUC-ROC: 0.9130 - AUC-PR: 0.9556 - P@50: 0.8600 > C0699744: ear infection
AP: 0.9152 - AUC-ROC: 0.9152 - AUC-PR: 0.9526 - P@50: 0.9200 > C0149721: left ventricular hypertrophy
AP: 0.8761 - AUC-ROC: 0.8761 - AUC-PR: 0.9284 - P@50: 0.8400 > C0085602: excessive thirst
AP: 0.9483 - AUC-ROC: 0.9483 - AUC-PR: 0.9680 - P@50: 0.9400 > C0032584: polyp
AP: 0.9352 - AUC-ROC: 0.9352 - AUC-PR: 0.9543 - P@50: 0.9800 > C0003873: Arthritis rheumatoid
AP: 0.8724 - AUC-ROC: 0.8724 - AUC-PR: 0.9235 - P@50: 0.8600 > C0456909: blindness
AP: 0.9260 - AUC-ROC: 0.9260 - AUC-PR: 0.9506 - P@50: 0.9400 > C0018991: hemiplegia
AP: 0.9321 - AUC-ROC: 0.9321 - AUC-PR: 0.9499 - P@50: 0.9600 > C0030920: gastroduodenal ulcer
AP: 0.8587 - AUC-ROC: 0.8587 - AUC-PR: 0.9130 - P@50: 0.8800 > C0000768: birth defect
AP: 0.9172 - AUC-ROC: 0.9172 - AUC-PR: 0.9438 - P@50: 0.9200 > C0004144: atelectasis
AP: 0.8930 - AUC-ROC: 0.8930 - AUC-PR: 0.9347 - P@50: 0.8800 > C0012569: Diplopia
AP: 0.8862 - AUC-ROC: 0.8862 - AUC-PR: 0.9344 - P@50: 0.8800 > C0020651: Hypotension Orthostatic
AP: 0.9372 - AUC-ROC: 0.9372 - AUC-PR: 0.9497 - P@50: 0.9200 > C0152459: Skin Striae
AP: 0.9477 - AUC-ROC: 0.9477 - AUC-PR: 0.9616 - P@50: 0.9600 > C0041952: calculus ureteric
AP: 0.9764 - AUC-ROC: 0.9764 - AUC-PR: 0.9779 - P@50: 1.0000 > C0162283: Nephrogenic diabetes insipidus
AP: 0.9479 - AUC-ROC: 0.9479 - AUC-PR: 0.9602 - P@50: 0.9800 > C0151517: Atrioventricular block complete
AP: 0.9266 - AUC-ROC: 0.9266 - AUC-PR: 0.9498 - P@50: 0.9400 > C0004626: bacterial pneumonia
AP: 0.8556 - AUC-ROC: 0.8556 - AUC-PR: 0.9100 - P@50: 0.8200 > C0036572: convulsion
AP: 0.8867 - AUC-ROC: 0.8867 - AUC-PR: 0.9306 - P@50: 0.8800 > C0042487: phlebothrombosis
AP: 0.9380 - AUC-ROC: 0.9380 - AUC-PR: 0.9608 - P@50: 0.9400 > C0020565: breast enlargement
AP: 0.9352 - AUC-ROC: 0.9352 - AUC-PR: 0.9617 - P@50: 0.9400 > C0034902: aplasia pure red cell
AP: 0.9182 - AUC-ROC: 0.9182 - AUC-PR: 0.9529 - P@50: 0.9400 > C0341047: parotid gland enlargement
AP: 0.9588 - AUC-ROC: 0.9588 - AUC-PR: 0.9697 - P@50: 0.9800 > C0011882: Diabetic neuropathy
AP: 0.8914 - AUC-ROC: 0.8914 - AUC-PR: 0.9327 - P@50: 0.8800 > C0042571: spinning sensation
AP: 0.9168 - AUC-ROC: 0.9168 - AUC-PR: 0.9468 - P@50: 0.9600 > C0013298: duodenitis
AP: 0.9226 - AUC-ROC: 0.9226 - AUC-PR: 0.9503 - P@50: 0.9400 > C0917798: cerebral ischaemia
AP: 0.9059 - AUC-ROC: 0.9059 - AUC-PR: 0.9448 - P@50: 0.9000 > C0027709: nephrocalcinosis
AP: 0.9130 - AUC-ROC: 0.9130 - AUC-PR: 0.9422 - P@50: 0.9200 > C0015802: femur fracture
AP: 0.9289 - AUC-ROC: 0.9289 - AUC-PR: 0.9582 - P@50: 0.9400 > C0221150: odynophagia
AP: 0.9336 - AUC-ROC: 0.9336 - AUC-PR: 0.9525 - P@50: 0.9800 > C0085614: Atrioventricular block first degree
AP: 0.8406 - AUC-ROC: 0.8406 - AUC-PR: 0.9074 - P@50: 0.7400 > C0015230: eruption
AP: 0.8961 - AUC-ROC: 0.8961 - AUC-PR: 0.9300 - P@50: 0.9200 > C0151766: Abnormal LFTs
AP: 0.9705 - AUC-ROC: 0.9705 - AUC-PR: 0.9779 - P@50: 0.9800 > C0031099: periodontitis
AP: 0.9430 - AUC-ROC: 0.9430 - AUC-PR: 0.9646 - P@50: 0.9400 > C0039591: testes pain
AP: 0.8773 - AUC-ROC: 0.8773 - AUC-PR: 0.9304 - P@50: 0.8200 > C0851578: sleep disorder
AP: 0.8725 - AUC-ROC: 0.8725 - AUC-PR: 0.9256 - P@50: 0.9000 > C0031256: petechia
AP: 0.8953 - AUC-ROC: 0.8953 - AUC-PR: 0.9406 - P@50: 0.8800 > C0151436: allergic vasculitis
AP: 0.9135 - AUC-ROC: 0.9135 - AUC-PR: 0.9456 - P@50: 0.8800 > C0026946: fungal disease
AP: 0.9143 - AUC-ROC: 0.9143 - AUC-PR: 0.9469 - P@50: 0.9400 > C0038525: subarachnoid haemorrhage
AP: 0.9699 - AUC-ROC: 0.9699 - AUC-PR: 0.9803 - P@50: 0.9800 > C0038012: spondylitis
AP: 0.8988 - AUC-ROC: 0.8988 - AUC-PR: 0.9284 - P@50: 0.8600 > C0035220: neonatal respiratory distress syndrome
AP: 0.9377 - AUC-ROC: 0.9377 - AUC-PR: 0.9564 - P@50: 0.9800 > C0085096: Disorder Peripheral Vascular
AP: 0.9144 - AUC-ROC: 0.9144 - AUC-PR: 0.9463 - P@50: 0.9400 > C0151706: bleeding Vaginal
AP: 0.9646 - AUC-ROC: 0.9646 - AUC-PR: 0.9745 - P@50: 0.9800 > C0006384: bundle branch block
AP: 0.9021 - AUC-ROC: 0.9021 - AUC-PR: 0.9377 - P@50: 0.9800 > C0012833: dizziness
AP: 0.9049 - AUC-ROC: 0.9049 - AUC-PR: 0.9319 - P@50: 0.9400 > C0022346: icterus
AP: 0.9523 - AUC-ROC: 0.9523 - AUC-PR: 0.9725 - P@50: 0.9600 > C0040213: costochondritis
AP: 0.9332 - AUC-ROC: 0.9332 - AUC-PR: 0.9539 - P@50: 0.9600 > C0016169: fistula
AP: 0.9262 - AUC-ROC: 0.9262 - AUC-PR: 0.9518 - P@50: 0.9200 > C0017168: acid reflux
AP: 0.9254 - AUC-ROC: 0.9254 - AUC-PR: 0.9440 - P@50: 0.9800 > C0020040: hot flash
AP: 0.9424 - AUC-ROC: 0.9424 - AUC-PR: 0.9637 - P@50: 0.9400 > C0158252: intervertebral disc disorder
AP: 0.9516 - AUC-ROC: 0.9516 - AUC-PR: 0.9674 - P@50: 0.9600 > C0423798: Easy bruisability
AP: 0.9528 - AUC-ROC: 0.9528 - AUC-PR: 0.9626 - P@50: 0.9800 > C0031350: pharyngeal inflammation
AP: 0.9806 - AUC-ROC: 0.9806 - AUC-PR: 0.9815 - P@50: 0.9400 > C0027022: MPD
AP: 0.9079 - AUC-ROC: 0.9079 - AUC-PR: 0.9371 - P@50: 0.9400 > C0006826: cancer
AP: 0.9315 - AUC-ROC: 0.9315 - AUC-PR: 0.9558 - P@50: 0.9600 > C0678222: Breast cancer
AP: 0.9478 - AUC-ROC: 0.9478 - AUC-PR: 0.9665 - P@50: 0.9600 > C0040261: onychomycosis
AP: 0.9119 - AUC-ROC: 0.9119 - AUC-PR: 0.9444 - P@50: 0.9200 > C0020473: hyperlipaemia
AP: 0.9012 - AUC-ROC: 0.9012 - AUC-PR: 0.9373 - P@50: 0.8800 > C0013362: dysarthria
AP: 0.9072 - AUC-ROC: 0.9072 - AUC-PR: 0.9432 - P@50: 0.9200 > C0011053: deafness
AP: 0.9235 - AUC-ROC: 0.9235 - AUC-PR: 0.9505 - P@50: 0.9400 > C0019825: Hoarseness
AP: 0.9624 - AUC-ROC: 0.9624 - AUC-PR: 0.9715 - P@50: 0.9800 > C0014863: esophageal spasm
AP: 0.9019 - AUC-ROC: 0.9019 - AUC-PR: 0.9391 - P@50: 0.8800 > C0342579: Electrolyte disorder
AP: 0.8986 - AUC-ROC: 0.8986 - AUC-PR: 0.9384 - P@50: 0.8400 > C0004096: asthma
AP: 0.9083 - AUC-ROC: 0.9083 - AUC-PR: 0.9406 - P@50: 0.9000 > C0149725: Chest infection
AP: 0.9114 - AUC-ROC: 0.9114 - AUC-PR: 0.9387 - P@50: 0.9400 > C0019557: hip fracture
AP: 0.9277 - AUC-ROC: 0.9277 - AUC-PR: 0.9539 - P@50: 0.9400 > C0152021: congenital heart disease
AP: 0.9094 - AUC-ROC: 0.9094 - AUC-PR: 0.9520 - P@50: 0.9400 > C0267716: incisional hernia
AP: 0.9665 - AUC-ROC: 0.9665 - AUC-PR: 0.9684 - P@50: 0.9400 > C0027092: myopia
AP: 0.9209 - AUC-ROC: 0.9209 - AUC-PR: 0.9423 - P@50: 0.9400 > C0014866: esophageal stenosis
AP: 0.9420 - AUC-ROC: 0.9420 - AUC-PR: 0.9674 - P@50: 0.9600 > C0085648: synovial cyst
AP: 0.8853 - AUC-ROC: 0.8853 - AUC-PR: 0.9330 - P@50: 0.7800 > C0011168: deglutition disorder
AP: 0.8926 - AUC-ROC: 0.8926 - AUC-PR: 0.9317 - P@50: 0.8800 > C0018681: Head ache
AP: 0.9534 - AUC-ROC: 0.9534 - AUC-PR: 0.9652 - P@50: 0.9600 > C0085652: pyoderma gangrenosum
AP: 0.8918 - AUC-ROC: 0.8918 - AUC-PR: 0.9356 - P@50: 0.8600 > C0003578: Apnea
AP: 0.8715 - AUC-ROC: 0.8715 - AUC-PR: 0.9224 - P@50: 0.9000 > C0019163: hepatitis B
AP: 0.8842 - AUC-ROC: 0.8842 - AUC-PR: 0.9305 - P@50: 0.8000 > C0009676: confusion
AP: 0.9849 - AUC-ROC: 0.9849 - AUC-PR: 0.9874 - P@50: 0.9800 > C1258666: ganglion
AP: 0.8970 - AUC-ROC: 0.8970 - AUC-PR: 0.9316 - P@50: 0.9200 > C0020672: decreased body temperature
AP: 0.9709 - AUC-ROC: 0.9709 - AUC-PR: 0.9750 - P@50: 0.9800 > C0038019: spondylosis
AP: 0.9566 - AUC-ROC: 0.9566 - AUC-PR: 0.9624 - P@50: 1.0000 > C0004610: Bacteraemia
AP: 0.9058 - AUC-ROC: 0.9058 - AUC-PR: 0.9475 - P@50: 0.9200 > C0020488: hypernatraemia
AP: 0.9652 - AUC-ROC: 0.9652 - AUC-PR: 0.9667 - P@50: 0.9200 > C0039446: telangiectases
AP: 0.8826 - AUC-ROC: 0.8826 - AUC-PR: 0.9252 - P@50: 0.9200 > C0041909: upper gastrointestinal bleeding
AP: 0.8786 - AUC-ROC: 0.8786 - AUC-PR: 0.9183 - P@50: 0.9400 > C0085631: agitated
AP: 0.9695 - AUC-ROC: 0.9695 - AUC-PR: 0.9758 - P@50: 0.9800 > C0332687: Burns Second Degree
AP: 0.9788 - AUC-ROC: 0.9788 - AUC-PR: 0.9845 - P@50: 0.9800 > C1384606: dyspareunia
AP: 0.9327 - AUC-ROC: 0.9327 - AUC-PR: 0.9490 - P@50: 0.9800 > C0149745: mouth ulcer
AP: 0.9432 - AUC-ROC: 0.9432 - AUC-PR: 0.9611 - P@50: 0.9600 > C0040460: dental pain
AP: 0.9004 - AUC-ROC: 0.9004 - AUC-PR: 0.9338 - P@50: 0.8800 > C0006849: candidiasis of mouth
AP: 0.8991 - AUC-ROC: 0.8991 - AUC-PR: 0.9344 - P@50: 0.9400 > C0030305: pancreatitis
AP: 0.9710 - AUC-ROC: 0.9710 - AUC-PR: 0.9762 - P@50: 0.9800 > C0158328: trigger finger
AP: 0.8728 - AUC-ROC: 0.8728 - AUC-PR: 0.9226 - P@50: 0.8400 > C0005758: bleb
AP: 0.9183 - AUC-ROC: 0.9183 - AUC-PR: 0.9549 - P@50: 0.9400 > C0151970: esophageal ulcer
AP: 0.8797 - AUC-ROC: 0.8797 - AUC-PR: 0.9302 - P@50: 0.8800 > C0085605: Hepatic failure
AP: 0.8992 - AUC-ROC: 0.8992 - AUC-PR: 0.9296 - P@50: 0.9600 > C0022658: disorder Renal
AP: 0.8567 - AUC-ROC: 0.8567 - AUC-PR: 0.9128 - P@50: 0.8600 > C0013221: drug toxicity NOS
AP: 0.9541 - AUC-ROC: 0.9541 - AUC-PR: 0.9666 - P@50: 0.9600 > C0013390: dysmenorrhea
AP: 0.9363 - AUC-ROC: 0.9363 - AUC-PR: 0.9486 - P@50: 0.9400 > C0010034: corneal disorder
AP: 0.9305 - AUC-ROC: 0.9305 - AUC-PR: 0.9532 - P@50: 0.9400 > C0271650: Glucose intolerance
AP: 0.8894 - AUC-ROC: 0.8894 - AUC-PR: 0.9227 - P@50: 0.9400 > C0035410: rhabdomyolysis
AP: 0.9169 - AUC-ROC: 0.9169 - AUC-PR: 0.9594 - P@50: 0.9400 > C0006852: candidiasis of vagina
AP: 0.9680 - AUC-ROC: 0.9680 - AUC-PR: 0.9726 - P@50: 0.9600 > C0038131: dysphemia
AP: 0.9412 - AUC-ROC: 0.9412 - AUC-PR: 0.9610 - P@50: 0.9600 > C0149521: pancreatitis relapsing
AP: 0.9369 - AUC-ROC: 0.9369 - AUC-PR: 0.9581 - P@50: 0.9600 > C0006112: metabolic encephalopathy
AP: 0.9157 - AUC-ROC: 0.9157 - AUC-PR: 0.9444 - P@50: 0.9400 > C0023798: lipoma
AP: 0.8682 - AUC-ROC: 0.8682 - AUC-PR: 0.9229 - P@50: 0.8800 > C0027726: nephrotic syndrome
AP: 0.9658 - AUC-ROC: 0.9658 - AUC-PR: 0.9754 - P@50: 0.9600 > C0037287: Nodule Skin
AP: 0.9730 - AUC-ROC: 0.9730 - AUC-PR: 0.9780 - P@50: 0.9800 > C0024198: Lyme Disease
AP: 0.8743 - AUC-ROC: 0.8743 - AUC-PR: 0.9230 - P@50: 0.8800 > C0020538: High blood pressure
AP: 0.9216 - AUC-ROC: 0.9216 - AUC-PR: 0.9491 - P@50: 0.9200 > C0006266: bronchial spasm
AP: 0.8919 - AUC-ROC: 0.8919 - AUC-PR: 0.9255 - P@50: 0.9600 > C0034065: Embolism pulmonary
AP: 0.9234 - AUC-ROC: 0.9234 - AUC-PR: 0.9381 - P@50: 0.9400 > C0029400: bone inflammation
AP: 0.9083 - AUC-ROC: 0.9083 - AUC-PR: 0.9381 - P@50: 0.9400 > C0151699: haemorrhage intracranial
AP: 0.8977 - AUC-ROC: 0.8977 - AUC-PR: 0.9264 - P@50: 1.0000 > C0023530: leucopenia
AP: 0.9124 - AUC-ROC: 0.9124 - AUC-PR: 0.9485 - P@50: 0.9600 > C0235527: right heart failure
AP: 0.8834 - AUC-ROC: 0.8834 - AUC-PR: 0.9349 - P@50: 0.9000 > C0038220: status epilepticus
AP: 0.8933 - AUC-ROC: 0.8933 - AUC-PR: 0.9273 - P@50: 0.9400 > C0152027: sensory disturbance
AP: 0.9333 - AUC-ROC: 0.9333 - AUC-PR: 0.9379 - P@50: 0.9200 > C0221166: paraparesis
AP: 0.9256 - AUC-ROC: 0.9256 - AUC-PR: 0.9603 - P@50: 0.9600 > C0027343: ingrowing nail
AP: 0.9289 - AUC-ROC: 0.9289 - AUC-PR: 0.9460 - P@50: 0.9600 > C0004239: atrial flutter
AP: 0.9015 - AUC-ROC: 0.9015 - AUC-PR: 0.9360 - P@50: 0.9200 > C0520474: aseptic necrosis bone
AP: 0.8821 - AUC-ROC: 0.8821 - AUC-PR: 0.9259 - P@50: 0.9200 > C0040822: tremor
AP: 0.9476 - AUC-ROC: 0.9476 - AUC-PR: 0.9655 - P@50: 0.9600 > C0149516: chronic sinusitis
AP: 0.9285 - AUC-ROC: 0.9285 - AUC-PR: 0.9395 - P@50: 1.0000 > C0019193: hepatitis toxic
AP: 0.9150 - AUC-ROC: 0.9150 - AUC-PR: 0.9444 - P@50: 0.9200 > C0009376: colonic polyp
AP: 0.9664 - AUC-ROC: 0.9664 - AUC-PR: 0.9800 - P@50: 0.9600 > C0085166: bacterial vaginitis
AP: 0.9491 - AUC-ROC: 0.9491 - AUC-PR: 0.9610 - P@50: 0.9800 > C0917799: excessive sleepiness
AP: 0.8756 - AUC-ROC: 0.8756 - AUC-PR: 0.9316 - P@50: 0.8400 > C0026764: Multiple Myeloma
AP: 0.9330 - AUC-ROC: 0.9330 - AUC-PR: 0.9554 - P@50: 0.9400 > C1510472: Drug addiction
AP: 0.9407 - AUC-ROC: 0.9407 - AUC-PR: 0.9630 - P@50: 0.9400 > C0040128: thyroid disease
AP: 0.9037 - AUC-ROC: 0.9037 - AUC-PR: 0.9306 - P@50: 0.9400 > C0006625: cachectic
AP: 0.9802 - AUC-ROC: 0.9802 - AUC-PR: 0.9822 - P@50: 0.9800 > C0235660: galactorrhea
AP: 0.9287 - AUC-ROC: 0.9287 - AUC-PR: 0.9503 - P@50: 0.9400 > C0025290: Aseptic meningitis
AP: 0.9609 - AUC-ROC: 0.9609 - AUC-PR: 0.9670 - P@50: 0.9800 > C0014009: empyema
AP: 0.8591 - AUC-ROC: 0.8591 - AUC-PR: 0.9153 - P@50: 0.8200 > C0011991: diarrhea
AP: 0.9585 - AUC-ROC: 0.9585 - AUC-PR: 0.9695 - P@50: 1.0000 > C0002103: allergic rhinitis
AP: 0.9248 - AUC-ROC: 0.9248 - AUC-PR: 0.9615 - P@50: 0.9600 > C0042847: vitamin B 12 deficiency
AP: 0.8932 - AUC-ROC: 0.8932 - AUC-PR: 0.9410 - P@50: 0.9000 > C0015256: Excoriation
AP: 0.9457 - AUC-ROC: 0.9457 - AUC-PR: 0.9543 - P@50: 0.9400 > C0004095: asthenopia
AP: 0.9317 - AUC-ROC: 0.9317 - AUC-PR: 0.9512 - P@50: 0.9400 > C0024902: breast pain
AP: 0.8914 - AUC-ROC: 0.8914 - AUC-PR: 0.9498 - P@50: 0.9400 > C0024110: lung abscess
AP: 0.9012 - AUC-ROC: 0.9012 - AUC-PR: 0.9302 - P@50: 0.9400 > C0027441: nasopharyngitis
AP: 0.8712 - AUC-ROC: 0.8712 - AUC-PR: 0.9203 - P@50: 0.8000 > C0002871: anaemia
AP: 0.9050 - AUC-ROC: 0.9050 - AUC-PR: 0.9416 - P@50: 0.9400 > C0019158: hepatitis
AP: 0.9540 - AUC-ROC: 0.9540 - AUC-PR: 0.9648 - P@50: 0.9400 > C0001818: agoraphobia
AP: 0.9544 - AUC-ROC: 0.9544 - AUC-PR: 0.9576 - P@50: 0.9800 > C0042134: uterine bleeding
AP: 0.8988 - AUC-ROC: 0.8988 - AUC-PR: 0.9523 - P@50: 0.9200 > C0079102: Cerebral thrombosis
AP: 0.9969 - AUC-ROC: 0.9969 - AUC-PR: 0.9968 - P@50: 0.9600 > C0007078: carbuncle
AP: 0.9473 - AUC-ROC: 0.9473 - AUC-PR: 0.9656 - P@50: 0.9600 > C0011884: Diabetic Retinopathy
AP: 0.9678 - AUC-ROC: 0.9678 - AUC-PR: 0.9791 - P@50: 0.9800 > C0042133: fibroids
AP: 0.8701 - AUC-ROC: 0.8701 - AUC-PR: 0.9225 - P@50: 0.8600 > C0011206: acute brain syndrome
AP: 0.9040 - AUC-ROC: 0.9040 - AUC-PR: 0.9409 - P@50: 0.9400 > C0699790: carcinoma of the colon
AP: 0.9183 - AUC-ROC: 0.9183 - AUC-PR: 0.9486 - P@50: 0.9200 > C0014038: encephalitis
AP: 0.9407 - AUC-ROC: 0.9407 - AUC-PR: 0.9662 - P@50: 0.9600 > C0010414: cryptococcosis
AP: 0.9721 - AUC-ROC: 0.9721 - AUC-PR: 0.9756 - P@50: 0.9600 > C1621958: glioblastoma multiforme
AP: 0.9906 - AUC-ROC: 0.9906 - AUC-PR: 0.9903 - P@50: 1.0000 > C0190211: coronary angioplasty
AP: 0.9536 - AUC-ROC: 0.9536 - AUC-PR: 0.9678 - P@50: 0.9600 > C0036396: ischias
AP: 0.8935 - AUC-ROC: 0.8935 - AUC-PR: 0.9352 - P@50: 0.9200 > C0264906: atrioventricular block second degree
AP: 0.9024 - AUC-ROC: 0.9024 - AUC-PR: 0.9345 - P@50: 0.9200 > C0038362: mucositis oral
AP: 0.9403 - AUC-ROC: 0.9403 - AUC-PR: 0.9556 - P@50: 0.9600 > C0002736: als
AP: 0.9825 - AUC-ROC: 0.9825 - AUC-PR: 0.9831 - P@50: 1.0000 > C0085655: polymyositis
AP: 0.9865 - AUC-ROC: 0.9865 - AUC-PR: 0.9869 - P@50: 0.9600 > C0019572: hirsuitism
AP: 0.9500 - AUC-ROC: 0.9500 - AUC-PR: 0.9608 - P@50: 0.9800 > C0085635: flashing lights
AP: 0.9150 - AUC-ROC: 0.9150 - AUC-PR: 0.9446 - P@50: 0.9600 > C0042510: ventricular fibrillation
AP: 0.9444 - AUC-ROC: 0.9444 - AUC-PR: 0.9585 - P@50: 0.9400 > C0152013: lung adenocarcinoma
AP: 0.9598 - AUC-ROC: 0.9598 - AUC-PR: 0.9699 - P@50: 0.9800 > C0023067: laryngitis
AP: 0.9099 - AUC-ROC: 0.9099 - AUC-PR: 0.9373 - P@50: 0.9600 > C0009763: conjunctivitis
AP: 0.8748 - AUC-ROC: 0.8748 - AUC-PR: 0.9236 - P@50: 0.8800 > C0003811: Arrhythmia
AP: 0.9294 - AUC-ROC: 0.9294 - AUC-PR: 0.9530 - P@50: 0.9600 > C0006277: bronchitis
AP: 0.9179 - AUC-ROC: 0.9179 - AUC-PR: 0.9466 - P@50: 0.9600 > C0011603: dermatitides
AP: 0.8588 - AUC-ROC: 0.8588 - AUC-PR: 0.9126 - P@50: 0.8400 > C0041657: loss of consciousness
AP: 0.9367 - AUC-ROC: 0.9367 - AUC-PR: 0.9608 - P@50: 0.9400 > C0030486: paraplegia
AP: 0.9138 - AUC-ROC: 0.9138 - AUC-PR: 0.9454 - P@50: 0.9200 > C0011334: dental caries
AP: 0.8798 - AUC-ROC: 0.8798 - AUC-PR: 0.9266 - P@50: 0.8800 > C0242429: pain in throat
AP: 0.9710 - AUC-ROC: 0.9710 - AUC-PR: 0.9717 - P@50: 0.9800 > C0022575: keratitis sicca
AP: 0.9458 - AUC-ROC: 0.9458 - AUC-PR: 0.9539 - P@50: 1.0000 > C0009917: contracture
AP: 0.9314 - AUC-ROC: 0.9314 - AUC-PR: 0.9504 - P@50: 0.9600 > C0220983: metabolic alkalosis
AP: 0.9625 - AUC-ROC: 0.9625 - AUC-PR: 0.9721 - P@50: 0.9600 > C0032533: polymyalgia rheumatica
AP: 0.8862 - AUC-ROC: 0.8862 - AUC-PR: 0.9297 - P@50: 0.9200 > C0085649: edema extremities
AP: 0.9200 - AUC-ROC: 0.9200 - AUC-PR: 0.9484 - P@50: 0.9400 > C0151827: eye pain
AP: 0.9076 - AUC-ROC: 0.9076 - AUC-PR: 0.9398 - P@50: 0.9200 > C0033845: benign intracranial hypertension
AP: 0.9738 - AUC-ROC: 0.9738 - AUC-PR: 0.9794 - P@50: 1.0000 > C0149756: fascitis plantar
AP: 0.9580 - AUC-ROC: 0.9580 - AUC-PR: 0.9656 - P@50: 0.9600 > C0019655: histoplasmosis
AP: 0.9718 - AUC-ROC: 0.9718 - AUC-PR: 0.9767 - P@50: 0.9800 > C0036337: schizoaffective disorder
AP: 0.8882 - AUC-ROC: 0.8882 - AUC-PR: 0.9261 - P@50: 0.9600 > C0020458: hyperhidrosis
AP: 0.9583 - AUC-ROC: 0.9583 - AUC-PR: 0.9650 - P@50: 0.9800 > C0027813: Neuritis
AP: 0.9823 - AUC-ROC: 0.9823 - AUC-PR: 0.9842 - P@50: 1.0000 > C0039504: tendon injury
AP: 0.9181 - AUC-ROC: 0.9181 - AUC-PR: 0.9487 - P@50: 0.9400 > C0024437: macula lutea degeneration
AP: 0.9142 - AUC-ROC: 0.9142 - AUC-PR: 0.9571 - P@50: 0.9200 > C0031212: Personality disorder
AP: 0.8945 - AUC-ROC: 0.8945 - AUC-PR: 0.9336 - P@50: 0.9200 > C0085615: bundle branch block right
AP: 0.8804 - AUC-ROC: 0.8804 - AUC-PR: 0.9248 - P@50: 0.9400 > C0442874: neuropathy
AP: 0.9318 - AUC-ROC: 0.9318 - AUC-PR: 0.9499 - P@50: 0.9600 > C0011860: Mod
AP: 0.9279 - AUC-ROC: 0.9279 - AUC-PR: 0.9422 - P@50: 0.9800 > C0151611: abnormal EEG
AP: 0.9405 - AUC-ROC: 0.9405 - AUC-PR: 0.9605 - P@50: 0.9400 > C0521620: hydroureter
AP: 0.9463 - AUC-ROC: 0.9463 - AUC-PR: 0.9523 - P@50: 0.9000 > C0037995: splenectomy
AP: 0.9059 - AUC-ROC: 0.9059 - AUC-PR: 0.9387 - P@50: 0.9200 > C0080179: Spinal fracture
AP: 0.9276 - AUC-ROC: 0.9276 - AUC-PR: 0.9576 - P@50: 0.9600 > C0026896: myasthenia gravis
AP: 0.8986 - AUC-ROC: 0.8986 - AUC-PR: 0.9328 - P@50: 0.9400 > C0220981: metabolic acidosis
AP: 0.9410 - AUC-ROC: 0.9410 - AUC-PR: 0.9483 - P@50: 0.9800 > C0003874: Arthritis bacterial
AP: 0.9633 - AUC-ROC: 0.9633 - AUC-PR: 0.9707 - P@50: 0.9400 > C0267566: perirectal abscess
AP: 0.9770 - AUC-ROC: 0.9770 - AUC-PR: 0.9753 - P@50: 1.0000 > C0206504: tympanic membrane perforation
AP: 0.9087 - AUC-ROC: 0.9087 - AUC-PR: 0.9457 - P@50: 0.9200 > C0149514: acute bronchitis
AP: 0.9231 - AUC-ROC: 0.9231 - AUC-PR: 0.9597 - P@50: 0.9200 > C0008320: cholecystectomies
AP: 0.9051 - AUC-ROC: 0.9051 - AUC-PR: 0.9459 - P@50: 0.9200 > C0007177: Cardiac tamponade
AP: 0.9059 - AUC-ROC: 0.9059 - AUC-PR: 0.9419 - P@50: 0.8600 > C0031117: neuropathy peripheral
AP: 0.9268 - AUC-ROC: 0.9268 - AUC-PR: 0.9512 - P@50: 0.9400 > C0017574: gingivitis
AP: 0.9887 - AUC-ROC: 0.9887 - AUC-PR: 0.9898 - P@50: 1.0000 > C0006145: Breast disorder
AP: 0.8780 - AUC-ROC: 0.8780 - AUC-PR: 0.9320 - P@50: 0.8600 > C0235896: lung infiltration
AP: 0.8669 - AUC-ROC: 0.8669 - AUC-PR: 0.9209 - P@50: 0.8200 > C0042963: emesis
AP: 0.9377 - AUC-ROC: 0.9377 - AUC-PR: 0.9615 - P@50: 0.9400 > C0000833: abscess
AP: 0.9308 - AUC-ROC: 0.9308 - AUC-PR: 0.9381 - P@50: 0.8800 > C0282005: swollen scrotum
AP: 0.9321 - AUC-ROC: 0.9321 - AUC-PR: 0.9554 - P@50: 0.9800 > C0242528: azotaemia
AP: 0.8734 - AUC-ROC: 0.8734 - AUC-PR: 0.9277 - P@50: 0.8600 > C0001339: acute pancreatitis
AP: 0.9547 - AUC-ROC: 0.9547 - AUC-PR: 0.9729 - P@50: 0.9400 > C0038436: post traumatic stress disorder
AP: 0.9606 - AUC-ROC: 0.9606 - AUC-PR: 0.9735 - P@50: 0.9800 > C0019322: umbilical hernia
AP: 0.9470 - AUC-ROC: 0.9470 - AUC-PR: 0.9595 - P@50: 0.9200 > C0006152: Breast swelling
AP: 0.8883 - AUC-ROC: 0.8883 - AUC-PR: 0.9290 - P@50: 0.8400 > C0037763: muscle spasm
AP: 0.9410 - AUC-ROC: 0.9410 - AUC-PR: 0.9601 - P@50: 0.9600 > C0016663: Bone Fracture Spontaneous
AP: 0.9156 - AUC-ROC: 0.9156 - AUC-PR: 0.9463 - P@50: 0.9200 > C0020440: Hypercapnia
AP: 0.8644 - AUC-ROC: 0.8644 - AUC-PR: 0.9132 - P@50: 0.8800 > C0027719: nephrosclerosis
AP: 0.9389 - AUC-ROC: 0.9389 - AUC-PR: 0.9617 - P@50: 0.9400 > C0149778: soft tissue infection
AP: 0.8664 - AUC-ROC: 0.8664 - AUC-PR: 0.9212 - P@50: 0.8200 > C0019079: coughing blood
AP: 0.9354 - AUC-ROC: 0.9354 - AUC-PR: 0.9521 - P@50: 0.9800 > C0158986: hypoglycaemia neonatal
AP: 0.9186 - AUC-ROC: 0.9186 - AUC-PR: 0.9446 - P@50: 0.9400 > C0032231: pleurisy
AP: 0.9092 - AUC-ROC: 0.9092 - AUC-PR: 0.9449 - P@50: 0.9200 > C0026848: muscle disorder
AP: 0.9206 - AUC-ROC: 0.9206 - AUC-PR: 0.9543 - P@50: 0.9400 > C0032310: viral pneumonia
AP: 0.9035 - AUC-ROC: 0.9035 - AUC-PR: 0.9340 - P@50: 0.9200 > C0011606: dermatitis exfoliative
AP: 0.9381 - AUC-ROC: 0.9381 - AUC-PR: 0.9619 - P@50: 0.9400 > C0024103: Breast Lump
AP: 0.9147 - AUC-ROC: 0.9147 - AUC-PR: 0.9425 - P@50: 0.9400 > C0038395: streptococcal infection
AP: 0.9324 - AUC-ROC: 0.9324 - AUC-PR: 0.9525 - P@50: 0.9600 > C0010709: cyst
AP: 0.9115 - AUC-ROC: 0.9115 - AUC-PR: 0.9470 - P@50: 0.9000 > C0085624: burning sensation
AP: 0.8889 - AUC-ROC: 0.8889 - AUC-PR: 0.9236 - P@50: 0.9400 > C0042514: tachycardia ventricular
AP: 0.8829 - AUC-ROC: 0.8829 - AUC-PR: 0.9241 - P@50: 0.8600 > C0018784: Deafness neurosensory
AP: 0.9353 - AUC-ROC: 0.9353 - AUC-PR: 0.9474 - P@50: 1.0000 > C0023467: Acute myeloblastic leukemia
AP: 0.9608 - AUC-ROC: 0.9608 - AUC-PR: 0.9700 - P@50: 0.9800 > C0022603: seborrhoeic keratosis
AP: 0.9326 - AUC-ROC: 0.9326 - AUC-PR: 0.9490 - P@50: 0.9400 > C0005697: neurogenic bladder
AP: 0.8966 - AUC-ROC: 0.8966 - AUC-PR: 0.9291 - P@50: 0.8800 > C0740394: hyperuricaemia
AP: 0.9231 - AUC-ROC: 0.9231 - AUC-PR: 0.9445 - P@50: 0.9400 > C0038363: aphthous stomatitis
AP: 0.9701 - AUC-ROC: 0.9701 - AUC-PR: 0.9758 - P@50: 0.9400 > C0029936: oophorectomy
AP: 0.9480 - AUC-ROC: 0.9480 - AUC-PR: 0.9596 - P@50: 0.9600 > C0039103: synovitis
AP: 0.8823 - AUC-ROC: 0.8823 - AUC-PR: 0.9242 - P@50: 0.9000 > C0030552: muscle paresis
AP: 0.9064 - AUC-ROC: 0.9064 - AUC-PR: 0.9467 - P@50: 0.9200 > C0042961: volvulus
AP: 0.9756 - AUC-ROC: 0.9756 - AUC-PR: 0.9802 - P@50: 0.9600 > C1510471: hypovitaminosis
AP: 0.9551 - AUC-ROC: 0.9551 - AUC-PR: 0.9622 - P@50: 0.9600 > C0002390: allergic alveolitis
AP: 0.8788 - AUC-ROC: 0.8788 - AUC-PR: 0.9335 - P@50: 0.8200 > C0004623: Bacterial infection
AP: 0.8835 - AUC-ROC: 0.8835 - AUC-PR: 0.9354 - P@50: 0.8200 > C0027404: narcolepsy
AP: 0.8869 - AUC-ROC: 0.8869 - AUC-PR: 0.9290 - P@50: 0.9200 > C0020295: hydronephrosis
AP: 0.9053 - AUC-ROC: 0.9053 - AUC-PR: 0.9348 - P@50: 0.9400 > C0014549: Convulsions Grand Mal
AP: 0.9377 - AUC-ROC: 0.9377 - AUC-PR: 0.9499 - P@50: 0.9800 > C0266813: fecal occult blood
AP: 0.9115 - AUC-ROC: 0.9115 - AUC-PR: 0.9375 - P@50: 0.9400 > C0001623: adrenal insufficiency
AP: 0.8943 - AUC-ROC: 0.8943 - AUC-PR: 0.9361 - P@50: 0.9000 > C0003126: anosmia
AP: 0.8996 - AUC-ROC: 0.8996 - AUC-PR: 0.9426 - P@50: 0.9000 > C0041582: ulcer
AP: 0.9239 - AUC-ROC: 0.9239 - AUC-PR: 0.9538 - P@50: 0.9400 > C0017979: glucosuria
AP: 0.9984 - AUC-ROC: 0.9984 - AUC-PR: 0.9983 - P@50: 1.0000 > C0026780: Mumps
AP: 0.9640 - AUC-ROC: 0.9640 - AUC-PR: 0.9659 - P@50: 1.0000 > C0034735: Raynauds phenomenon
AP: 0.8782 - AUC-ROC: 0.8782 - AUC-PR: 0.9256 - P@50: 0.8600 > C0027497: nausea
AP: 0.8903 - AUC-ROC: 0.8903 - AUC-PR: 0.9262 - P@50: 0.9000 > C0497327: amentia
AP: 0.9516 - AUC-ROC: 0.9516 - AUC-PR: 0.9514 - P@50: 0.9200 > C0018924: haemarthrosis
AP: 0.9347 - AUC-ROC: 0.9347 - AUC-PR: 0.9542 - P@50: 0.9600 > C0005745: blepharoptosis
AP: 0.8808 - AUC-ROC: 0.8808 - AUC-PR: 0.9312 - P@50: 0.8400 > C0038454: apoplexy
AP: 0.9108 - AUC-ROC: 0.9108 - AUC-PR: 0.9491 - P@50: 0.9200 > C0013405: Dyspnoea paroxysmal nocturnal
AP: 0.9437 - AUC-ROC: 0.9437 - AUC-PR: 0.9613 - P@50: 0.9600 > C0870082: hyperkeratosis
AP: 0.9307 - AUC-ROC: 0.9307 - AUC-PR: 0.9455 - P@50: 0.9600 > C0003869: Arthritis infective
AP: 0.8979 - AUC-ROC: 0.8979 - AUC-PR: 0.9406 - P@50: 0.8000 > C0030554: Paraesthesia
AP: 0.8772 - AUC-ROC: 0.8772 - AUC-PR: 0.9285 - P@50: 0.8000 > C0020649: arterial pressure NOS decreased
AP: 0.9640 - AUC-ROC: 0.9640 - AUC-PR: 0.9700 - P@50: 1.0000 > C0151480: antinuclear antibody positive
AP: 0.9125 - AUC-ROC: 0.9125 - AUC-PR: 0.9486 - P@50: 0.9600 > C0010043: corneal ulcer
AP: 0.8864 - AUC-ROC: 0.8864 - AUC-PR: 0.9274 - P@50: 0.8600 > C0027051: heart attack
AP: 0.9368 - AUC-ROC: 0.9368 - AUC-PR: 0.9646 - P@50: 0.9800 > C0014733: erysipelas
AP: 0.9211 - AUC-ROC: 0.9211 - AUC-PR: 0.9410 - P@50: 0.9600 > C0024299: lymphoma
AP: 0.9369 - AUC-ROC: 0.9369 - AUC-PR: 0.9599 - P@50: 0.9600 > C0549567: pigmentation disorder
AP: 0.9543 - AUC-ROC: 0.9543 - AUC-PR: 0.9616 - P@50: 0.9200 > C0020490: hypermetropia
AP: 0.9172 - AUC-ROC: 0.9172 - AUC-PR: 0.9464 - P@50: 0.9800 > C0013295: duodenal ulcer
AP: 0.8775 - AUC-ROC: 0.8775 - AUC-PR: 0.9246 - P@50: 0.8800 > C0041834: erythema
AP: 0.8828 - AUC-ROC: 0.8828 - AUC-PR: 0.9278 - P@50: 0.8600 > C0000731: abdominal distension
AP: 0.9237 - AUC-ROC: 0.9237 - AUC-PR: 0.9340 - P@50: 0.9800 > C1257843: colitis pseudomembranous
AP: 0.9026 - AUC-ROC: 0.9026 - AUC-PR: 0.9398 - P@50: 0.9200 > C0026769: multiple sclerosis
AP: 0.9509 - AUC-ROC: 0.9509 - AUC-PR: 0.9630 - P@50: 0.9600 > C0699885: bladder cancer
AP: 0.9615 - AUC-ROC: 0.9615 - AUC-PR: 0.9742 - P@50: 0.9600 > C0030583: parotitis
AP: 0.8633 - AUC-ROC: 0.8633 - AUC-PR: 0.9239 - P@50: 0.9000 > C0023524: multifocal leukoencephalopathy
AP: 0.9652 - AUC-ROC: 0.9652 - AUC-PR: 0.9734 - P@50: 1.0000 > C1442903: bone spur
AP: 0.8654 - AUC-ROC: 0.8654 - AUC-PR: 0.9207 - P@50: 0.7800 > C0039070: Fainting
AP: 0.9455 - AUC-ROC: 0.9455 - AUC-PR: 0.9594 - P@50: 0.9600 > C0020453: hyperaesthesia
AP: 0.9414 - AUC-ROC: 0.9414 - AUC-PR: 0.9530 - P@50: 1.0000 > C0007820: cerebral vascular disorder
AP: 0.9938 - AUC-ROC: 0.9938 - AUC-PR: 0.9928 - P@50: 1.0000 > C0009088: cluster headache
AP: 0.9754 - AUC-ROC: 0.9754 - AUC-PR: 0.9773 - P@50: 0.9400 > C0040456: Tooth Impacted
AP: 0.9414 - AUC-ROC: 0.9414 - AUC-PR: 0.9691 - P@50: 0.9800 > C0220982: ketoacidosis
AP: 0.9485 - AUC-ROC: 0.9485 - AUC-PR: 0.9652 - P@50: 0.9600 > C0015544: failure to thrive
AP: 0.9025 - AUC-ROC: 0.9025 - AUC-PR: 0.9486 - P@50: 0.8800 > C0267112: erosive gastritis
AP: 0.9171 - AUC-ROC: 0.9171 - AUC-PR: 0.9454 - P@50: 0.9600 > C0023211: bundle branch block left
AP: 0.9734 - AUC-ROC: 0.9734 - AUC-PR: 0.9787 - P@50: 0.9600 > C0033246: proctitis
AP: 0.9180 - AUC-ROC: 0.9180 - AUC-PR: 0.9470 - P@50: 0.9200 > C0221776: mouth pain
AP: 0.8868 - AUC-ROC: 0.8868 - AUC-PR: 0.9296 - P@50: 0.8800 > C0011175: dehydration
AP: 0.8829 - AUC-ROC: 0.8829 - AUC-PR: 0.9300 - P@50: 0.8200 > C0015672: Fatigue
AP: 0.9335 - AUC-ROC: 0.9335 - AUC-PR: 0.9548 - P@50: 0.9400 > C0152128: drug withdrawal
AP: 0.9889 - AUC-ROC: 0.9889 - AUC-PR: 0.9898 - P@50: 1.0000 > C0032776: postmenopausal bleeding
AP: 0.9755 - AUC-ROC: 0.9755 - AUC-PR: 0.9769 - P@50: 0.9800 > C0281774: acute psychosis
AP: 0.8888 - AUC-ROC: 0.8888 - AUC-PR: 0.9247 - P@50: 0.9400 > C0014544: epilepsy
AP: 0.9459 - AUC-ROC: 0.9459 - AUC-PR: 0.9574 - P@50: 0.9200 > C0024282: lymphocytosis
AP: 0.9460 - AUC-ROC: 0.9460 - AUC-PR: 0.9611 - P@50: 0.9400 > C0002874: Anemia aplastic
AP: 0.9192 - AUC-ROC: 0.9192 - AUC-PR: 0.9462 - P@50: 0.9400 > C0031154: peritonitis
AP: 0.9380 - AUC-ROC: 0.9380 - AUC-PR: 0.9628 - P@50: 0.9600 > C0001948: alcohol consumption
AP: 0.8500 - AUC-ROC: 0.8500 - AUC-PR: 0.9108 - P@50: 0.8000 > C0231218: Feeling unwell
AP: 0.9070 - AUC-ROC: 0.9070 - AUC-PR: 0.9407 - P@50: 0.9200 > C0038814: sunburn
AP: 0.8890 - AUC-ROC: 0.8890 - AUC-PR: 0.9281 - P@50: 0.9000 > C0024586: carcinoid syndrome
AP: 0.8669 - AUC-ROC: 0.8669 - AUC-PR: 0.9126 - P@50: 0.9000 > C0020615: hypoglycaemia
AP: 0.9440 - AUC-ROC: 0.9440 - AUC-PR: 0.9626 - P@50: 0.9800 > C0263912: rotator cuff syndrome
AP: 0.9480 - AUC-ROC: 0.9480 - AUC-PR: 0.9658 - P@50: 0.9600 > C0016053: fibromyalgia
AP: 0.9583 - AUC-ROC: 0.9583 - AUC-PR: 0.9581 - P@50: 0.9600 > C0034888: rectal prolapse
AP: 0.8746 - AUC-ROC: 0.8746 - AUC-PR: 0.9213 - P@50: 0.8200 > C0017181: gastrointestinal bleed
AP: 0.9570 - AUC-ROC: 0.9570 - AUC-PR: 0.9683 - P@50: 0.9600 > C0155773: portal vein thrombosis
AP: 0.8959 - AUC-ROC: 0.8959 - AUC-PR: 0.9304 - P@50: 0.9400 > C0085584: encephalopathy
AP: 0.8638 - AUC-ROC: 0.8638 - AUC-PR: 0.9177 - P@50: 0.8600 > C0018801: cardiac failure
AP: 0.9620 - AUC-ROC: 0.9620 - AUC-PR: 0.9695 - P@50: 0.9800 > C0042928: vocal cord paralysis
AP: 0.9299 - AUC-ROC: 0.9299 - AUC-PR: 0.9399 - P@50: 0.9200 > C0026975: myelitis
AP: 0.9600 - AUC-ROC: 0.9600 - AUC-PR: 0.9749 - P@50: 0.9800 > C0003615: appendicitis
AP: 0.9437 - AUC-ROC: 0.9437 - AUC-PR: 0.9632 - P@50: 0.9400 > C0023903: hepatic neoplasia
AP: 0.9047 - AUC-ROC: 0.9047 - AUC-PR: 0.9368 - P@50: 0.9000 > C0003862: Aching joints
AP: 0.9771 - AUC-ROC: 0.9771 - AUC-PR: 0.9764 - P@50: 0.9600 > C0026948: mycosis fungoides
AP: 0.8832 - AUC-ROC: 0.8832 - AUC-PR: 0.9374 - P@50: 0.7800 > C0012813: diverticulitis
AP: 0.9266 - AUC-ROC: 0.9266 - AUC-PR: 0.9519 - P@50: 0.9200 > C0007859: cervicalgia
AP: 0.8927 - AUC-ROC: 0.8927 - AUC-PR: 0.9344 - P@50: 0.9400 > C0227791: vaginal discharge
AP: 0.8967 - AUC-ROC: 0.8967 - AUC-PR: 0.9325 - P@50: 0.9000 > C0030252: palpitation
AP: 0.8918 - AUC-ROC: 0.8918 - AUC-PR: 0.9325 - P@50: 0.9200 > C0009421: coma
AP: 0.9867 - AUC-ROC: 0.9867 - AUC-PR: 0.9868 - P@50: 0.9600 > C0149741: breast discharge
AP: 0.9227 - AUC-ROC: 0.9227 - AUC-PR: 0.9478 - P@50: 0.9200 > C0038663: attempted suicide
AP: 0.8926 - AUC-ROC: 0.8926 - AUC-PR: 0.9392 - P@50: 0.9200 > C0013922: embolism
AP: 0.9019 - AUC-ROC: 0.9019 - AUC-PR: 0.9479 - P@50: 0.9200 > C0023885: liver abscess
AP: 0.8646 - AUC-ROC: 0.8646 - AUC-PR: 0.9253 - P@50: 0.7200 > C0010200: Cough
AP: 0.8779 - AUC-ROC: 0.8779 - AUC-PR: 0.9246 - P@50: 0.8800 > C0031046: pericarditis
AP: 0.8723 - AUC-ROC: 0.8723 - AUC-PR: 0.9128 - P@50: 0.9000 > C0042798: Abnormal vision
AP: 0.9075 - AUC-ROC: 0.9075 - AUC-PR: 0.9464 - P@50: 0.9400 > C0162529: colitis ischemic
AP: 0.9823 - AUC-ROC: 0.9823 - AUC-PR: 0.9880 - P@50: 0.9800 > C0018500: hair disease
AP: 0.9303 - AUC-ROC: 0.9303 - AUC-PR: 0.9465 - P@50: 0.9200 > C0014534: epididymitis
AP: 0.9693 - AUC-ROC: 0.9693 - AUC-PR: 0.9732 - P@50: 1.0000 > C0152032: hesitancy
AP: 0.8827 - AUC-ROC: 0.8827 - AUC-PR: 0.9479 - P@50: 0.9200 > C0003044: animal bite
AP: 0.8543 - AUC-ROC: 0.8543 - AUC-PR: 0.9090 - P@50: 0.8600 > C0002878: haemolytic anaemia
AP: 0.9517 - AUC-ROC: 0.9517 - AUC-PR: 0.9570 - P@50: 0.9600 > C0027822: neurodermatitis
AP: 0.8834 - AUC-ROC: 0.8834 - AUC-PR: 0.9351 - P@50: 0.8800 > C0018817: atrial septal defect
AP: 0.9515 - AUC-ROC: 0.9515 - AUC-PR: 0.9638 - P@50: 0.9600 > C0149531: fractured pelvis NOS
AP: 0.9772 - AUC-ROC: 0.9772 - AUC-PR: 0.9810 - P@50: 0.9800 > C0270629: epidural abscess
AP: 0.9113 - AUC-ROC: 0.9113 - AUC-PR: 0.9306 - P@50: 0.9400 > C0011609: dermatitis medicamentosa
AP: 0.9711 - AUC-ROC: 0.9711 - AUC-PR: 0.9809 - P@50: 0.9800 > C0033953: psychosexual disorder
AP: 0.9117 - AUC-ROC: 0.9117 - AUC-PR: 0.9440 - P@50: 0.9400 > C0041755: ADVERSE DRUG EFFECT
AP: 0.9824 - AUC-ROC: 0.9824 - AUC-PR: 0.9846 - P@50: 0.9800 > C0019284: diaphragmatic hernia
AP: 0.9249 - AUC-ROC: 0.9249 - AUC-PR: 0.9499 - P@50: 0.9400 > C0149931: migraine
AP: 0.9772 - AUC-ROC: 0.9772 - AUC-PR: 0.9751 - P@50: 0.9800 > C0042907: vitreous detachment
AP: 0.8945 - AUC-ROC: 0.8945 - AUC-PR: 0.9350 - P@50: 0.9200 > C0019291: hernia hiatal
AP: 0.8910 - AUC-ROC: 0.8910 - AUC-PR: 0.9304 - P@50: 0.8800 > C0032285: neumonia
AP: 0.9568 - AUC-ROC: 0.9568 - AUC-PR: 0.9685 - P@50: 0.9600 > C0008035: Chest wall pain
AP: 0.8698 - AUC-ROC: 0.8698 - AUC-PR: 0.9250 - P@50: 0.8400 > C0575090: balance disorder
AP: 0.9308 - AUC-ROC: 0.9308 - AUC-PR: 0.9511 - P@50: 0.9800 > C0242362: Intervertebral Disc Herniation
AP: 0.8792 - AUC-ROC: 0.8792 - AUC-PR: 0.9276 - P@50: 0.8800 > C0042024: Incontinence
AP: 0.8550 - AUC-ROC: 0.8550 - AUC-PR: 0.9127 - P@50: 0.7800 > C0151904: Aspartate Aminotransferase Increase
AP: 0.9221 - AUC-ROC: 0.9221 - AUC-PR: 0.9548 - P@50: 0.9400 > C0085606: micturition urgency
AP: 0.9360 - AUC-ROC: 0.9360 - AUC-PR: 0.9560 - P@50: 0.9400 > C0039483: temporal arteritis
AP: 0.8814 - AUC-ROC: 0.8814 - AUC-PR: 0.9257 - P@50: 0.9200 > C0020456: hyperglycaemia
AP: 0.8704 - AUC-ROC: 0.8704 - AUC-PR: 0.9224 - P@50: 0.8400 > C0021311: infection
AP: 0.9521 - AUC-ROC: 0.9521 - AUC-PR: 0.9582 - P@50: 1.0000 > C0008311: Cholangitis
AP: 0.9664 - AUC-ROC: 0.9664 - AUC-PR: 0.9708 - P@50: 0.9600 > C0036508: dermatitis seborrheic
AP: 0.8962 - AUC-ROC: 0.8962 - AUC-PR: 0.9362 - P@50: 0.9200 > C0011849: Diabetes
AP: 0.9015 - AUC-ROC: 0.9015 - AUC-PR: 0.9383 - P@50: 0.9400 > C0037199: Sinusitis
AP: 0.9409 - AUC-ROC: 0.9409 - AUC-PR: 0.9568 - P@50: 0.9400 > C0519030: pneumonia Klebsiella
AP: 0.9300 - AUC-ROC: 0.9300 - AUC-PR: 0.9567 - P@50: 0.9400 > C0259768: wound dehiscence
AP: 0.8830 - AUC-ROC: 0.8830 - AUC-PR: 0.9334 - P@50: 0.9000 > C0029925: Ovarian cancer
AP: 0.9048 - AUC-ROC: 0.9048 - AUC-PR: 0.9378 - P@50: 0.8800 > C0030196: Extremity pain
AP: 0.9185 - AUC-ROC: 0.9185 - AUC-PR: 0.9486 - P@50: 0.9200 > C0008301: choking
AP: 0.9541 - AUC-ROC: 0.9541 - AUC-PR: 0.9678 - P@50: 0.9600 > C0025297: Meningitis Viral
AP: 0.9294 - AUC-ROC: 0.9294 - AUC-PR: 0.9650 - P@50: 0.9600 > C0036439: Scoliosis
AP: 0.9307 - AUC-ROC: 0.9307 - AUC-PR: 0.9525 - P@50: 0.9400 > C0005741: blepharitis
AP: 0.9086 - AUC-ROC: 0.9086 - AUC-PR: 0.9393 - P@50: 0.9400 > C0037284: skin lesion
AP: 0.9776 - AUC-ROC: 0.9776 - AUC-PR: 0.9828 - P@50: 0.9800 > C0033893: tension headache
AP: 0.9575 - AUC-ROC: 0.9575 - AUC-PR: 0.9643 - P@50: 0.9800 > C0013274: patent ductus arteriosis
AP: 0.9209 - AUC-ROC: 0.9209 - AUC-PR: 0.9531 - P@50: 0.9400 > C0014869: reflux esophagitis
AP: 0.9467 - AUC-ROC: 0.9467 - AUC-PR: 0.9696 - P@50: 0.9800 > C0002940: aneurysm
AP: 0.8731 - AUC-ROC: 0.8731 - AUC-PR: 0.9294 - P@50: 0.7800 > C0392525: Nephrolithiasis
AP: 0.9127 - AUC-ROC: 0.9127 - AUC-PR: 0.9381 - P@50: 0.9200 > C0042345: varicose vein
AP: 0.9671 - AUC-ROC: 0.9671 - AUC-PR: 0.9740 - P@50: 0.9200 > C1261473: sarcoma
AP: 0.9486 - AUC-ROC: 0.9486 - AUC-PR: 0.9564 - P@50: 0.9800 > C0740401: duodenal ulcer perforation
AP: 0.9381 - AUC-ROC: 0.9381 - AUC-PR: 0.9614 - P@50: 0.9400 > C0025061: mediastinal disorder
AP: 0.9563 - AUC-ROC: 0.9563 - AUC-PR: 0.9587 - P@50: 0.9800 > C0022568: keratitis
AP: 0.9241 - AUC-ROC: 0.9241 - AUC-PR: 0.9523 - P@50: 0.9200 > C0034186: pyelonephritis
AP: 0.9161 - AUC-ROC: 0.9161 - AUC-PR: 0.9525 - P@50: 0.9000 > C0318712: gastroenteritis viral
AP: 0.8944 - AUC-ROC: 0.8944 - AUC-PR: 0.9319 - P@50: 0.9200 > C0024115: Disorder Lung
AP: 0.8866 - AUC-ROC: 0.8866 - AUC-PR: 0.9233 - P@50: 0.9200 > C0027947: Neutropenia
AP: 0.9346 - AUC-ROC: 0.9346 - AUC-PR: 0.9562 - P@50: 0.9800 > C0018188: granuloma
AP: 0.9279 - AUC-ROC: 0.9279 - AUC-PR: 0.9571 - P@50: 0.9200 > C0013456: ear ache
AP: 0.9055 - AUC-ROC: 0.9055 - AUC-PR: 0.9412 - P@50: 0.9000 > C0001969: Alcoholic intoxication
AP: 0.9211 - AUC-ROC: 0.9211 - AUC-PR: 0.9452 - P@50: 0.9600 > C0149801: urosepsis
AP: 0.9463 - AUC-ROC: 0.9463 - AUC-PR: 0.9597 - P@50: 0.9800 > C0036341: schizophrenia
AP: 0.8737 - AUC-ROC: 0.8737 - AUC-PR: 0.9167 - P@50: 0.8800 > C0036974: cardiovascular collapse
AP: 0.9094 - AUC-ROC: 0.9094 - AUC-PR: 0.9446 - P@50: 0.9200 > C0700200: Near Syncope
AP: 0.9669 - AUC-ROC: 0.9669 - AUC-PR: 0.9715 - P@50: 0.9800 > C0282488: Cystitis Interstitial
AP: 0.9407 - AUC-ROC: 0.9407 - AUC-PR: 0.9456 - P@50: 0.9200 > C0034372: quadriplegia
AP: 0.8966 - AUC-ROC: 0.8966 - AUC-PR: 0.9319 - P@50: 0.9200 > C0014518: Lyell
AP: 0.9305 - AUC-ROC: 0.9305 - AUC-PR: 0.9528 - P@50: 0.9400 > C0235946: cerebral atrophy
AP: 0.9055 - AUC-ROC: 0.9055 - AUC-PR: 0.9418 - P@50: 0.9200 > C0151636: Extrasystoles Ventricular
AP: 0.9355 - AUC-ROC: 0.9355 - AUC-PR: 0.9535 - P@50: 0.9600 > C0010823: CMV infection
AP: 0.9305 - AUC-ROC: 0.9305 - AUC-PR: 0.9552 - P@50: 0.9400 > C1260880: rhinorrhea
AP: 0.8916 - AUC-ROC: 0.8916 - AUC-PR: 0.9259 - P@50: 0.9200 > C0002170: alopecia
AP: 0.9101 - AUC-ROC: 0.9101 - AUC-PR: 0.9395 - P@50: 0.9000 > C0017086: gangrene
AP: 0.9428 - AUC-ROC: 0.9428 - AUC-PR: 0.9599 - P@50: 0.9600 > C0040997: trigeminal neuralgia
AP: 0.9206 - AUC-ROC: 0.9206 - AUC-PR: 0.9497 - P@50: 0.9200 > C0019112: haemorrhoids
AP: 0.8642 - AUC-ROC: 0.8642 - AUC-PR: 0.9230 - P@50: 0.7600 > C0042029: Infection Urinary Tract
AP: 0.9351 - AUC-ROC: 0.9351 - AUC-PR: 0.9541 - P@50: 0.9600 > C0686347: tardive dyskinesia
AP: 0.9264 - AUC-ROC: 0.9264 - AUC-PR: 0.9490 - P@50: 0.9600 > C0021390: inflammatory bowel disease
AP: 0.8577 - AUC-ROC: 0.8577 - AUC-PR: 0.9116 - P@50: 0.8600 > C0016382: facial flushing
AP: 0.9175 - AUC-ROC: 0.9175 - AUC-PR: 0.9390 - P@50: 0.9800 > C0014457: Eosinophil Count Increased
AP: 0.9555 - AUC-ROC: 0.9555 - AUC-PR: 0.9599 - P@50: 0.9400 > C0030326: panniculitis
AP: 0.8908 - AUC-ROC: 0.8908 - AUC-PR: 0.9228 - P@50: 0.9600 > C0027080: myoglobinuria
AP: 0.9032 - AUC-ROC: 0.9032 - AUC-PR: 0.9441 - P@50: 0.8800 > C0016977: gall bladder
AP: 0.8924 - AUC-ROC: 0.8924 - AUC-PR: 0.9196 - P@50: 1.0000 > C0428977: bradycardia
AP: 0.9106 - AUC-ROC: 0.9106 - AUC-PR: 0.9399 - P@50: 0.9400 > C0314719: dry eye
AP: 0.8971 - AUC-ROC: 0.8971 - AUC-PR: 0.9378 - P@50: 0.8800 > C0039240: Supraventricular tachycardia
AP: 0.9505 - AUC-ROC: 0.9505 - AUC-PR: 0.9590 - P@50: 1.0000 > C0029878: external ear infection
AP: 0.9616 - AUC-ROC: 0.9616 - AUC-PR: 0.9663 - P@50: 0.9600 > C0085583: choreoathetosis
AP: 0.9306 - AUC-ROC: 0.9306 - AUC-PR: 0.9546 - P@50: 0.9600 > C0086769: panic attack
AP: 0.9142 - AUC-ROC: 0.9142 - AUC-PR: 0.9627 - P@50: 0.9400 > C0574960: sacroiliitis
AP: 0.8948 - AUC-ROC: 0.8948 - AUC-PR: 0.9429 - P@50: 0.8600 > C0018099: gout
AP: 0.9390 - AUC-ROC: 0.9390 - AUC-PR: 0.9566 - P@50: 0.9800 > C0037672: sleep walking
AP: 0.9230 - AUC-ROC: 0.9230 - AUC-PR: 0.9507 - P@50: 0.9200 > C0008325: cholecystitis
AP: 0.9595 - AUC-ROC: 0.9595 - AUC-PR: 0.9766 - P@50: 0.9600 > C0031090: periodontal disease
AP: 0.8873 - AUC-ROC: 0.8873 - AUC-PR: 0.9326 - P@50: 0.8800 > C0019360: herpes zoster
AP: 0.9630 - AUC-ROC: 0.9630 - AUC-PR: 0.9725 - P@50: 0.9800 > C0014118: endocarditis
AP: 0.9669 - AUC-ROC: 0.9669 - AUC-PR: 0.9806 - P@50: 0.9800 > C0016665: fracture nonunion
AP: 0.9708 - AUC-ROC: 0.9708 - AUC-PR: 0.9704 - P@50: 1.0000 > C0004030: aspergillosis
AP: 0.9156 - AUC-ROC: 0.9156 - AUC-PR: 0.9445 - P@50: 0.9600 > C0010054: arteriosclerotic heart disease
AP: 0.9373 - AUC-ROC: 0.9373 - AUC-PR: 0.9489 - P@50: 0.9200 > C0029124: optic atrophy
AP: 0.8928 - AUC-ROC: 0.8928 - AUC-PR: 0.9385 - P@50: 0.9000 > C0270996: eye swelling
AP: 0.9765 - AUC-ROC: 0.9765 - AUC-PR: 0.9801 - P@50: 0.9800 > C0007868: cervical dysplasia
AP: 0.9548 - AUC-ROC: 0.9548 - AUC-PR: 0.9651 - P@50: 0.9800 > C0010055: coronary artery bypass graft
AP: 0.9015 - AUC-ROC: 0.9015 - AUC-PR: 0.9472 - P@50: 0.9000 > C0011854: insulin dependent diabetes mellitus
AP: 0.8538 - AUC-ROC: 0.8538 - AUC-PR: 0.9048 - P@50: 0.8400 > C0595939: still birth
AP: 0.9395 - AUC-ROC: 0.9395 - AUC-PR: 0.9587 - P@50: 0.9600 > C0022408: arthropathy
AP: 0.9942 - AUC-ROC: 0.9942 - AUC-PR: 0.9940 - P@50: 1.0000 > C0151514: atrophy of skin
AP: 0.9374 - AUC-ROC: 0.9374 - AUC-PR: 0.9505 - P@50: 0.9400 > C0149678: EBV infection
AP: 0.9019 - AUC-ROC: 0.9019 - AUC-PR: 0.9402 - P@50: 0.9000 > C0003467: Anxiety
AP: 0.9530 - AUC-ROC: 0.9530 - AUC-PR: 0.9650 - P@50: 0.9800 > C0042267: Colpitis
AP: 0.8831 - AUC-ROC: 0.8831 - AUC-PR: 0.9320 - P@50: 0.8600 > C0015695: fatty liver
AP: 0.9554 - AUC-ROC: 0.9554 - AUC-PR: 0.9643 - P@50: 0.9600 > C0005687: distended bladder
AP: 0.9007 - AUC-ROC: 0.9007 - AUC-PR: 0.9278 - P@50: 0.9400 > C0034150: peliosis
AP: 0.9331 - AUC-ROC: 0.9331 - AUC-PR: 0.9688 - P@50: 0.9600 > C0009410: colostomy
AP: 0.9543 - AUC-ROC: 0.9543 - AUC-PR: 0.9629 - P@50: 0.9400 > C0003635: apraxia
AP: 0.9382 - AUC-ROC: 0.9382 - AUC-PR: 0.9619 - P@50: 0.9600 > C0007570: coeliac disease
AP: 0.9002 - AUC-ROC: 0.9002 - AUC-PR: 0.9360 - P@50: 0.9000 > C0019151: hepatic encephalopathy
AP: 0.9941 - AUC-ROC: 0.9941 - AUC-PR: 0.9931 - P@50: 0.9600 > C0020258: normal pressure hydrocephalus
AP: 0.8760 - AUC-ROC: 0.8760 - AUC-PR: 0.9259 - P@50: 0.8200 > C0231528: aching muscles
AP: 0.8667 - AUC-ROC: 0.8667 - AUC-PR: 0.9194 - P@50: 0.8400 > C0013384: abnormal movements
AP: 0.8892 - AUC-ROC: 0.8892 - AUC-PR: 0.9302 - P@50: 0.8800 > C0206062: ild
AP: 0.8769 - AUC-ROC: 0.8769 - AUC-PR: 0.9223 - P@50: 0.9200 > C0014591: epistaxis
AP: 0.9650 - AUC-ROC: 0.9650 - AUC-PR: 0.9695 - P@50: 1.0000 > C0027962: melanocytic naevus
AP: 0.8612 - AUC-ROC: 0.8612 - AUC-PR: 0.9167 - P@50: 0.8200 > C0149871: deep vein thromboses
AP: 0.9595 - AUC-ROC: 0.9595 - AUC-PR: 0.9672 - P@50: 0.9800 > C0042485: venous insufficiency
AP: 0.9207 - AUC-ROC: 0.9207 - AUC-PR: 0.9474 - P@50: 0.9600 > C0006840: Candida Infection
AP: 0.8887 - AUC-ROC: 0.8887 - AUC-PR: 0.9444 - P@50: 0.9400 > C0019917: hordeolum
AP: 0.9091 - AUC-ROC: 0.9091 - AUC-PR: 0.9376 - P@50: 0.9400 > C0702166: Acne
AP: 0.8764 - AUC-ROC: 0.8764 - AUC-PR: 0.9270 - P@50: 0.9200 > C0015408: eye injury
AP: 0.9181 - AUC-ROC: 0.9181 - AUC-PR: 0.9485 - P@50: 0.9400 > C0037315: sleep apnea
AP: 0.9632 - AUC-ROC: 0.9632 - AUC-PR: 0.9839 - P@50: 0.9800 > C0241353: testicular swelling
AP: 0.9608 - AUC-ROC: 0.9608 - AUC-PR: 0.9723 - P@50: 0.9800 > C0259749: autonomic neuropathy
AP: 0.9488 - AUC-ROC: 0.9488 - AUC-PR: 0.9562 - P@50: 0.9600 > C0006144: Breast cyst
AP: 0.9192 - AUC-ROC: 0.9192 - AUC-PR: 0.9443 - P@50: 0.9600 > C0002962: angina
AP: 0.9638 - AUC-ROC: 0.9638 - AUC-PR: 0.9723 - P@50: 0.9400 > C0019159: Hepatitis A
AP: 0.8730 - AUC-ROC: 0.8730 - AUC-PR: 0.9306 - P@50: 0.7600 > C0018989: hemiparesis
AP: 0.9219 - AUC-ROC: 0.9219 - AUC-PR: 0.9456 - P@50: 1.0000 > C0878544: Cardiomyopathy
AP: 0.8561 - AUC-ROC: 0.8561 - AUC-PR: 0.9145 - P@50: 0.8600 > C0007784: cerebral haemorrhage
AP: 0.9062 - AUC-ROC: 0.9062 - AUC-PR: 0.9380 - P@50: 0.9200 > C0025222: black stools
AP: 0.8984 - AUC-ROC: 0.8984 - AUC-PR: 0.9354 - P@50: 0.9000 > C0022116: ischaemia
AP: 0.9738 - AUC-ROC: 0.9738 - AUC-PR: 0.9816 - P@50: 0.9600 > C0028077: night blindness
AP: 0.9649 - AUC-ROC: 0.9649 - AUC-PR: 0.9750 - P@50: 0.9800 > C0042025: Stress incontinence
AP: 0.8976 - AUC-ROC: 0.8976 - AUC-PR: 0.9349 - P@50: 0.9000 > C0013491: ecchymoses
AP: 0.9610 - AUC-ROC: 0.9610 - AUC-PR: 0.9734 - P@50: 0.9800 > C0025322: premature menopause
AP: 0.9013 - AUC-ROC: 0.9013 - AUC-PR: 0.9382 - P@50: 0.9000 > C0151908: dry skin
AP: 0.9589 - AUC-ROC: 0.9589 - AUC-PR: 0.9655 - P@50: 1.0000 > C0027651: neoplasia
AP: 0.9105 - AUC-ROC: 0.9105 - AUC-PR: 0.9461 - P@50: 0.9200 > C0027796: Neuralgia
AP: 0.9266 - AUC-ROC: 0.9266 - AUC-PR: 0.9506 - P@50: 0.9600 > C0085636: Light sensitivity
AP: 0.8653 - AUC-ROC: 0.8653 - AUC-PR: 0.9113 - P@50: 0.9000 > C0042109: hive
AP: 0.8938 - AUC-ROC: 0.8938 - AUC-PR: 0.9413 - P@50: 0.8000 > C0032300: lobar pneumonia
AP: 0.9169 - AUC-ROC: 0.9169 - AUC-PR: 0.9449 - P@50: 0.9400 > C0162323: polyarthritis
AP: 0.9725 - AUC-ROC: 0.9725 - AUC-PR: 0.9782 - P@50: 0.9600 > C0040259: tinea pedis
AP: 0.8776 - AUC-ROC: 0.8776 - AUC-PR: 0.9283 - P@50: 0.8400 > C0000737: abdominal pain
AP: 0.9034 - AUC-ROC: 0.9034 - AUC-PR: 0.9372 - P@50: 0.9400 > C0020598: Blood calcium decreased
AP: 0.9029 - AUC-ROC: 0.9029 - AUC-PR: 0.9290 - P@50: 0.9200 > C0007876: Caesarean Section
AP: 0.9106 - AUC-ROC: 0.9106 - AUC-PR: 0.9428 - P@50: 0.9200 > C0023518: leucocytosis
AP: 0.8675 - AUC-ROC: 0.8675 - AUC-PR: 0.9194 - P@50: 0.8200 > C0015967: body temperature increased
AP: 0.9536 - AUC-ROC: 0.9536 - AUC-PR: 0.9626 - P@50: 0.9000 > C0015300: exophthalmos
AP: 0.9257 - AUC-ROC: 0.9257 - AUC-PR: 0.9454 - P@50: 0.9400 > C1384666: Decreased hearing
AP: 0.9235 - AUC-ROC: 0.9235 - AUC-PR: 0.9490 - P@50: 0.9600 > C0020443: elevated cholesterol
AP: 0.9549 - AUC-ROC: 0.9549 - AUC-PR: 0.9685 - P@50: 0.9600 > C0085662: macrocytosis
AP: 0.9241 - AUC-ROC: 0.9241 - AUC-PR: 0.9362 - P@50: 1.0000 > C0041956: ureteral obstruction
AP: 0.9784 - AUC-ROC: 0.9784 - AUC-PR: 0.9829 - P@50: 1.0000 > C0034887: rectal polyp
AP: 0.9226 - AUC-ROC: 0.9226 - AUC-PR: 0.9563 - P@50: 0.9400 > C0037383: sneezing
AP: 0.9154 - AUC-ROC: 0.9154 - AUC-PR: 0.9445 - P@50: 0.9400 > C0014868: esophagitis
AP: 0.8631 - AUC-ROC: 0.8631 - AUC-PR: 0.9178 - P@50: 0.8200 > C0019080: Bleeding
AP: 0.9421 - AUC-ROC: 0.9421 - AUC-PR: 0.9664 - P@50: 0.9600 > C0022671: kidney transplant
AP: 0.9742 - AUC-ROC: 0.9742 - AUC-PR: 0.9776 - P@50: 0.9800 > C0152030: Irritation Skin
AP: 0.9658 - AUC-ROC: 0.9658 - AUC-PR: 0.9702 - P@50: 0.9800 > C0030794: pain pelvic
AP: 0.9336 - AUC-ROC: 0.9336 - AUC-PR: 0.9489 - P@50: 1.0000 > C0037011: shoulder pain
AP: 0.8729 - AUC-ROC: 0.8729 - AUC-PR: 0.9174 - P@50: 0.8600 > C0002994: angioedema
AP: 0.9345 - AUC-ROC: 0.9345 - AUC-PR: 0.9624 - P@50: 0.9600 > C0085681: hyperphosphatemia
AP: 0.8884 - AUC-ROC: 0.8884 - AUC-PR: 0.9329 - P@50: 0.8400 > C0004093: asthenia
AP: 0.9441 - AUC-ROC: 0.9441 - AUC-PR: 0.9643 - P@50: 0.9400 > C0033860: psoriasis
AP: 0.9652 - AUC-ROC: 0.9652 - AUC-PR: 0.9664 - P@50: 1.0000 > C0020541: portal hypertension
AP: 0.9450 - AUC-ROC: 0.9450 - AUC-PR: 0.9607 - P@50: 0.9600 > C0009144: coated tongue
AP: 0.9508 - AUC-ROC: 0.9508 - AUC-PR: 0.9576 - P@50: 0.9600 > C0024236: lymphedema
AP: 0.9617 - AUC-ROC: 0.9617 - AUC-PR: 0.9684 - P@50: 0.9400 > C0011633: dermatomyositis
AP: 0.9188 - AUC-ROC: 0.9188 - AUC-PR: 0.9584 - P@50: 0.9400 > C0020540: malignant hypertension
AP: 0.8840 - AUC-ROC: 0.8840 - AUC-PR: 0.9339 - P@50: 0.9200 > C0149736: neck mass
AP: 0.9797 - AUC-ROC: 0.9797 - AUC-PR: 0.9808 - P@50: 1.0000 > C0003611: appendectomy
AP: 0.9688 - AUC-ROC: 0.9688 - AUC-PR: 0.9751 - P@50: 1.0000 > C0042594: Vestibular disorder
AP: 0.9154 - AUC-ROC: 0.9154 - AUC-PR: 0.9467 - P@50: 0.9400 > C0221706: road traffic accident
AP: 0.9604 - AUC-ROC: 0.9604 - AUC-PR: 0.9691 - P@50: 0.9600 > C0032768: Postherpetic Neuralgia
AP: 0.9526 - AUC-ROC: 0.9526 - AUC-PR: 0.9596 - P@50: 0.9600 > C0151966: duodenal ulcer haemorrhage
AP: 0.8831 - AUC-ROC: 0.8831 - AUC-PR: 0.9212 - P@50: 0.9200 > C0033774: itch
AP: 0.9489 - AUC-ROC: 0.9489 - AUC-PR: 0.9588 - P@50: 0.9600 > C0019294: Hernia Inguinal
AP: 0.8876 - AUC-ROC: 0.8876 - AUC-PR: 0.9295 - P@50: 0.9200 > C0085680: hypochloraemia
AP: 0.9035 - AUC-ROC: 0.9035 - AUC-PR: 0.9534 - P@50: 0.9000 > C0149512: acute sinusitis
AP: 0.9089 - AUC-ROC: 0.9089 - AUC-PR: 0.9376 - P@50: 0.9600 > C0030446: adynamic ileus
AP: 0.8952 - AUC-ROC: 0.8952 - AUC-PR: 0.9265 - P@50: 0.9400 > C0038379: Strabismus
AP: 0.9166 - AUC-ROC: 0.9166 - AUC-PR: 0.9362 - P@50: 0.9000 > C0006105: brain abscess
AP: 0.9420 - AUC-ROC: 0.9420 - AUC-PR: 0.9685 - P@50: 0.9600 > C0019212: hepatorenal syndrome
AP: 0.9262 - AUC-ROC: 0.9262 - AUC-PR: 0.9604 - P@50: 0.9600 > C0006107: brain concussion
AP: 0.8792 - AUC-ROC: 0.8792 - AUC-PR: 0.9297 - P@50: 0.8600 > C0020542: pulmonary hypertension
AP: 0.8995 - AUC-ROC: 0.8995 - AUC-PR: 0.9381 - P@50: 0.8600 > C0043094: weight gain
AP: 0.9200 - AUC-ROC: 0.9200 - AUC-PR: 0.9476 - P@50: 0.9600 > C0032326: pneumothorax
AP: 0.9359 - AUC-ROC: 0.9359 - AUC-PR: 0.9645 - P@50: 0.9400 > C0018621: hay fever
AP: 0.9456 - AUC-ROC: 0.9456 - AUC-PR: 0.9561 - P@50: 0.9800 > C0015806: femoral neck fracture
AP: 0.8979 - AUC-ROC: 0.8979 - AUC-PR: 0.9361 - P@50: 0.9200 > C0235329: Small intestinal obstruction
AP: 0.8962 - AUC-ROC: 0.8962 - AUC-PR: 0.9272 - P@50: 0.9400 > C0033036: atrial ectopic beats
AP: 0.8940 - AUC-ROC: 0.8940 - AUC-PR: 0.9271 - P@50: 0.9200 > C0007785: cerebral infarct
AP: 0.9816 - AUC-ROC: 0.9816 - AUC-PR: 0.9854 - P@50: 0.9800 > C0005961: bone marrow transplant
AP: 0.9386 - AUC-ROC: 0.9386 - AUC-PR: 0.9556 - P@50: 0.9600 > C0026846: amyotrophy
AP: 0.8897 - AUC-ROC: 0.8897 - AUC-PR: 0.9279 - P@50: 0.9400 > C0497156: Adenopathy
AP: 0.9341 - AUC-ROC: 0.9341 - AUC-PR: 0.9487 - P@50: 0.9800 > C0011880: diabetic acidosis
AP: 0.9160 - AUC-ROC: 0.9160 - AUC-PR: 0.9438 - P@50: 0.9400 > C0152025: polyneuropathy
AP: 0.8915 - AUC-ROC: 0.8915 - AUC-PR: 0.9277 - P@50: 0.9200 > C0032302: pneumonia primary atypical
AP: 0.9707 - AUC-ROC: 0.9707 - AUC-PR: 0.9755 - P@50: 1.0000 > C1510431: Superficial thrombophlebitis
AP: 0.9099 - AUC-ROC: 0.9099 - AUC-PR: 0.9550 - P@50: 0.9400 > C0006267: bronchiectasis
AP: 0.9934 - AUC-ROC: 0.9934 - AUC-PR: 0.9928 - P@50: 0.9400 > C0009193: coccydynia
AP: 0.8924 - AUC-ROC: 0.8924 - AUC-PR: 0.9381 - P@50: 0.9000 > C0026986: myelodysplasia
AP: 0.9103 - AUC-ROC: 0.9103 - AUC-PR: 0.9497 - P@50: 0.9400 > C0265031: Bleeding hemorrhoids
AP: 0.8896 - AUC-ROC: 0.8896 - AUC-PR: 0.9280 - P@50: 0.8800 > C0030312: bone marrow failure
AP: 0.9729 - AUC-ROC: 0.9729 - AUC-PR: 0.9769 - P@50: 1.0000 > C0262613: renal mass
AP: 0.9367 - AUC-ROC: 0.9367 - AUC-PR: 0.9543 - P@50: 0.9400 > C0019348: herpes simplex
AP: 0.8947 - AUC-ROC: 0.8947 - AUC-PR: 0.9303 - P@50: 0.9000 > C0018946: hematoma subdural
AP: 0.8724 - AUC-ROC: 0.8724 - AUC-PR: 0.9220 - P@50: 0.8200 > C0018799: cardiac disease
AP: 0.9376 - AUC-ROC: 0.9376 - AUC-PR: 0.9603 - P@50: 0.9600 > C0426636: defaecation urgency
AP: 0.9251 - AUC-ROC: 0.9251 - AUC-PR: 0.9477 - P@50: 0.9600 > C0026650: movement disorder
AP: 0.8839 - AUC-ROC: 0.8839 - AUC-PR: 0.9341 - P@50: 0.8800 > C0019196: Hepatitis C
AP: 0.9353 - AUC-ROC: 0.9353 - AUC-PR: 0.9599 - P@50: 0.9600 > C0004153: Atherosclerosis
AP: 0.8568 - AUC-ROC: 0.8568 - AUC-PR: 0.9096 - P@50: 0.8400 > C0020625: blood sodium decreased
AP: 0.9007 - AUC-ROC: 0.9007 - AUC-PR: 0.9354 - P@50: 0.9000 > C0003507: aortic stenosis
AP: 0.9507 - AUC-ROC: 0.9507 - AUC-PR: 0.9634 - P@50: 0.9600 > C0007780: cerebral artery embolism
AP: 0.9426 - AUC-ROC: 0.9426 - AUC-PR: 0.9508 - P@50: 0.9600 > C1527336: Sjogrens syndrome
AP: 0.8596 - AUC-ROC: 0.8596 - AUC-PR: 0.9133 - P@50: 0.8400 > C0020517: allergies
AP: 0.8816 - AUC-ROC: 0.8816 - AUC-PR: 0.9335 - P@50: 0.8400 > C0024117: chronic obstructive airway disease
AP: 0.9823 - AUC-ROC: 0.9823 - AUC-PR: 0.9839 - P@50: 1.0000 > C0156404: irregular menstrual cycle
AP: 0.9154 - AUC-ROC: 0.9154 - AUC-PR: 0.9360 - P@50: 0.9800 > C0973461: dysphasia
AP: 0.9359 - AUC-ROC: 0.9359 - AUC-PR: 0.9576 - P@50: 0.9400 > C0235328: colonic obstruction
AP: 0.9156 - AUC-ROC: 0.9156 - AUC-PR: 0.9476 - P@50: 0.9000 > C0040046: Thrombophlebitis
AP: 0.9150 - AUC-ROC: 0.9150 - AUC-PR: 0.9447 - P@50: 0.8800 > C0009324: chronic ulcerative colitis
AP: 0.9015 - AUC-ROC: 0.9015 - AUC-PR: 0.9412 - P@50: 0.8800 > C0085610: sinus bradycardia
AP: 0.9061 - AUC-ROC: 0.9061 - AUC-PR: 0.9520 - P@50: 0.9000 > C0009326: Collagen disease
AP: 0.9335 - AUC-ROC: 0.9335 - AUC-PR: 0.9582 - P@50: 0.9200 > C0004134: Ataxia
AP: 0.9160 - AUC-ROC: 0.9160 - AUC-PR: 0.9430 - P@50: 0.9600 > C0231807: Dyspnea exertional
AP: 0.9321 - AUC-ROC: 0.9321 - AUC-PR: 0.9595 - P@50: 0.9600 > C0025160: megacolon
AP: 0.9624 - AUC-ROC: 0.9624 - AUC-PR: 0.9725 - P@50: 0.9800 > C0030578: paronychia
AP: 0.9512 - AUC-ROC: 0.9512 - AUC-PR: 0.9635 - P@50: 0.9600 > C0005424: biliary tract disorder
AP: 0.8837 - AUC-ROC: 0.8837 - AUC-PR: 0.9317 - P@50: 0.7800 > C0013404: Difficulty breathing
AP: 0.8809 - AUC-ROC: 0.8809 - AUC-PR: 0.9292 - P@50: 0.9000 > C0040586: Tracheobronchitis
AP: 0.9422 - AUC-ROC: 0.9422 - AUC-PR: 0.9646 - P@50: 0.9400 > C0152029: nasal sinus congestion
AP: 0.9333 - AUC-ROC: 0.9333 - AUC-PR: 0.9553 - P@50: 0.9400 > C0029442: osteomalacia
AP: 0.9125 - AUC-ROC: 0.9125 - AUC-PR: 0.9385 - P@50: 0.9400 > C0035222: Acute Respiratory Distress Syndrome
AP: 0.9855 - AUC-ROC: 0.9855 - AUC-PR: 0.9890 - P@50: 0.9800 > C0262578: night cramps
AP: 0.9434 - AUC-ROC: 0.9434 - AUC-PR: 0.9626 - P@50: 0.9600 > C0026265: mitral valve disease NOS
AP: 0.9598 - AUC-ROC: 0.9598 - AUC-PR: 0.9672 - P@50: 0.9800 > C0022893: labyrinthitis
AP: 0.8846 - AUC-ROC: 0.8846 - AUC-PR: 0.9296 - P@50: 0.9000 > C0034063: lung edema
AP: 0.8961 - AUC-ROC: 0.8961 - AUC-PR: 0.9407 - P@50: 0.8400 > C0038999: bulging
AP: 0.9108 - AUC-ROC: 0.9108 - AUC-PR: 0.9494 - P@50: 0.9000 > C0033581: prostatitis
AP: 0.9338 - AUC-ROC: 0.9338 - AUC-PR: 0.9484 - P@50: 1.0000 > C0003537: aphasia
AP: 0.9160 - AUC-ROC: 0.9160 - AUC-PR: 0.9437 - P@50: 0.9400 > C0013595: eczema
AP: 0.9114 - AUC-ROC: 0.9114 - AUC-PR: 0.9354 - P@50: 0.9400 > C0000786: abortion spontaneous
AP: 0.9430 - AUC-ROC: 0.9430 - AUC-PR: 0.9560 - P@50: 0.9400 > C0021092: cerumen impaction
AP: 0.9311 - AUC-ROC: 0.9311 - AUC-PR: 0.9569 - P@50: 0.9400 > C0392699: dysaesthesia
AP: 0.8828 - AUC-ROC: 0.8828 - AUC-PR: 0.9250 - P@50: 0.9400 > C0010692: Bladder inflammation
AP: 0.9412 - AUC-ROC: 0.9412 - AUC-PR: 0.9598 - P@50: 0.9400 > C0007282: carotid artery stenosis
AP: 0.9640 - AUC-ROC: 0.9640 - AUC-PR: 0.9679 - P@50: 1.0000 > C0036202: sarcoidosis
AP: 0.9610 - AUC-ROC: 0.9610 - AUC-PR: 0.9678 - P@50: 0.9800 > C0002453: amenorrhea
AP: 0.9519 - AUC-ROC: 0.9519 - AUC-PR: 0.9688 - P@50: 0.9400 > C0021099: impetigo
AP: 0.9624 - AUC-ROC: 0.9624 - AUC-PR: 0.9678 - P@50: 0.9800 > C0274435: Transfusion reaction
AP: 0.9318 - AUC-ROC: 0.9318 - AUC-PR: 0.9551 - P@50: 0.9400 > C0518988: dental abscess
AP: 0.8814 - AUC-ROC: 0.8814 - AUC-PR: 0.9257 - P@50: 0.8800 > C0750426: increased white blood cell count
AP: 0.9106 - AUC-ROC: 0.9106 - AUC-PR: 0.9462 - P@50: 0.9400 > C0162316: iron deficiency anaemia
AP: 0.9677 - AUC-ROC: 0.9677 - AUC-PR: 0.9794 - P@50: 0.9800 > C0024894: breast inflammation
================================================================================
[AVERAGE] AP: 0.9234 - AUC-ROC: 0.9234 - AUC-PR: 0.9500 - P@50: 0.9320
================================================================================
``` 