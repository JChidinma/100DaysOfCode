# Write a Tip Calculator program

# 1. Ask the user what their total bill is
# 2. How much tip would they like to give?
# 3. How many people are splitting the bill?
# 4. Return a message that shows how much each person will pay

print("Welcome to your Tip Calculator!")
bill = float(input("What is the total bill? "))
number_of_friends = int(input("How many people are splitting the bill? "))
tip_percent = int(input("What percentage tip would you like to give? "))

bill_as_float = float(bill)

tip = (bill / number_of_friends) * (1 + (tip_percent / 100))
print(round(tip))
