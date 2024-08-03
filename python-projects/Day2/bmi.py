height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")

weight_as_float = float(weight)
height_as_float = float(height)
BMI = weight_as_float / (height_as_float ** 2)
BMI = round(BMI)  # Round the BMI to 2 decimal places
# print(f"Your body-mass index is: {BMI}")


if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
