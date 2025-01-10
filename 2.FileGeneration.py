import random,string

f = open('MB25.txt','w+')
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (25*1024*1024))) 
f.write(key)
f.close()

f = open('MB50.txt','w+')
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (50*1024*1024))) 
f.write(key)
f.close()

f = open('MB75.txt','w+')
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (75*1024*1024))) 
f.write(key)
f.close()

f = open('MB100.txt','w+')
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (100*1024*1024))) 
f.write(key)
f.close()

f = open('MB500.txt','w+')
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (500*1024*1024))) 
f.write(key)
f.close()

f = open('MB1000.txt','w+')
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (1000*1024*1024))) 
f.write(key)
f.close()