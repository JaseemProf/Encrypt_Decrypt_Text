# Encrypt and Decrypt text
from decrypt import decrypt
from encrypt import encrypt
from logo import logo

print(logo)

is_repeat = True

# it will repeat until the user said no
while is_repeat:
    # we need to get input from the user
    choice = input("Type 'Encode' to encrypt or 'Decode' to decrypt: \n").lower()
    message = input("Type the Message: \n").lower()
    shift = int(input("Type the Shift number:\n"))
    # iif the user type 'encode' then it will call the encode function and vice versa
    if choice == "encode":
        encrypt(message, shift)
    elif choice == "decode":
        decrypt(message, shift)
    # we need to ask user to continue or not
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no':").lower()
    # if the user type 'yes' then it will repeat if 'no' then it will stop
    if repeat == "yes":
        is_repeat = True
    elif repeat == "no":
        is_repeat = False
