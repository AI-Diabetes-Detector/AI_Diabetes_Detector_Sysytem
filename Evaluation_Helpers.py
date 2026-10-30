from sklearn.metrics import accuracy_score


def confusion_matrix_values(actual_values, predicted_values):
    tn = 0
    fp = 0
    fn = 0
    tp = 0

    for actual, predicted in zip(actual_values, predicted_values):
        if actual == 0 and predicted == 0:
            tn += 1
        elif actual == 0 and predicted == 1:
            fp += 1
        elif actual == 1 and predicted == 0:
            fn += 1
        elif actual == 1 and predicted == 1:
            tp += 1

    return tn, fp, fn, tp


def calculate_precision(tp, fp):
    if tp + fp == 0:
        return 0

    return tp / (tp + fp)


def calculate_recall(tp, fn):
    if tp + fn == 0:
        return 0

    return tp / (tp + fn)


def evaluate_model(model_name, actual_values, predicted_values):
    accuracy = accuracy_score(actual_values, predicted_values)

    tn, fp, fn, tp = confusion_matrix_values(
        actual_values,
        predicted_values
    )

    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)

    print("\n" + "=" * 60)
    print(model_name)
    print("=" * 60)

    print("Accuracy:", accuracy * 100, "%")
    print("Confusion Matrix:")
    print([[tn, fp], [fn, tp]])
    print("True Negatives:", tn)
    print("False Positives:", fp)
    print("False Negatives:", fn)
    print("True Positives:", tp)
    print("Precision:", precision)
    print("Recall:", recall)
