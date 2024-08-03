height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")

weight_as_float = float(weight)
height_as_float = float(height)
BMI = weight_as_float / (height_as_float ** 2)
BMI = round(BMI)  # Round the BMI to 2 decimal places
print(f"Your body-mass index is: {BMI}")
