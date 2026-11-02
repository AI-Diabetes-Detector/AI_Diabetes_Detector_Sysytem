from nlp_analysis import classify_question


def get_chatbot_response(question):

      category = classify_question(question)

      if category == "diabetes":

            return (
                  "Diabetes is a health condition related to how the body "
                  "handles blood glucose. Dia Detect AI only provides an "
                  "educational classification and not a medical diagnosis."
            )

      elif category == "prediction":

            return (
                  "The system predicts either class 0 or class 1. "
                  "Class 0 represents the no-diabetes class and class 1 "
                  "represents the diabetes/prediabetes class in the dataset."
            )

      elif category == "lifestyle":

            return (
                  "General healthy habits include balanced nutrition, "
                  "physical activity and routine health check-ups. "
                  "For personal medical guidance, consult a qualified "
                  "healthcare professional."
            )

      elif category == "project":

            return (
                  "Dia Detect AI is an educational diabetes classification "
                  "prototype. The main classifier used by the console "
                  "application is a Decision Tree."
            )

      return (
            "I can answer questions about diabetes, the prediction result, "
            "general healthy habits and the Dia Detect AI project."
      )


def main():

      print("=" * 60)
      print("DIA DETECT AI CHATBOT")
      print("Type exit to stop")
      print("=" * 60)

      while True:

            question = input("\nYou: ")

            if question.lower() == "exit":

                  print("Chatbot: Goodbye.")
                  break

            response = get_chatbot_response(question)

            print("Chatbot:",response)


if __name__ == "__main__":
      main()
