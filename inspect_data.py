import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

data = pd.read_csv("data/diabetes_binary_health_indicators_BRFSS2015.csv") #Read an csv dataset
#print(data.head()) #Display something in the terminal
#print(data.shape) #Tells us the size of the data frame (253680, 22) -> Number of records and Columns
#print(data.columns) #Show us all the colums that exist within our dataset
#print(data.isnull().sum()) #Check our dataset if there are missing values, anda then show us how many missing values
#print(data["Diabetes_binary"].value_counts()) #Show me contents of "Diabetes_binary" column and Count how many times each unique value appears.
#print(data["Diabetes_binary"].value_counts(normalize=True) * 100)


y = data["Diabetes_binary"]
x = data.drop("Diabetes_binary", axis = 1)

#print(x.shape)
#print(y.shape)

#============================================================================
# TRAIN/TEST SPLIT
#============================================================================
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

#print(x_test.shape)
#print(x_train.shape)
#print(y_test.shape)
#print(y_train.shape)

#============================================================================
# MODELL CREATION  AND TRAINING = WE USE THE LOGISTIC REGRESSION
#============================================================================
#model = LogisticRegression(max_iter=1000)
balanced_model = LogisticRegression(max_iter=1000, class_weight="balanced")
balanced_model.fit(x_train, y_train)
balanced_predictions = balanced_model.predict(x_test)
#print(predictions[:10])
#print("predictions:",predictions[:20])
#print("Actual:", y_test.values[:20])
#print(pd.Series(predictions).value_counts())
#print(pd.Series(predictions).value_counts(normalize=True) * 100)

#============================================================================
# MODEL CAN'T PREDICT ACCURATELY, SO WE INVESTIGATE 
#============================================================================
print("Balanced Logistic Regression")

print("Accuracy:", accuracy_score(y_test,balanced_predictions))
#accuracy = accuracy_score(y_test, balanced_predictions)
#print ("Accuracy:" , accuracy * 100)

#matrix = confusion_matrix(y_test, balanced_predictions)
#print(matrix)

print("Confusion Matrix:")
print(confusion_matrix(y_test,balanced_predictions))

print("Classification Report:")
print(classification_report(y_test,balanced_predictions))