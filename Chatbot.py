# DIABETES CHAT BOT Only answers diabetes related questions
#created by DZUNISANI MABUNDA
# line 71 MAIN CHAT LOOP
# from line 19 calculate  weight in kg, height in meters
#line 82  Check if it's diabetes related
# line 88 Try to auto-detect weight and height for BMI
  # line 93 very simple extraction
# line 100 check if they typed 175 not 1.75

def is_diabetes_question(question):
    question = question.lower()
    keywords = [
        "diabetes", "diabetic", "sugar", "glucose", "bmi", 
        "insulin", "food", "diet", "symptom", "symptoms",
        "blood sugar", "type 1", "type 2", "cause", "prevent",
        "weight", "obesity", "carbs", "sweet", "fruits"
    ]
    for word in keywords:
        if word in question:
            return True
    return False

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal - Good for diabetes prevention"
    elif bmi < 30:
        status = "Overweight - Higher risk for diabetes"
    else:
        status = "Obese - High risk for diabetes"
    return f"Your BMI is {bmi:.1f} - {status}"

def get_answer(question):
    q = question.lower()

    if "bmi" in q:
        return """To calculate BMI, I need your weight and height.
Example: type 'my weight is 80kg and height 1.75m'
Formula: BMI = weight(kg) / height(m)²
Normal BMI (18.5-24.9) helps prevent diabetes."""

    if "food" in q or "eat" in q or "cause" in q:
        return """Foods that can increase sugar/diabetes risk if eaten too much:
- Sugary drinks (Coke, juice, energy drinks)
- White bread, white rice, pap, vetkoek
- Sweets, biscuits, cakes
- Fast food, fried foods, fatty meat

Good foods for prevention:
- Brown rice, whole wheat, oats
- Vegetables, beans, lentils
- Lean chicken, fish
- Water instead of sugary drinks"""

    if "symptom" in q:
        return """Common symptoms of diabetes/sugar diabetes:
- Always thirsty
- Peeing a lot
- Always tired
- Blurry vision
- Wounds heal slowly
- Tingling in hands/feet
If you have these, please see a clinic/doctor."""

    if "sugar" in q or "diabetes" in q:
        return """Diabetes is when your blood sugar is too high.
Type 1: Body doesn't make insulin
Type 2: Common type, caused by lifestyle, diet, overweight.
You can prevent Type 2 by healthy eating, exercise, and keeping normal BMI."""

    return """I can help with diabetes, sugar, BMI, foods, and symptoms.
Ask me e.g: 'What foods cause diabetes?' or 'Calculate my BMI'"""

print("Diabetes Chat Bot is ready (type 'exit' to stop)")
print("Ask me about BMI, foods, sugar, diabetes symptoms...\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Stay healthy! Remember to check your sugar.")
        break


    if not is_diabetes_question(user_input):
        print("Bot: Sorry, I only answer questions about diabetes, sugar, BMI, foods and symptoms.")
        continue

    
    if "kg" in user_input.lower() and "m" in user_input.lower():
        try:
            
            parts = user_input.lower().replace("kg"," ").replace("m"," ").split()
            nums = [float(s) for s in parts if s.replace('.','',1).isdigit()]
            if len(nums) >= 2:
                weight = nums[0]
                height = nums[1]
                if height > 3:
                    height = height/100
                print(f"Bot: {calculate_bmi(weight, height)}")
                continue
        except:
            pass

    answer = get_answer(user_input)
    print(f"Bot: {answer}\n")