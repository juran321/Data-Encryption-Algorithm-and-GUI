'''
Ran Ju Final Project, CSEG 505
This program is the GUI that can generate key,
decode/encode what I what
'''
import sys
from PyQt5.QtWidgets import *
from Crypto import *

class CryptoTool(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - self.size().width()) / 2
        y = (screen.height() - self.size().height()) / 2
        self.x = x
        self.y = y
        self.move(x, y)
        self.setWindowTitle("Crypto Tool")

        label_1 = QLabel('Key file:', self)
        label_1.setMaximumWidth(100)
        label_1.setMinimumWidth(100)

        label_2 = QLabel('Source File:', self)
        label_2.setMaximumWidth(100)
        label_2.setMinimumWidth(100)

        self.text_1 = QLineEdit(self)
        self.text_2 = QLineEdit(self)
        self.text_1.setReadOnly(True)
        self.text_2.setReadOnly(True)

        self.button_1 = QPushButton("browse", self)
        self.button_1.clicked.connect(self.getfiles1)
        self.button_2 = QPushButton("browse", self)
        self.button_2.clicked.connect(self.getfiles2)
        self.button_3 = QPushButton("encode",self)
        self.button_3.clicked.connect(self.encode)

        self.button_4 = QPushButton("decode", self)
        self.button_4.clicked.connect(self.decode)
        self.button_5 = QPushButton("generate key",self)
        self.button_5.clicked.connect(self.file_save)

        self.text_3 = QLineEdit(self)
        self.text_3.setText("Key:")
        self.text_3.setReadOnly(True)
        self.text_4 = QLineEdit(self)
        self.text_4.setText("Encrypted/Decryted source text")
        self.text_4.setReadOnly(True)
        self.content_1 = QTextEdit(self)
        self.content_2 = QTextEdit(self)
        self.content_1.setReadOnly(True)
        self.content_2.setReadOnly(True)
        self.content_2.setFontFamily('courier')
        self.content_1.setFontFamily('courier')
        self.text_5 = QLineEdit(self)
        self.text_5.setText("Decryted/Encrted text")
        self.key =""
        self.text = ""
        self.keyfile = ""
        self.code = ""

        lyt1 = QHBoxLayout()
        lyt1.addWidget(label_1)
        lyt1.addWidget(self.text_1)
        lyt1.addWidget(self.button_1)

        lyt2 = QHBoxLayout()
        lyt2.addWidget(label_2)
        lyt2.addWidget(self.text_2)
        lyt2.addWidget(self.button_2)

        lyt4 = QHBoxLayout()
        lyt4.addWidget(self.button_3)
        lyt4.addWidget(self.button_4)
        lyt4.addWidget(self.button_5)

        lyt3 = QVBoxLayout()
        lyt3.addLayout(lyt1)
        lyt3.addLayout(lyt2)
        lyt3.addLayout(lyt4)
        lyt3.addWidget(self.text_3)
        lyt3.addWidget(self.text_4)
        lyt3.addWidget(self.content_1)
        lyt3.addWidget(self.text_5)
        lyt3.addWidget(self.content_2)

        self.setLayout(lyt3)
        self.setMinimumSize(700,400)

    def getfiles1(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open a File', '', '*.txt')
        if fileName == "":
            self.text_1.setText("")
        else:
            self.text_1.setText(fileName)
            file = open(fileName, 'r')
            self.keyfile = fileName
            text = ""
            for line in file:
                text += line
            self.key = text
            self.text_3.setText("Key: "+text)

    def getfiles2(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open a File',  '', '*.enc;;*.txt')
        if fileName == "":
            self.text_2.setText("")
        else:
            self.text_2.setText(fileName)
            self.content_1.setText(open(fileName,'r').read())

    #function on decode button
    def decode(self):
        if self.text_1.text() == "" or self.text_2.text() == "":
            reply = QMessageBox.information(self,"Error","Please select the key file and source file")
        else:
            self.content_1.clear()
            fileName = self.text_2.text()
            self.code = fileName
            file = open(fileName, 'r')
            text = ""
            for line in file:
                text += line
            self.text = text
            self.content_1.setText(text)
            c = Crypto()
            c.SetKey(self.key)
            infile = open(self.code,'r')
            res = ""
            fileName, _ = QFileDialog.getSaveFileName(self, 'Save the content', '', '*.txt')
            with open(fileName, 'w') as f:
                for i in infile:
                    line = c.UnEncrypt(i)
                    res  += c.UnEncrypt(i)
                f.write(res)
            self.content_2.setText(res)



            # if fileName != "":
            #     with open(fileName, 'w') as f:
            #         f.write(res)




    #function on encode function
    def encode(self):
        if self.text_1.text() == "" or self.text_2.text() == "":
            reply = QMessageBox.information(self,"Error","Please select the key file and source file")
        else:
            c = Crypto()
            key = self.text_1.text()
            keyFile = open(key,'r')
            keyString = ""
            for i in keyFile:
                keyString += i
            c.SetKey(i)
            filename = self.text_2.text()
            file = open(filename,'r')
            res = ""
            fileName, _ = QFileDialog.getSaveFileName(self, 'Save the content', '', '*.enc')
            for j in file:
                res += c.Encrypt(j)+"\r"
            if fileName != "":
                with open(fileName, 'w') as f:
                    f.write(res)

                self.content_2.setText(open(fileName,'r').read())
            #print the content of the text
            fileName = self.text_2.text()
            self.code = fileName
            file = open(fileName, 'r')
            text = ""
            for line in file:
                text += line
            self.text = text
            self.content_1.setText(text)



    def file_save(self):
        fileName, _ = QFileDialog.getSaveFileName(self, 'Generate a new key file', '', '*.txt')
        if fileName != "":
            c = Crypto()
            res = c.GenerateKey()
            with open(fileName,'w') as f:
                f.write(res)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = CryptoTool()
    mw.show()
    sys.exit(app.exec_())
