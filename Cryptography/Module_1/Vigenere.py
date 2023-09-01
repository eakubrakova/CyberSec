import itertools as it
import functools as ft

ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, it.cycle(key))
    result = ''

    for pair in pairs:
        total = ft.reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()

 
def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, it.cycle(key))
    result = ''

    for pair in pairs:
        total = ft.reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print('Key: %s' % key)
    print('Plaintext: %s' % plaintext)
    print('Encrytped: %s' % encrypted)
    print('Decrytped: %s' % decrypted)