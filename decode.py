from Crypto import *

f = open('My_Key.txt', 'r')
key = f.read(8)
f.close()

pCr = Crypto()
pCr.SetKey(key)

infile = open('Secret.enc', 'r')
outfile = open('Answer.txt', 'w')

for line in infile:
    decrptLine = pCr.UnEncrypt(line)
    print(decrptLine.strip())
    outfile.write(decrptLine)

infile.close()
outfile.close()