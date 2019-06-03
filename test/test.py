from myPackage.ForuSquare import encrypt, decrypt

if __name__ == '__main__':
    plaintext = 'Lila Lomnicka'

    key = ['example', 'keyword']

    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

    print(decrypt(key, ciphertext))