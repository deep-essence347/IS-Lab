alphabets = [chr(i) for i in range(ord('A'),ord('Z')+1)]

def tabulate():
	n = len(alphabets)
	tabula = [[] for i in range(0,n)]
	for i in range(0,n):
		tabula[i] = [alphabets[(i+j)%n] for j in range(0,n)]
	return tabula

def keyGen(text,key):
	newKey = key
	for i in range(len(key),len(text)):
		newKey += key[i%len(key)]
	return newKey

def encrypt(text,key,table):
	encrypted =''
	for i in range(0,len(text)):
		encrypted += table[alphabets.index(key[i])][alphabets.index(text[i])]
	return encrypted

def decrypt(encoded,key,table):
	decrypted = ''
	for i in range(0,len(encoded)):
		row = table[alphabets.index(key[i])]
		decrypted += alphabets[row.index(encoded[i])]
	return decrypted

if __name__ == "__main__":
	text = 'KATHMANDUUNIVERSITY'
	key = "COMPUTER"
	
	table = tabulate()
	updatedKey = keyGen(text,key)
	
	print('Original Text: ', text)
	print('Key:', key)
	
	encryptedText = encrypt(text,updatedKey,table)
	decryptedText = decrypt(encryptedText,updatedKey,table)
	
	print('Encrypted Text: ',encryptedText)
	print('Decrypted Text: ',decryptedText)
