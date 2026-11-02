from sklearn import linear_model
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from data_preparation import load_data, prepare_data, show_data_information
from evaluate_models import evaluate_model


def train_logistic_regression(X_train, y_train):
    classifier = linear_model.LogisticRegression(
        solver="liblinear",
        C=75
    )
    classifier.fit(X_train, y_train)
    return classifier


def train_decision_tree(X_train, y_train):
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    return classifier


def train_random_forest(X_train, y_train):
    classifier = RandomForestClassifier(
        n_estimators=50,
        random_state=0
    )
    classifier.fit(X_train, y_train)
    return classifier


def main():
    data = load_data()

    show_data_information(data)

    X_train, X_test, y_train, y_test = prepare_data(data)

    print("\nTraining rows:", len(X_train))
    print("Testing rows:", len(X_test))

    logistic_regression = train_logistic_regression(
        X_train,
        y_train
    )

    logistic_predictions = logistic_regression.predict(X_test)

    evaluate_model(
        "LOGISTIC REGRESSION",
        y_test,
        logistic_predictions
    )

    decision_tree = train_decision_tree(
        X_train,
        y_train
    )

    decision_tree_predictions = decision_tree.predict(X_test)

    evaluate_model(
        "DECISION TREE",
        y_test,
        decision_tree_predictions
    )

    random_forest = train_random_forest(
        X_train,
        y_train
    )

    random_forest_predictions = random_forest.predict(X_test)

    evaluate_model(
        "RANDOM FOREST",
        y_test,
        random_forest_predictions
    )

    print("\nRANDOM FOREST TRAINING AND TESTING ACCURACY")
    print(
        "Training accuracy:",
        random_forest.score(X_train, y_train) * 100,
        "%"
    )
    print(
        "Testing accuracy:",
        random_forest.score(X_test, y_test) * 100,
        "%"
    )


if __name__ == "__main__":
    main()
