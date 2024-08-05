# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."

print("The Love Calculator is calculating your score...")
name1 = str(input("What is your name? "))
name2 = str(input("What is their name? "))

join_names = (name1 + name2).lower()

t = join_names.count("t")
r = join_names.count("r")
u = join_names.count("u")
e = join_names.count("e")

true_score = t + r + u + e

l = join_names.count("l")
o = join_names.count("o")
v = join_names.count("v")
e = join_names.count("e")

love_score = l + o + v + e

score = int(str(true_score) + str(love_score))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
