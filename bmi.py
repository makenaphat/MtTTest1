def calculate_bmi(weight, height):
    # Formula: Weight (kg) / Height (m)^2
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 23:
        return "Normal Weight / Healthy"
    elif 23 <= bmi < 25:
        return "Overweight / Obesity Level 0"
    elif 25 <= bmi < 30:
        return "Obese / Obesity Level 1"
    else:
        return "Severely Obese / Obesity Level 2"

# Get user input
try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))

    bmi_result = calculate_bmi(weight, height)
    category = interpret_bmi(bmi_result)

    print(f"\nYour BMI is: {bmi_result:.2f}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numbers.")