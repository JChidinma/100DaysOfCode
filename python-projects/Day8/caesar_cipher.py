alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                      'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

############################# ENCRYPT STANDALONE #############################
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift'
# hello 2
# def encrypt(original_text, shift_amount):
#     # print(shift)

#     # TODO-2 - Inside the 'encrypt' function, shift each letter of the original_text' forwards in the alphabet by the shift amount and print the encrypted text. Use index library to find the position of an item in a list. E.g. fruits = ["orange", "apple", "pear"]. fruits.index("pear"). If we have the following values: plain_text - "hello" and shift_amount = 1, the final encrypted output should be: "Here is the encoded result: 'ifmmp'"
#     # TODO - 3 Call the 'encrypt()' function and pass in the user inputs. You shoull
#     # TODO -  4 What happens if you try to shift z forwards by 9? Can you fix the code?
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount  # h=7 + 2
#         shifted_position %= len(alphabet)  # 0 - 25
#         cipher_text += alphabet[shifted_position]  # j
#     print(f"Here is the encoded result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)

############################# DECRYPT STANDALONE #########################################

# def decrypt(original_text, shift_amount):
#     # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift'
#     # TODO-2 - Inside the 'decrypt' function, shift each letter of the original_text' backwards in the alphabet by the shift amount and print the encrypted text.
#     received_cipher_letter = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         received_cipher_letter += alphabet[shifted_position]
#     print(f"Here is the decoded result: {received_cipher_letter}")
# TODO - 3 Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
# Use the value of the user chosen direction variable to determine which functionaity to use.
# Call the 'caesar() function instead of encrypt/decrypt and pass in all the variables direction/text/shift.

# decrypt(original_text=text, shift_amount=shift)

##################### COMBINED ENCRYPT AND DECRYPT #############################


def caesar(original_text, shift_amount, encode_or_decode):
    received_cipher_letter = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        received_cipher_letter += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {received_cipher_letter}")


caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
