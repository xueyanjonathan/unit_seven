# Jonathan Lin
# 11/06/2018
# The Vigenére Cipher
# Modifying strings

alphabet = "abcdefghijklmnopqrstuvwxyz"  # The string to indicate the places of letters in texts and keywords


def encode():
    """
    This function receives input from the user, and saves the keyword(password).
    It will use the alphabet to get numerical values for each letter in the list and keyword.
    The values of the letters in the key and the text are added together to get the values for the ciphertext.
    The function then uses the alphabet again to convert the values in the ciphertext back to
    letters they correspond to.
    :return: Nothing
    """
    text = input("Please enter text to be encoded:")
    keyword = input("Please enter the key string:")
    text_two = text.lower().replace(" ", "")
    keyword_two = keyword.lower().replace(" ", "")
    text_converted = ""  # Create a blank list to be ready to be put numbers in
    for x in range(len(text_two)):
        # According to the length of the text,
        # if during the addition the keyword is shorter than the text, it will repeat itself.
        number = alphabet.index(text_two[x])  # Get the letters' values in the text
        number_key = alphabet.index(keyword_two[x % len(keyword_two)])  # Get the letters' values in keyword
        converted_number = number + number_key
        text_converted = text_converted + alphabet[converted_number % 26]
        # Convert the numbers back to letters.
        # If the sum in addition is over 26, the remainder from dividing 26 will be the value to be converted.
    print(text_converted)


def decode():
    text = input("Please enter text to be decoded:")
    keyword = input("Please enter the key string:")
    keyword_two = keyword.lower().replace(" ", "")
    text_converted = ""  # Create a blank list to be ready to be put numbers in
    for x in range(len(text)):
        # According to the length of the text,
        # if during the subtraction the keyword is shorter than the text, it will repeat itself.
        number = alphabet.index(text[x])  # Get the letters' values in the text
        number_key = alphabet.index(keyword_two[x % len(keyword_two)])  # Get the letters' values in keyword
        converted_number = number - number_key
        text_converted = text_converted + alphabet[converted_number]
        # Convert the numbers back to letters.
        # If the product in subtraction is over 26, the remainder from dividing 26 will be the value to be converted.
    print(text_converted)


def main():
    while True:
        user_input = input("Press e to encode, d to decode, or q to quit:")
        if user_input == "e":
            encode()
        elif user_input == "d":
            decode()
        elif user_input == "q":
            print("Thanks for playing.")
            break
        else:
            print("Please enter the correct command.")


main()
