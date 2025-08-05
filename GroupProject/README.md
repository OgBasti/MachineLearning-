# Enhancing Stroke Prevention with Machine Learning: A Business Case for Insurance RPM

This project analyzes clinical and symptom data to predict stroke risk and identify high-risk individuals using machine learning. The objective is to support proactive healthcare and insurance remote patient monitoring (RPM) by enabling early interventions and data-driven decision-making.

## Overview
- **Goal:** Develop predictive models to assess individual stroke risk, identify at-risk patients, and provide actionable insights for healthcare and insurance applications, particularly focusing on integration with RPM systems.
- **Data:** Clinical dataset comprising patient demographics, 15 binary symptom indicators, stroke risk percentages, and binary at-risk classification, curated based on medical literature and expert guidance.

## Main Features in Data
| Feature                     | Description                                                    |
|-----------------------------|----------------------------------------------------------------|
| Age                         | Patient age (major risk factor)                                |
| Binary Symptoms             | Presence/absence of key symptoms such as chest pain, fatigue, dizziness, etc. |
| Stroke Risk (%)              | Continuous risk score representing probability of stroke       |
| At Risk (Binary)             | Binary indicator if stroke risk > 50%                           |

## Workflow
- Exploratory Data Analysis (EDA) to understand feature distributions and correlations
- Unsupervised Learning via clustering to identify patient subgroups based on symptoms and risk profiles
- Development of Regression models to predict stroke risk as a continuous variable, including symptom-driven and age-adjusted approaches
- Development of Classification models (Logistic Regression, Random Forest, Gradient Boosting) focusing on maximizing recall to reduce missed stroke cases
- Model interpretation and feature importance analysis using SHAP and LIME explainability tools
- Business and clinical recommendations for integration into RPM systems and insurance risk stratification

## Libraries
pandas, NumPy, scikit-learn, SHAP, LIME, matplotlib, seaborn

## Key Results
- Identified three meaningful patient clusters differentiated by symptom prevalence and stroke risk levels
- Developed a symptom-focused Random Forest Regression model achieving R² = 0.42 without using age, enhancing clinical interpretability
- Gradient Boosting classifier chosen for stroke detection due to highest recall (0.91), prioritizing minimizing false negatives in a medical context
- Key symptoms influencing stroke risk prediction include chest pain, fatigue, high blood pressure, cold hands/feet, and excessive sweating
- Actionable recommendations include incorporating symptom-based digital scoring, wearable patient monitoring, and continuous model validation to support preventive care and insurance RPM integration

## Limitations and Future Work
- Real-world clinical data complexity (noise, missing values) not fully modeled
- Potential demographic biases affecting generalization and fairness across age groups
- Lack of temporal symptom progression data limits dynamic risk prediction
- Future research should include validating models on real-world datasets, incorporating time-series features, and ensuring equitable performance across populations

---

*See the full report and appendix for detailed analyses, visualizations, methodology, and references.*
