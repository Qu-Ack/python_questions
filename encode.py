str = "this is a test"


def encode(str):
    """
    encodes the string by adding 9 to the ascii value of the character
    """
    result = ""
    for character in str:
        result += chr(ord(character) + 9)
    return result


def decode(str):
    """
    decodes the string by subtracting 9 from the ascii value of the character
    """
    result = ""
    for character in str:
        result += chr(ord(character) - 9)
    return result


encoded_str = encode(str)
print(encoded_str)
print(encode.__doc__)
decoded_str = decode(encoded_str)
print(decode.__doc__)
print(decoded_str)
