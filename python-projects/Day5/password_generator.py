# Create a password generator"
#number_generator = [str(i) for i in range(10)]
# print(number_generator)

# letters_generator = [chr(i) for i in range(65, 91) + [chr(i) for i in range(91, 123)]]
# print(letters_generator)

import random

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', ';', ':', '?']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to Password Generator!")
pwd_letters = int(input("How many letters do you want in your password: \n"))
pwd_nums = int(input("How many numbers do you want: \n"))
pwd_symbols = int(input(f"How many symbols: \n"))

# password = ""
# for char in range(0, pwd_letters):
#     password += random.choice(letters)

# for char in range(0, pwd_nums):
#     password += random.choice(numbers)

# for char in range(0, pwd_symbols):
#     password += random.choice(symbols)

# print(f"Here is your unique password:\n {password}")

###################### Using Shuffle library ######################
# Reshuffle the password output. Add the new passwords to a list instead of a string
password_list = []

for char in range(0, pwd_letters):
    password_list += random.choice(letters)

for char in range(0, pwd_nums):
    password_list += random.choice(numbers)

for char in range(0, pwd_symbols):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

# Then turn the reshuffed password to a string
password = ""
for char in password_list:
    password += char
print(f"Here is your unique password:\n {password}")
