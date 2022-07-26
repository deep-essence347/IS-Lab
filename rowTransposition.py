def encrypt(text, key):
    text= text.replace(' ','')
    textA = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    encrypted =''
    order = {
        int(val): num for num, val in enumerate(key)
    }
    for i in sorted(order.keys()):
        for j in textA:
            try:encrypted +=j[order[i]]
            except IndexError:
                encrypted +='-'

    return encrypted

if __name__ == "__main__":
    key = "4312567"
    text = 'attack postponed until two am'
    print('Original Text: ',text)
    print('Key: ', key)
    encryptedText = encrypt(text,key)
    print('Encrypted Text: ',encryptedText)