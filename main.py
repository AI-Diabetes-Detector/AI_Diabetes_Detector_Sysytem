from data_preparation import load_data, prepare_data
from train_models import train_decision_tree

def get_yes_no(question):
      
      while True:
           
           try:
                
               answer = int(input(question + "(1 = yes, 0 = no): "))

               if answer == 0 or answer == 1:
                      return answer

               print("Please only enter 1 for yes or 0 for no")

           except ValueError:
            print("Please enter a number: 1 for yes or 0 for no.")


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

      print("\nINPUT CHECK")
      print("HighBP:", high_bp)
      print("HighChol:", high_chol)
      print("CholCheck:", chol_check)
      print("BMI:",bmi)
      

if __name__ == "__main__" :
    main()


