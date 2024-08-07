import random

hangman_word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_word_list)
print(chosen_word)
placeholder = len(chosen_word) * "_"
print(placeholder)

# TODO -1 - Use a while loop to let the user guess again
game_over = False

while not game_over:
    guess = str(input("Type a letter: ")).lower()
    print(guess)

    display = ""
# TODO -2 - Change the for loop so that you keep the previous correct guesses added to the display String. At the moment, when the user makes a new guess, the previous guess gets replaced by a"_". Fix that by updating the for loop.


for char in chosen_word:
    if guess == char:
        display += char
        # print(display)
        # print("Right")
    else:
        display += "_"
        # print(display)
        # print("Wrong")
print(display)
