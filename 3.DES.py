import time
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
print(key)
des = DES.new(key,DES.MODE_ECB)

#input text should be multiple of 8
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def dataEncryptionStandard(text,des):
    padded_text = pad(text.encode())

    start_time = time.time()
    encrypted_text = des.encrypt(padded_text)
    print("---Encryptin Time: %s seconds ---" % round((time.time() - start_time),2))
    start_time = time.time()
    d_text = des.decrypt(encrypted_text)
    print("---Decryption Time: %s seconds ---" % round((time.time() - start_time),2))


#from sys import getsizeof
#print(getsizeof(text))


ls = ['MB100.txt','MB500.txt','MB1000.txt']

for i in ls:
    f=open(i, 'r')
    text = f.read()
    dataEncryptionStandard(text,des)
    f.close()
