# DiaDetect AI — AI-Driven Diabetes Predictor System

## Project Overview

DiaDetect AI is a Python-based educational machine learning project developed for **Business Analysis 3.2 (AIBUY3A)** at the **Vaal University of Technology**.

The system uses health, lifestyle, healthcare-access, and demographic indicators from the **BRFSS 2015 Diabetes Health Indicators dataset** to classify a record into one of two classes:

- **0** — No-diabetes class
- **1** — Diabetes/prediabetes class

The project is intended for educational and awareness purposes only. It does not provide a medical diagnosis and should not replace professional medical advice, screening, diagnosis, or treatment.

## Group Members

- D Mabunda — 223975753
- FL Phokungwana — 224119966
- PN Mabasa — 240397177
- VD Mathosi — 224506501
- E Nongqoto — 224569600
- R Nemutanzhela — 223377589
- M Ndlovu — 222435119

## Project Aim

The main aim of the project is to develop a machine learning application that:

- accepts 21 health and lifestyle indicators;
- trains and compares supervised classification models;
- produces a binary diabetes classification;
- provides a simple user-facing recommendation;
- demonstrates additional AI concepts such as NLP, chatbot functionality, deep learning, and time-series analysis.

## Dataset

The project uses the Kaggle **Diabetes Health Indicators Dataset — BRFSS 2015**.

Dataset size:

- **253,680 records**
- **22 columns**
- **21 input features**
- **1 target column: `Diabetes_binary`**

The 21 input features are:

1. HighBP
2. HighChol
3. CholCheck
4. BMI
5. Smoker
6. Stroke
7. HeartDiseaseorAttack
8. PhysActivity
9. Fruits
10. Veggies
11. HvyAlcoholConsump
12. AnyHealthcare
13. NoDocbcCost
14. GenHlth
15. MentHlth
16. PhysHlth
17. DiffWalk
18. Sex
19. Age
20. Education
21. Income

## Machine Learning Models

The project trains and compares three supervised classification models:

- Logistic Regression
- Decision Tree
- Random Forest

The models are evaluated using:

- Accuracy
- Precision
- Recall
- Confusion Matrix

### Primary Model

The **Decision Tree** is used as the primary classifier in the main application.

Although Logistic Regression produced the highest overall accuracy during testing, the Decision Tree achieved the highest recall for the diabetes/prediabetes class.

Model results from the project testing:

| Model | Accuracy | Class-1 Recall |
|---|---:|---:|
| Logistic Regression | 86.47% | 15.79% |
| Decision Tree | 79.59% | 32.32% |
| Random Forest | 85.91% | 17.11% |

The Random Forest also showed a large difference between training and testing accuracy, indicating overfitting in the tested configuration.

## Project Files

### `main.py`

Main console application. It loads the dataset, prepares the data, trains the Decision Tree, collects the 21 user inputs, validates them, displays an input summary, and produces the prediction.

### `data_preparation.py`

Handles dataset loading, feature selection, target selection, train/test splitting, and basic dataset information.

### `train_models.py`

Trains Logistic Regression, Decision Tree, and Random Forest models and sends their predictions for evaluation.

### `evaluate_models.py`

Calculates accuracy, confusion matrix values, precision, and recall.

### `recommendations.py`

Converts the predicted class into a user-friendly result and recommendation and includes the project disclaimer.

### `nlp_analysis.py`

Demonstrates Natural Language Processing using text feature extraction and category prediction with `CountVectorizer` and `MultinomialNB`.

### `chatbot.py`

Provides a simple chatbot interface for questions about diabetes, prediction results, healthy lifestyle guidance, and the project.

### `deep_learning.py`

Demonstrates a simple neural-network approach using Keras `Sequential` and `Dense` layers. This is an additional AI demonstration and is not the primary classifier used by `main.py`.

### `time_series_analysis.py`

Demonstrates basic time-series concepts using Pandas. The BRFSS dataset does not contain a genuine date/time field, so this module uses an illustrative sample sequence.

### `requirements.txt`

Contains the main Python dependencies required by the project.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AI-Diabetes-Detector/AI_Diabetes_Detector_Sysytem.git
```

```bash
cd AI_Diabetes_Detector_Sysytem
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Dataset location

Place the dataset inside:

```text
data/
└── diabetes_binary_health_indicators_BRFSS2015.csv
```

Expected structure:

```text
AI_Diabetes_Detector_Sysytem/
│
├── data/
│   └── diabetes_binary_health_indicators_BRFSS2015.csv
│
├── main.py
├── data_preparation.py
├── train_models.py
├── evaluate_models.py
├── recommendations.py
├── nlp_analysis.py
├── chatbot.py
├── deep_learning.py
├── time_series_analysis.py
├── requirements.txt
└── README.md
```

## Running the Project

Main application:

```bash
python main.py
```

Train and compare models:

```bash
python train_models.py
```

NLP demonstration:

```bash
python nlp_analysis.py
```

Chatbot:

```bash
python chatbot.py
```

Deep learning demonstration:

```bash
python deep_learning.py
```

Time-series demonstration:

```bash
python time_series_analysis.py
```

## System Flow

```text
Dataset
   ↓
Data Preparation
   ↓
Train and Compare Models
   ↓
Select Decision Tree
   ↓
Collect 21 User Inputs
   ↓
Create Model Input
   ↓
Prediction
   ↓
Recommendation / Disclaimer
```

## Ethical and Medical Considerations

- The dataset is based on self-reported survey information.
- The system does not measure blood glucose.
- A model prediction can be incorrect.
- False negatives are important because an actual positive case may be classified as negative.
- The output must never be treated as a confirmed medical diagnosis.
- Users should consult qualified healthcare professionals for screening, diagnosis, and treatment.

## Additional AI Components

The project also demonstrates:

- Supervised Machine Learning
- Natural Language Processing
- Chatbot / Softbot
- Deep Learning
- Time-Series Analysis

The primary practical solution remains the supervised diabetes classification system.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Keras
- TensorFlow
- Git
- GitHub

## Version Control

Git and GitHub are used for source control, group collaboration, branch-based development, tracking changes, and merging completed project components.

## References

- Tutorials Point — *AI with Python*
- Kaggle — *Diabetes Health Indicators Dataset / BRFSS 2015*
- Centers for Disease Control and Prevention (CDC) — Diabetes information and risk guidance

## Disclaimer

**DiaDetect AI is an educational machine learning prototype. It does not provide medical diagnoses and must not be used as a replacement for professional healthcare advice, screening, diagnosis, or treatment.**
