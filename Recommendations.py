def get_recommendation(prediction: int) -> str:
    """
    Produces simple informational output for prediction 0 or 1,
    including a non-diagnostic disclaimer.
    """
    # Non-diagnostic disclaimer required for the project
    disclaimer = (
        "\n\nDISCLAIMER: This tool is created for educational and school project "
        "purposes only. It does not provide medical diagnoses and should not replace "
        "professional medical advice, diagnosis, or treatment."
    )
    
    if prediction == 0:
        output = (
            "Prediction Result: Low Risk / Negative (0)\n"
            "• Your model output suggests a lower risk level.\n"
            "• Recommendation: Maintain a balanced diet, stay physically active, "
            "and keep up with routine general health check-ups."
        )
    elif prediction == 1:
        output = (
            "Prediction Result: Potential Risk / Positive (1)\n"
            "• Your model output suggests indicators associated with diabetes risk.\n"
            "• Recommendation: Consult a qualified healthcare professional or doctor "
            "for proper screening, diagnosis, and medical guidance."
        )
    else:
        output = "Invalid prediction value supplied. Expected 0 or 1."
        
    return output + disclaimer

# Optional: Quick test block to verify functionality when run directly
if __name__ == "__main__":
    print("Testing Prediction 0:")
    print(get_recommendation(0))
    print("\n" + "="*50 + "\n")
    print("Testing Prediction 1:")
    print(get_recommendation(1))