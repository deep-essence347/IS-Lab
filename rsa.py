import string

def encrypt(message,n,e):
    encrypted = [-1 for i in message]

    for i in range(0,len(message)):
        index = alphabets.index(message[i])
        encrypted[i] = (index**e)%n

    return encrypted

def decrypt(encrypted,n, d):
    decrypted = ''
    for i in range(0, len(encrypted)):
        val = (encrypted[i]**d)%n 
        decrypted +=alphabets[val]
    return decrypted

alphabets = string.ascii_uppercase
p = 7
q = 11
n = p*q
phi_n = (p-1) * (q-1)
e = 17

d = 1
while True:
    val = (e*d)%phi_n
    if(val == 1):
        break
    else:
        d+=1

message = "HELLO"

encrypted = encrypt(message,n,e)
decrypted = decrypt(encrypted,n,d)

print('Encrypted',encrypted)
print('Decrypted',decrypted)