def get_recommendation(prediction: int) -> str:
    disclaimer = (
        "\n\nDISCLAIMER: This tool is created for educational and school project "
        "purposes only. It does not provide medical diagnoses and should not replace "
        "professional medical advice, diagnosis, or treatment."
    )

    if prediction == 0:
        output = (
            "[RESULT] Predicted Class: No-Diabetes (0)\n"
            "• The model classified the provided information into the no-diabetes class.\n"
            "• Recommendation: Maintain a balanced diet, stay physically active, "
            "and keep up with routine general health check-ups."
        )
    elif prediction == 1:
        output = (
            "[RESULT] Predicted Class: Diabetes/Prediabetes (1)\n"
            "• The model classified the provided information into the diabetes/prediabetes class.\n"
            "• Recommendation: Consider consulting a qualified healthcare professional "
            "for appropriate screening and medical guidance."
        )
    else:
        raise ValueError(
            f"Invalid prediction value '{prediction}' supplied. Expected 0 or 1."
        )

    return output + disclaimer


if __name__ == "__main__":
    print("Testing Prediction 0:")
    print(get_recommendation(0))

    print("\n" + "=" * 60 + "\n")

    print("Testing Prediction 1:")
    print(get_recommendation(1))
