def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        shift = ord(key[i % key_length].upper()) - 65
        if plaintext[i].isalpha():
            encrypted_text += chr((ord(plaintext[i].upper()) + shift - 65) % 26 + 65)
        else:
            encrypted_text += plaintext[i]
    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        shift = ord(key[i % key_length].upper()) - 65
        if ciphertext[i].isalpha():
            decrypted_text += chr((ord(ciphertext[i].upper()) - shift - 65) % 26 + 65)
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text


# Example Usage:
plaintext = "Hello, World!"
key = "KEY"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
