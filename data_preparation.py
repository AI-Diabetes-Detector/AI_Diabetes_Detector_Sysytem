import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("data/diabetes_binary_health_indicators_BRFSS2015.csv")

# ============================================================================
# DATA PROCESSING & CLEANING
# ============================================================================

# 1. Remove duplicate rows (BRFSS datasets frequently contain duplicates)
print("Initial shape:", data.shape)
data = data.drop_duplicates()
print("Shape after dropping duplicates:", data.shape)

# 2. Check for missing values
missing_values = data.isnull().sum().sum()
print(f"Total missing values: {missing_values}")

# 3. Separate features (x) and target (y)
y = data["Diabetes_binary"]
x = data.drop("Diabetes_binary", axis=1)

# 4. Feature Scaling for continuous variables
# Logistic regression performs better when continuous features (like BMI) 
# are on the same scale as binary/ordinal indicators.
continuous_features = ["BMI", "MentHlth", "PhysHlth"]

scaler = StandardScaler()
x[continuous_features] = scaler.fit_transform(x[continuous_features])

# ============================================================================
# TRAIN/TEST SPLIT
# ============================================================================
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# ============================================================================
# MODEL CREATION AND TRAINING
# ============================================================================
balanced_model = LogisticRegression(max_iter=1000, class_weight="balanced")
balanced_model.fit(x_train, y_train)
balanced_predictions = balanced_model.predict(x_test)

# ============================================================================
# EVALUATION
# ============================================================================
print("\n--- Balanced Logistic Regression Results ---")
print("Accuracy:", accuracy_score(y_test, balanced_predictions))
print("Confusion Matrix:\n", confusion_matrix(y_test, balanced_predictions))
print("Classification Report:\n", classification_report(y_test, balanced_predictions))