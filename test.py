
from Crypto import *
p = Crypto()

(p.SetKey('0d48fa23'))
print(p.UnEncrypt('9d729be7'))

key1 = p.GenerateKey()
key2 = p.GenerateKey()
key3 = p.GenerateKey()
print (key1)
print (key2)
print (key3)