import time
from Crypto.Hash import SHA512

h = SHA512.new()


ls = ['MB100.txt','MB500.txt','MB1000.txt']

for i in ls:
    f=open(i, 'r')
    text = f.read()
    start_time = time.time()
    h.update(text.encode())
    print(h.digest())
    print("--- %s seconds ---" % round((time.time() - start_time),2))
    f.close()
