# 1. Create a greeting for your program
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:

greeting = "Welcome to your band name generator! Let's get going."
city_name = input("Enter the name of the city you grew up in?\n")
pet_name = input(
    "Enter your pet name if you have one or make up a cool name:\n")

print(greeting)
print(city_name)
print(pet_name)

print("Your Band Name could be " + city_name + " " + pet_name + "!")
