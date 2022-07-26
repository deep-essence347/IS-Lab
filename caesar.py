def encrypt(t, s):
    encrypted = ''
    for i in range(len(t)):
        a = t[i]
        encrypted += chr(ord(a)+3)
    return encrypted

def decrypt(e,s):
    decrypted = ''
    for i in range(len(e)):
        a = e[i]
        decrypted += chr(ord(a)-3)
    return decrypted

if __name__ == "__main__":
    text = "Kathmandu University"
    shift = 3

    print('Original Text: ', text)

    encryptedText = encrypt(text,shift)
    decryptedText = decrypt(encryptedText,shift)

    print('Encrypted Text: ',encryptedText)
    print('Decrypted Text: ',decryptedText)