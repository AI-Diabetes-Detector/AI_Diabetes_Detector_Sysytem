from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_sentences = [
      "What is diabetes",
      "Tell me about diabetes",
      "What does diabetes mean",
      "What is prediabetes",
      "How does the prediction work",
      "What does class zero mean",
      "What does class one mean",
      "Explain the prediction result",
      "How can I stay healthy",
      "Tell me about physical activity",
      "What about healthy food",
      "Should I see a doctor",
      "What is Dia Detect AI",
      "Is this a medical diagnosis",
      "What model does the project use",
      "What is the purpose of this project"
]

training_categories = [
      "diabetes",
      "diabetes",
      "diabetes",
      "diabetes",
      "prediction",
      "prediction",
      "prediction",
      "prediction",
      "lifestyle",
      "lifestyle",
      "lifestyle",
      "lifestyle",
      "project",
      "project",
      "project",
      "project"
]


def create_nlp_model():

      vectorizer = CountVectorizer()

      training_features = vectorizer.fit_transform(training_sentences)

      classifier = MultinomialNB()

      classifier.fit(training_features,training_categories)

      return vectorizer,classifier


def classify_question(question):

      vectorizer,classifier = create_nlp_model()

      question_features = vectorizer.transform([question])

      category = classifier.predict(question_features)

      return category[0]


def main():

      question = input("Enter a question: ")

      category = classify_question(question)

      print("Detected category:",category)


if __name__ == "__main__":
      main()
