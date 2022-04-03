# Exercise 1: Creating a user-defined function
def get_double_alphabet(alphabet):
    double_alphabet = alphabet + alphabet
    return double_alphabet

# Exercise 2: Encrypting a message
def get_message(): 
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt

# Exercise 3: Getting a cipher key
def get_cipher_key():
    shift_amount = input("Please enter a key (whole number from 1-25): ")
    return shift_amount

# Exercise 4: Encrypting a message
def encrypt_message(message, cipherKey, alphabet):
    encrypted_message = ""
    uppercase_message = ""
    uppercase_message = message.upper()
    for current_character in uppercase_message:
        position = alphabet.find(current_character)
        new_position = position + int(cipherKey)
        if current_character in alphabet:
            encrypted_message = encrypted_message + alphabet[new_position]
        else:
            encrypted_message = encrypted_message + current_character
    return encrypted_message

# Exercise 5: Decrypting a message
def decrypt_message(message, cipher_key, alphabet):
    decrypt_key = -1 * int(cipher_key)
    return encrypt_message(message, decrypt_key, alphabet)

# Exercise 6: Create a main function
def runCaesarCipherProgram():
    my_alphabet1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet 1: {my_alphabet1}')
    my_alphabet2 = get_double_alphabet(my_alphabet1)
    print(f'Alphabet 2: {my_alphabet2}')
    my_message = get_message()
    print(my_message)
    my_cipher_key = get_cipher_key()
    print(my_cipher_key)
    my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet2)
    print(f'Encrypted Message: {my_encrypted_message}')
    my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet2)
    print(f'Decypted Message: {my_decrypted_message}')

runCaesarCipherProgram()