---
title: "Development of Prediction Model for Brain Amyloid-Beta Accumulation for Early Screening of Alzheimer's Disease"
date: "2025-02-14 11:49:19"
summary: "TOKYO, Feb 14, 2025 - (JCN Newswire) - Oita University and Eisai Co., Ltd. (Eisai) announced today the development of a machine learning model to predict amyloid beta(1)(Abeta) accumulation in the brain, combining background data such as age, gender, smoking history and medical history, as well as general blood test..."
categories:
  - "Reuters"
lang:
  - "en"
translations:
  - "en"
tags:
  - "Reuters"
menu: ""
thumbnail: ""
lead: ""
comments: false
authorbox: false
pager: true
toc: false
mathjax: false
sidebar: "right"
widgets:
  - "search"
  - "recent"
  - "taglist"
---

TOKYO, Feb 14, 2025 - (JCN Newswire) - Oita University and Eisai Co., Ltd. (Eisai) announced today the development of a machine learning model to predict amyloid beta(1)(Abeta) accumulation in the brain, combining background data such as age, gender, smoking history and medical history, as well as general blood test and MMSE(2) items. This model is expected to enable primary care physicians to predict the accumulation of brain Abeta, which is an important pathological factor of Alzheimer's disease(3) (AD), during routine medical examinations and to facilitate simple early screening for AD.

The details of this model were published in the online edition of the peer-reviewed medical journal Alzheimer's Research & Therapy on January 21, 2025.

Currently, although brain Abeta accumulation can be detected by positron emission tomography(4) (amyloid PET) and cerebrospinal fluid testing(5) (CSF testing), the high cost and invasiveness of these tests are recognized as issues. Therefore, in recent years,numerous studies have been conducted on various AD- related blood biomarkers as a more convenient screening method. However, there is almost no research evaluating the predictive performance of models for brain Abeta accumulation using routineclinical data. This study is the first to develop a machine learning model for prediction of amyloid PET positivity using 34 clinical data items consisting of background data (such as age, gender, smoking history, and medical history), general blood test data (such as kidney function, liver function, and thyroid function), and MMSE items, which are routinely collected in dementia care. The evaluation metric of the prediction model, the Area Under the Curve (AUC), was 0.70 for the model combining background data and general blood test data, and 0.73 for the model combining background data, general blood test data, and MMSE data, indicating a certain level of predictive accuracy.

Anti-Abeta antibody has been shown to potentially provide greater benefit when treatment is initiated at an earlier stage of AD1 ,making early detection of Abeta accumulation in the brain crucial. This machine learning model can predict brain Abeta accumulation using clinical data that can be collected during routine medical care, and so is expected to be widely used by primary care physicians for early screening of AD.

By utilizing the model to determine the necessity of amyloid PET and CSF tests, it is anticipated to lead to early diagnosis andtreatment initiation for AD, as well as a reduction in the economic and physical burden on patients.

(1) Amyloid beta: A protein viewed as a cause of Alzheimer's disease, which accumulates in the brain for about 20 years prior to the onset of the disease and forms senile plaques

(2) MMSE (Mini-Mental State Examination): A method for evaluating cognitive function. It consists of evaluation items such as orientation, memory, attention/calculation, delayed recall, naming, repetition, comprehension, reading, writing, and figure copying, and is evaluated between 30 to 0 points (normal to severe).

(3) Alzheimer's disease: the most common cause of dementia, and its pathological characteristics include senile plaques, neurofibrillary tangles, and neuronal cell death

(4) Amyloid PET: a brain imaging test visualizing Abeta accumulation in the brain

(5) Cerebrospinal fluid testing: A test analyzing cerebrospinal fluid for Abeta, phosphorylated tau, and total tau as biomarkers of Alzheimer's disease

Background and Outline of Research

As Japan has become a super-aging society with the rise in the number of dementia patients over the age of 65, the developmentof new therapeutic agents for AD, the most common cause of dementia, is an urgent issue. In AD, accumulation of Abeta in the brain is apathological event that precedes onset. It has been shown that anti-Abeta antibody could offer greater benefit if treatment is initiated atearlier stages of AD1, highlighting the importance of earlier detection of Abeta accumulation in the brain. While imaging such as amyloid PET useful for AD diagnosis and fluid biomarkers are used for detection, these methods have challenges related to invasiveness and cost.

Therefore, many machine learning-based brain Abeta prediction models have been developed as simpler screening tools, but oftenthese models incorporate markers not measured in routine clinical practice, such as imaging data and ApoE genotype. This study is the first to attempt the development of a machine learning model to predict amyloid PET positivity using only background dataand general blood test results routinely collected in dementia care.

Results and Significance of Research

This research utilized outpatient data from Oita University Hospital collected between September 2012 and November 2017, anddata from a prospective cohort study (USUKI STUDY) on the elderly without dementia aged 65 and older living in Usuki City, Oita Prefecture, conducted between October 2015 and November 2017. The prediction model was created using three machine learningtechniques: Support Vector Machine, Elastic Net, and L2 regularization logistic regression, combining 12 items on participants'backgrounds (age, gender, smoking history, medical history - hypertension, dyslipidemia, heart disease, stroke, diabetes, thyroid disease), 11 general blood test items (kidney function, liver function, thyroid function, etc.), and 11 MMSE item scores of 262 individuals (136 men, 126 women, median age 73.8 years) with mild cognitive impairment or normal cognitive function, and evaluating the model's performance.

For the prediction performance using L2 regularization logistic regression, both the model combining participant backgrounds and MMSE items and the model combining participant backgrounds and general blood tests showed an AUC of 0.70, indicating similarperformance. Furthermore, the model that combined all of these elements (participant backgrounds, general blood tests, and MMSEitems) showed an improved performance with an AUC of 0.73. Analyzing the key factors contributing to the prediction of Abeta accumulation identified delayed recall and place orientation among MMSE items, age, thyroid-stimulating hormone, and mean corpuscular volume as important factors.

Academic Paper:

Title: Machine learning models for dementia screening to classify brain amyloid positivity on positron emission tomography using blood markers and demographic characteristics: a retrospective observational study

Authors: Noriyuki Kimura (Department of Neurology, Faculty of Medicine, Oita University), Kotaro Sasaki (Eisai Co., Ltd), TeruakiMasuda (Department of Neurology, Faculty of Medicine, Oita University), Takuaki Ataka (Department of Neurology, Faculty ofMedicine, Oita University), Mariko Matsumoto (Eisai Co., Ltd.), Mika Kitamura (Eisai Co., Ltd.), Yosuke Nakamura (Eisai Co., Ltd.), Etsuro Matsubara (Department of Neurology, Faculty of Medicine, Oita University)

Publisher: Alzheimer's Research & Therapy

Please direct any interview requests or inquiries to the contact information provided below For further information or any inquiries regarding this study

Noriyuki Kimura, Associate Professor, Department of Neurology, Faculty of Medicine, Oita University

TEL: +81-(0)97-586-5814, FAX: +81-(0)97-586-6502

Email: naika3@oita-u.ac.jp

Media Inquiries:

Oita University

Public Relations Section, General Affairs Division, Department of General Affairs

TEL: +81-(0)97-554-7376

Eisai Co., Ltd.

Public Relations Department

TEL: +81-(0)3-3817-5120

Source: Eisai

Copyright 2025 JCN Newswire . All rights reserved.

[Reuters](https://www.tradingview.com/news/reuters.com,2025-02-14:newsml_JCN96056a:0-development-of-prediction-model-for-brain-amyloid-beta-accumulation-for-early-screening-of-alzheimer-s-disease/)
