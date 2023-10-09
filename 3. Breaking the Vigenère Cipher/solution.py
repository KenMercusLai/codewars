from itertools import cycle

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_keyword(ciphertext, key_len):
    splited_ciphertext = [ciphertext[i:i+key_len] for i in range(0, len(ciphertext), key_len)]
    print(splited_ciphertext)
    return
