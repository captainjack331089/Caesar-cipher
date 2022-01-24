alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_number, direction):
    if direction == "decode":
        shift_number *= -1
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_postion = position + shift_number
            result += alphabet[new_postion]
        else:
            result += letter
    return result

from art import logo
print(logo)

status = 1
while status:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_input = input("Type your message:\n")

    shift_number = int(input("Type the shift number:\n"))
    shift_number = shift_number % 26

    result = caesar(user_input, shift_number, direction)
    print(f"Here's the encoded result: {result}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == 'no':
        print('Goodbye.')
        status = 0
