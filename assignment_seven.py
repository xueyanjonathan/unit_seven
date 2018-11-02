# Jonathan Lin
# 11/02/2018
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
    text_converted = ""
    for x in range(len(text_two)):
        number = alphabet.index(text_two[x])
        number_key = alphabet.index(keyword_two[x % len(keyword_two)])
        converted_number = number + number_key
        text_converted = text_converted + alphabet[converted_number % 26]
    print(text_converted)


def decode():
    text = input("Please enter text to be decoded:")
    keyword = input("Please enter the key string:")
    keyword_two = keyword.lower().replace(" ", "")  # All letters are made lowercase and all spaces are eliminated.
    text_converted = ""  # 
    for x in range(len(text)):
        number = alphabet.index(text[x])
        number_key = alphabet.index(keyword_two[x % len(keyword_two)])
        converted_number = number - number_key
        text_converted = text_converted + alphabet[converted_number % 26]
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



