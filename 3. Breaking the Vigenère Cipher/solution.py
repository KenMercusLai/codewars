from itertools import cycle

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHER = "CODEWARS"


def get_keyword(ciphertext, key_len):
    splitted_ciphertext = [
        ciphertext[i : i + key_len] for i in range(0, len(ciphertext), key_len)
    ]
    print(splitted_ciphertext)

    for i in splitted_ciphertext:
        for j, v in enumerate(i):
            new_index = ALPHABET.index(v) - ALPHABET.index(CIPHER[j])
            if new_index < 0:
                new_index += 26
            print(
                ALPHABET[new_index],
            )
    return
