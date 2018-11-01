alphabet = "abcdefghijklmnopqrstuvwxyz"


def encode():
    text = input("Please enter text to be encoded: ")
    keyword = input("Please enter the key string: ")
    text_two = text.lower().replace(" ", "")
    keyword_two = keyword.lower()
    text_converted = ""
    for x in range(len(text_two)):
        number = alphabet.index(text_two[x])
        number_key = alphabet.index(keyword_two[x % len(keyword_two)])
        converted_number = number + number_key
        text_converted = text_converted + alphabet[converted_number % 26]
    print(text_converted)
 