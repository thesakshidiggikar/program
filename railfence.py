# def cipher(s, key, graph=False):
#     down = True
#     raw_out = []
#     out = ""
#     i = 0
#     for x in range(key):
#         raw_out.append({})
#     for pos in range(len(s)):
#         raw_out[i][pos] = s[pos]
#         if i == key - 1:
#             down = False
#         if i == 0:
#             down = True
#         if down:
#             i = i + 1
#         else:
#             i = i - 1
#     for p in raw_out:
#         for q in p:
#             out += p[q]
#     if graph:
#         return raw_out
#     return out


# def decipher(s, key):
#     map_list = cipher(
#         s, key, True
#     )  # CREATING JUST FOR MAPPING - WHICHth CHARACTER OF THE STRING - IS WHICHth CHARACTER OF THE CIPHER
#     new = {}
#     out = ""
#     s_counter = 0
#     for x in map_list:
#         for y in x:
#             new[y] = s[s_counter]
#             s_counter += 1
#     for p in new:
#         out += new[p]
#     return map_list
# _____________________________________________________________________
def rail_fence_cipher(text, key, encrypt=True):
    if encrypt:
        return (
              "".join(text[i] for i in range(len(text)) if i % (2 * key - 2) == 0)
            + "".join(text[i] for i in range(len(text)) if i % (2 * key - 2) == 1)
            + "".join(text[i] for i in range(len(text)) if i % (2 * key - 2) > 1 and i % (2 * key - 2) < key)
            + "".join(text[i] for i in range(len(text)) if i % (2 * key - 2) >= key)
        )
    else:
        order = sorted(
            range(len(text)),
            key=lambda i: (
                i // (key - 1)
                if i % (2 * key - 2) == 0
                else (
                    (key - 1) - i % (key - 1)
                    if i % (2 * key - 2) >= key
                    else 2 * (i // (key - 1)) + 1
                )
            ),
        )
        return "".join(text[order.index(i)] for i in range(len(text)))


# Example Usage:
plaintext = "Hello, World!"
key = 3
encrypted_text = rail_fence_cipher(plaintext, key, encrypt=True)
print("Encrypted:", encrypted_text)
decrypted_text = rail_fence_cipher(encrypted_text, key, encrypt=False)
print("Decrypted:", decrypted_text)
