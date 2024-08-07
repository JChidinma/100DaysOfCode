from caesar_art import caesar_art

print(f"Welcome to your CAESAR CIPHER game!\n{caesar_art}")

# TODO - 5 -  What if a user enters a number/symbol/space that is not listed in the alphabets? Can you handle this casein order to keep the numbers/symbols/space when the text is encoded or decoded?


def caesar(original_text, shift_amount, encode_or_decode):
    received_cipher_letter = ""

    for letter in original_text:
        if letter not in alphabet:
            received_cipher_letter += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            received_cipher_letter += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {received_cipher_letter}")


should_continue = True

while should_continue:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input(
        "Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text = str(input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input(
        "Type 'Y' if you want to try again. Otherwise, type 'N'.\n").lower()


# TODO - 6 - Restart the program if the user want to try again
    if restart == "n":
        should_continue = False
        print("Goodbye!")
