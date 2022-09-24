from encrypt import alphabet, length


# vice versa but the only change is we need to subtract te shift number with the index number
def decrypt(message, shift):
    cipher_text = []
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter) - shift
            if index < 0:
                index %= length
            cipher_text += alphabet[index]
        else:
            cipher_text += letter
    print(f"Here's the Decoded result: {''.join(cipher_text)}")
