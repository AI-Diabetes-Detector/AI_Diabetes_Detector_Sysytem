from data_preparation import load_data, prepare_data
from train_models import train_decision_tree
import pandas as pd 

def get_yes_no(question):
      
      while True:
           
           try:
                
               answer = int(input(question + " (1 = yes, 0 = no): "))

               if answer == 0 or answer == 1:
                      return answer

               print("Please only enter 1 for yes or 0 for no")

           except ValueError:
            print("Please enter a number: 1 for yes or 0 for no.")


def get_range(question,minimum,maximum):

     while True:
          try:
               answer = int(input(question))

               if minimum <= answer <= maximum:
                 return answer

               print("Please enter value between", minimum, "and",maximum)

          except ValueError:
               print("Please enter a whole number.")

def main():

      print("=" * 60)
      print("DIA DETECT AI")
      print("Diabetes Classification prototype")
      print("=" * 60)


      data = load_data()

      x_train,x_test,y_train,y_test = prepare_data(data)

      model = train_decision_tree(x_train,y_train)

      print("\n Model trained successfully")

      high_bp = get_yes_no("Do you have high blood pressure?")
      high_chol = get_yes_no("Do you have high cholesterol?")
      chol_check = get_yes_no("Have you had your cholesterol checked?")
      bmi = float(input("Enter your BMI: "))
      smoker = get_yes_no("Have you  smoked at least 100 cigarettes in your life?")
      stroke = get_yes_no("Have you ever had stroke?")
      heart_disease = get_yes_no("Have you ever had coronary heart diseases or a heart attack?")
      physical_activity = get_yes_no("Have you done physical activity in the past 30 days")
      fruits = get_yes_no("Do you consume fruits once or more times per day?")
      veggies = get_yes_no("Do you consume vegetables once or more times per day?")
      heavy_alcohol = get_yes_no("Do meet the datasets heavy alcohol consumption category")
      healthcare = get_yes_no("DO you have healthcare coverage?")
      no_doctor_cost = get_yes_no("Was there a time you needed a doctore but could not see one because of costs")

      print("\nGeneral Health")
      print("1 = Excellent")
      print("2 = Very good")
      print("3 = Good")
      print("4 = Fair")
      print("5 = Poor")

      general_health = get_range("Enter you general health category: ", 1, 5)
      mental_health = get_range("Number of poor mental health days in the last 30 days: ", 0, 30)
      physical_health = get_range("Number of poor physical health days in the last 30 days: ",0,30)
      difficulty_walking = get_yes_no("Do you have a serious difficulty ealking or climbing stairs?")

      print("\nSex")
      print("0 = Female")
      print("1 = Male")

      sex = get_range("Enter sex category: " , 0, 1)

      print("\nAge Category")
      print("1  = 18-24")
      print("2  = 25-29")
      print("3  = 30-34")
      print("4  = 35-39")
      print("5  = 40-44")
      print("6  = 45-49")
      print("7  = 50-54")
      print("8  = 55-59")
      print("9  = 60-64")
      print("10 = 65-69")
      print("11 = 70-74")
      print("12 = 75-79")
      print("13 = 80+")

      age = get_range("Enter age category: ",1,13)

      print("\nEducation Category")
      print("1 = Never attended school / Creché")
      print("2 = Grades 1-8")
      print("3 = Grades 9-11")
      print("4 = Grade 12 / GED")
      print("5 = College 1-3 years")
      print("6 = College 4 years or more")

      education = get_range("Enter education category: ",1,6)

      print("\nIncome Category")
      print("1 = Less than $10,000")
      print("2 = $10,000 - $15,000")
      print("3 = $15,000 - $20,000")
      print("4 = $20,000 - $25,000")
      print("5 = $25,000 - $35,000")
      print("6 = $35,000 - $50,000")
      print("7 = $50,000 - $75,000")
      print("8 = $75,000 or more")

      income = get_range("Enter income category: " ,1,8)
      
      print("\nINPUT CHECK")
      print("HighBP:", high_bp)
      print("HighChol:", high_chol)
      print("CholCheck:", chol_check)
      print("BMI:",bmi)
      print("Smoker:", smoker)
      print("Stroke:", stroke)
      print("HeartDiseaseorAttack:", heart_disease)
      print("PhysActivity:", physical_activity)
      print("Fruits:", fruits)
      print("Veggies:", veggies)
      print("HvyAlcoholConsump:", heavy_alcohol)
      print("AnyHealthcare:", healthcare)
      print("NoDocbcCost:", no_doctor_cost)
      print("GenHlth:", general_health)
      print("MentHlth:", mental_health)
      print("PhysHlth:", physical_health)
      print("DiffWalk:", difficulty_walking)
      print("Sex:", sex)
      print("Age:", age)
      print("Education:", education)
      print("Income:", income)

      user_data = pd.DataFrame(
           [[
                high_bp,
                high_chol,
                chol_check,
                bmi,
                smoker,
                stroke,
                heart_disease,
                physical_activity,
                fruits,
                veggies,
                heavy_alcohol,
                healthcare,
                no_doctor_cost,
                general_health,
                mental_health,
                physical_health,
                difficulty_walking,
                sex,
                age,
                education,
                income
           ]],
           columns = x_train.columns)
      
      prediction = model.predict(user_data)

      print("\n" + "=" * 60)
      print("PREDICTION RESULT")
      print("=" * 60)

      if prediction[0] == 0:

                    print("Predicted class: 0")
                    print("No-diabetes class")

      else:

                     print("Predicted class: 1")
                     print("Diabetes/prediabetes class")


      print("\nThis system is an educational classification prototype.")
      print("It does not provide a medical diagnosis.")

if __name__ == "__main__" :
    main()


