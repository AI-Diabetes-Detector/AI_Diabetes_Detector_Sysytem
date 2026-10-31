import pandas as pd
from sklearn.model_selection import train_test_split

DATA_PATH = "data/diabetes_binary_health_indicators_BRFSS2015.csv"
TARGET_COLUMN = "Diabetes_binary"

FEATURE_COLUMNS = [
      "HighBP",
      "HighChol",
      "CholCheck",
      "BMI",
      "Smoker",
      "Stroke",
      "HeartDiseaseorAttack",
      "PhysActivity",
      "Fruits",
      "Veggies",
      "HvyAlcoholConsump",
      "AnyHealthcare",
      "NoDocbcCost",
      "GenHlth",
      "MentHlth",
      "PhysHlth",
      "DiffWalk",
      "Sex",
      "Age",
      "Education",
      "Income"
]


def load_data():

      data = pd.read_csv(DATA_PATH)

      return data


def prepare_data(data):

      x = data[FEATURE_COLUMNS]
      y = data[TARGET_COLUMN]

      x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.40,random_state=42)

      return x_train,x_test,y_train,y_test


def show_data_information(data):

      print("Dataset shape:",data.shape)

      print("\nTarget class counts:")
      print(data[TARGET_COLUMN].value_counts())

      print("\nMissing values:")
      print(data.isnull().sum())
