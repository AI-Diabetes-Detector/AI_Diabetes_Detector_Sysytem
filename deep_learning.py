from keras.models import Sequential
from keras.layers import Dense
from data_preparation import load_data, prepare_data


def build_deep_learning_model(input_count):

      model = Sequential()

      model.add(Dense(21,input_dim=input_count,activation="relu"))

      model.add(Dense(1,activation="sigmoid"))

      model.compile(
            optimizer="adam",
            loss="binary_crossentropy",
            metrics=["accuracy"]
      )

      return model


def main():

      data = load_data()

      x_train,x_test,y_train,y_test = prepare_data(data)

      model = build_deep_learning_model(x_train.shape[1])

      model.fit(
            x_train,
            y_train,
            epochs=5,
            batch_size=32,
            verbose=1
      )

      prediction = model.predict(x_test[:1])

      print("\nDEEP LEARNING SAMPLE PREDICTION")
      print("Predicted value:",prediction[0][0])


if __name__ == "__main__":
      main()
