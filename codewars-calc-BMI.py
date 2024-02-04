def bmi(weight, height):
    bmi_result = weight / height ** 2
    if bmi_result <= 18.5:
        return "Underweight"
    elif bmi_result <= 25.0:
        return "Normal"
    elif bmi_result <= 30.0:
        return "Overweight"
    else:
        return "Obese"