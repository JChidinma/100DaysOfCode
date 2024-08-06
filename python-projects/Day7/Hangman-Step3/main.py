import random

hangman_word_list = ["aardvark", "baboon", "camel"]

# TODO -1 - Randomly choose a word from the hangman_word_list and assign it to a variable called chosen_word. Then print it.
# TODO -2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO -3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.

chosen_word = random.choice(hangman_word_list)
print(chosen_word)
guess = str(input("Type a letter: ")).lower()

for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")
