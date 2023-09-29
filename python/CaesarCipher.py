# We need the alphabet coz we convert letters into numerical values
# to be able to use math-ops (note we encrypt the spaces as well)
ALPHABET = " !ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3


def caesar_encrypt(plain_text):
    # encrypte message
    cipher_text = ""
    # we make the algorithm case insensitive
    plain_text = plain_text.upper()

    # consider all the letters in the plain_text
    for c in plain_text:
        # find the numerical representation (index) associated with the letter
        index = ALPHABET.find(c)
        # Caesar encryption is just a simple shift of characters according
        # to the key use modular arithmetic to transform the values within
        # the range [0, num_of_letters_in_alphabet]
        index = (index + KEY) % len(ALPHABET)
        # keep appending the encrypted character to the cipher_text
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def caesar_decrypt(cipher_text):
    # decrypted message
    plain_text = ""

    # consider all the letters in the cipher_text
    for c in cipher_text:
        index = ALPHABET.find(c)

        index = (index - KEY) % len(ALPHABET)
        # keep appending the encrypted character to the plain_text
        plain_text = plain_text + ALPHABET[index]

    return plain_text


if __name__ == "__main__":
    m = "Welcome to my Udemy course!"
    encrypted = caesar_encrypt(m)
    print(encrypted)
    print(caesar_decrypt(encrypted))
