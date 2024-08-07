import random
from hangman_art import hangman_stages_art
from hangman_words import words

hangman_word_list = []
hangman_word_list.extend(words)
# print(hangman_word_list)

chosen_word = random.choice(hangman_word_list)
print(chosen_word)
placeholder = len(chosen_word) * "_"
print(placeholder)


# TODO -1 - Create a variable called "lives" to keep track of the number of lives left. Set lives to equal 6.
lives = 6
print(f"You have {lives} lives left")
game_over = False
correct_guessed_letters = []

while not game_over:
    guess = str(input("Type a letter: ")).lower()
    print(guess)
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed {guess}, that's not a letter in the word. \nYou have {lives} lives left.")
        if lives == 0:
            print("You lost!!")

    display = ""
    # TODO -2 - If guess is not a letter in the chosen_word, then reduce lives by 1.
    # If lives goes down to 0, then the game should end and it should print("You lose!")

    for char in chosen_word:
        if guess == char:
            display += char
            correct_guessed_letters.append(guess)
        elif char in correct_guessed_letters:
            display += char
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")

    # TODO -3 - Print the ASCII art from the list "stages" that corresponds to the current Numberof lives the user has remaining.
    print(hangman_stages_art[lives])
