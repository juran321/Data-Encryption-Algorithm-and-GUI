import random

class Crypto(object):
    def __init__(self):
        self.key = []

    # set a previously generated key from file
    def SetKey(self, keyfilename):
        list = []
        for i in range(0,8,2):
            list.append(keyfilename[i : i + 2])

        firstKey = []
        for element in list:
            firstKey.append(int(element,16))
        firstBinaryKey = ""

        for key in firstKey:
            firstBinaryKey += '{0:08b}'.format(key)
        secondBinKey = firstBinaryKey[::-1]
        secondKey = []
        for i in range(0, 32, 8):
            secondKey.append(int(secondBinKey[i: i + 8], 2))

        self.key.append(firstKey)
        self.key.append(secondKey)
        return self.key


    def Encrypt(self,text):
        list = []
        for i in range(0, len(text),4):
            list.append(text[i:i + 4])
        res = ""
        for s in list:
            text = []
            for i in range(len(s)):
                text.append(ord(s[i]))
            for i in range(len(text)):
                text[i] = text[i] ^ self.key[0][i] ^ self.key[1][i]
            for i in range(len(text)):
                res += '{0:x}'.format(int(text[i])).zfill(2)
        return res

    def UnEncrypt(self, content):
        content = content.strip()
        text = []
        for i in range(0, len(content), 8):
            text.append(content[i: i + 8])
        decode = ""
        for s in text:
            textDec = []
            for i in range(0, len(s), 2):
                textDec.append(int(s[i: i + 2], 16))
            for i in range(len(textDec)):
                textDec[i] = textDec[i] ^ self.key[1][i] ^ self.key[0][i]

            for i in range(len(textDec)):
                decode += chr(textDec[i])

        return decode

    def GenerateKey(self):
        key = random.sample(range(0, 255), 4)
        newKey = ""
        for i in range(len(key)):
            newKey += '{0:x}'.format(int(key[i])).zfill(2)
        return newKey