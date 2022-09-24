alphabet = ["v", "f", "g", "h", "i", "j", "a", "z", "e", "b", "c", "d", "x", "y", "l", "m", "n", "o", "u", "k", "w",
            "p", "q", "r", "s", "t"]
length = len(alphabet)


def encrypt(message, shift):
    cipher_text = ""
    for letter in message:
        # we need to check the message if the letter is present or not
        if letter in alphabet:
            # and then add the shift number with the index number of the letter
            index = alphabet.index(letter) + shift
            # if the index is more than the length of the alphabet then
            # we need to divide with the length of the alphabet
            if index >= length:
                index %= length
                # then we need to add the letter to the string
            cipher_text += alphabet[index]
        # if the string contain number or !@# then it will not encrypt that exact character
        else:
            cipher_text += letter

    print(f"Here's the Encoded result: {cipher_text}")
