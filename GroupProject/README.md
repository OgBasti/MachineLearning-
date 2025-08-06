# Stroke Prediction – Machine Learning Classification Project

This repository contains a machine learning classification project focused on predicting the likelihood of stroke occurrence using patient health data.

## Overview

- **Goal:** Build and evaluate classification models to predict stroke based on clinical and demographic features.
- **Project Context:** Conducted as part of a group assignment involving preprocessing, model selection, and performance evaluation using scikit-learn.

## Main Data Features

| Feature             | Description                                     |
|---------------------|-------------------------------------------------|
| gender              | Gender of the patient                           |
| age                 | Age in years                                    |
| hypertension        | Whether the patient has hypertension            |
| heart_disease       | Whether the patient has heart disease           |
| ever_married        | Marital status                                  |
| work_type           | Type of employment                              |
| Residence_type      | Urban or rural residence                        |
| avg_glucose_level   | Average glucose level                           |
| bmi                 | Body Mass Index                                 |
| smoking_status      | Smoking habits                                  |
| stroke              | Target variable (1 = stroke, 0 = no stroke)     |

*(See notebook for complete preprocessing and feature engineering steps.)*

## Workflow

- Load and clean the dataset
- Handle missing values and encode categorical variables
- Perform feature selection and standardization
- Train multiple classification models (e.g., Logistic Regression, Random Forest, etc.)
- Evaluate model performance using accuracy, precision, recall, F1-score, and AUC

## Data Source

Data sourced from the [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset), based on real patient records.

## Results

- Best-performing models identified based on cross-validation scores and evaluation metrics
- Feature importance explored and interpreted
- Limitations and suggestions for future improvements discussed

---

_See the notebook (`group_Y_stroke_prediction.ipynb`) for full code, results, and explanations._
