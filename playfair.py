def playfair(text, key, decrypt=False):
    def create_matrix(key):
        print("Key before sorting:", key)
        key = "".join(sorted(set(key.replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ")))
        print("Sorted key:", key)
        return [list(key[i : i + 5]) for i in range(0, 25, 5)]

    def find_coords(matrix, char):
        return [
            (r, c)
            for r, row in enumerate(matrix)
            for c, val in enumerate(row)
            if val == char
        ]

    def process_pair(matrix, a, b):
        (a_row, a_col), (b_row, b_col) = find_coords(matrix, a), find_coords(matrix, b)
        if a_row == b_row:
            return (
                matrix[a_row][(a_col + (-1 if decrypt else 1)) % 5]
                + matrix[b_row][(b_col + (-1 if decrypt else 1)) % 5]
            )
        elif a_col == b_col:
            return (
                matrix[(a_row + (-1 if decrypt else 1)) % 5][a_col]
                + matrix[(b_row + (-1 if decrypt else 1)) % 5][b_col]
            )
        else:
            return matrix[a_row][b_col] + matrix[b_row][a_col]

    text = text.replace("J", "I").replace(" ", "").upper()
    matrix = create_matrix(key)
    processed_text = ""
    for i in range(0, len(text), 2):
        processed_text += process_pair(matrix, text[i], text[i + 1])
    return processed_text


# Example Usage:
key = "playfair example"
plaintext = "Hide the gold in the tree stump"
encrypted_text = playfair(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = playfair(encrypted_text, key, decrypt=True)
print("Decrypted:", decrypted_text)
