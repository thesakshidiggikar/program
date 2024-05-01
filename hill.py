import numpy as np


def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus


def hill_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = np.array(key)
    key_size = len(key)
    plaintext_len = len(plaintext)
    num_blocks = plaintext_len // key_size
    padded_text = plaintext + "X" * (num_blocks * key_size - plaintext_len)
    encrypted_text = ""
    for i in range(0, len(padded_text), key_size):
        block = [ord(char) - ord("A") for char in padded_text[i : i + key_size]]
        block = np.array(block).reshape(-1, 1)
        encrypted_block = (np.dot(key, block) % 26).flatten()
        encrypted_text += "".join([chr(char + ord("A")) for char in encrypted_block])
    return encrypted_text


def hill_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = np.array(key)
    key_inv = matrix_mod_inv(key, 26)
    key_size = len(key)
    decrypted_text = ""
    for i in range(0, len(ciphertext), key_size):
        block = [ord(char) - ord("A") for char in ciphertext[i : i + key_size]]
        block = np.array(block).reshape(-1, 1)
        decrypted_block = (np.dot(key_inv, block) % 26).flatten()
        decrypted_text += "".join([chr(char + ord("A")) for char in decrypted_block])
    return decrypted_text


# Example Usage:
key = [[3, 3], [2, 5]]
plaintext = "HELLO"
encrypted_text = hill_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = hill_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
