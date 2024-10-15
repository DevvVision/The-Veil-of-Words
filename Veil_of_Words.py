from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import pyautogui as pag
import socket
import os
import subprocess
import pyautogui as pag
import threading
from PyQt6 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def decrypt_data(self,encrypted_text):
        # Decode the Base64 encoded encrypted data
        encrypted_data = b64decode(encrypted_text)

        # Extract the key, IV, and ciphertext from the decoded data
        key = encrypted_data[:16]  # The first 16 bytes are the key
        iv = encrypted_data[16:32]  # The next 16 bytes are the IV
        cipher_text = encrypted_data[32:]  # The remaining bytes are the ciphertext

        # Recreate the cipher object using the key and IV
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)

        # Decrypt the ciphertext
        plain_text = cipher.decrypt(cipher_text).decode('utf-8')
        return plain_text

    def sendMsg(self):
        try:
            send = self.messageInput.text()
            self.messageInput.setText("")
            send = self.name + ": " + send
            self.s.send(send.encode("utf-8"))
        except Exception as e:
            print("Exception occured or disconnected ")
            # self.sendMsg()
    def recving(self):
        while True:
            try:
                dt = str(self.s.recv(1024), 'utf-8')
                print(dt)
                self.chatDisplay.append(dt)
            except Exception as e:
                print("Error")
    def setupUi(self, MainWindow):
        self.s = socket.socket()
        self.host = self.decrypt_data(str(pag.password(text='Enter the Room Pass Key :I', title='Pass Key', default='Randi', mask='*')))
        self.port = 9999
        self.s.connect((self.host, self.port))
        thr1 = threading.Thread(target=self.recving)
        thr1.start()

        self.name =pag.prompt(text='Enter Alias', title='Alias : Anonymous name' , default="Psycho_"+str(random.randint(1,100000000))+"_Killer")
        self.s.send(self.name.encode('utf-8'))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 606)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messageInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.messageInput.setGeometry(QtCore.QRect(180, 500, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(-1)
        self.messageInput.setFont(font)
        self.messageInput.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.messageInput.setStyleSheet("QLineEdit{\n"
"                    padding: 6px 12px;\n"
"                    background: rgb(31, 32, 35);\n"
"                    border: 1px solid rgb(60, 63, 68);\n"
"                    border-radius: 4px;\n"
"                    font-size: 20px;\n"
"                    color: rgb(247, 248, 248);\n"
"                    height: 46px;\n"
"                    appearance: none;\n"
"                    transition: border 0.15s ease 0s;\n"
"}\n"
"                    QLineEdit:focus{\n"
"                        outline: none;\n"
"                        box-shadow: none;\n"
"                        border-color: rgb(100, 153, 255);\n"
"                    }\n"
"                ")
        self.messageInput.setObjectName("messageInput")
        self.sendButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(820, 490, 111, 61))
        self.sendButton.setStyleSheet("\n"
"\n"
"\n"
"\n"
"    QPushButton {\n"
"      background-color:rgb(121,82,179); color:white; border-radius:3px; font-weight:bold; height:36px; width:120px; border:none; margin-top:5px; margin-right:10px; \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: gray;\n"
"                color: white;\n"
"                cursor:pointer;\n"
"            }")
        self.sendButton.setObjectName("sendButton")
        self.connDisplay = QtWidgets.QListWidget(parent=self.centralwidget)
        self.connDisplay.setGeometry(QtCore.QRect(0, 120, 181, 431))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.connDisplay.setFont(font)
        self.connDisplay.setStyleSheet("                   padding: 6px 12px;\n"
"                   background: rgb(31, 32, 35);\n"
"                    border: 1px solid rgb(60, 63, 68);\n"
"                    border-radius: 4px;")
        self.connDisplay.setObjectName("connDisplay")
        self.chatScroll = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.chatScroll.setGeometry(QtCore.QRect(890, 0, 21, 501))
        self.chatScroll.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.chatScroll.setObjectName("chatScroll")
        self.connScroll = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.connScroll.setGeometry(QtCore.QRect(160, 120, 21, 431))
        self.connScroll.setStyleSheet("")
        self.connScroll.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.connScroll.setObjectName("connScroll")
        self.LOGO = QtWidgets.QLabel(parent=self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(0, 0, 181, 121))
        self.LOGO.setStyleSheet("                color: #FFFFFF;\n"
"                background-color: #1E1E1E;\n"
"                border: 2px solid #4A4A4A;\n"
"                border-radius: 2px;\n"
"                padding: 10px;")
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap("../../../../Downloads/logo.jpg"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setObjectName("LOGO")
        self.chatDisplay = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.chatDisplay.setGeometry(QtCore.QRect(180, 0, 711, 501))
        self.chatDisplay.setStyleSheet("QTextEdit {\n"
"color: rgba(255, 255, 255, 1.0);          /* White text with 90% opacity */\n"
"background-color: rgba(30, 30, 30, 0.05);\n"
"border:rgba(30, 30, 30, 0.5);\n"
"border-radius: 15px;\n"
"font-size:25px;\n"
"\n"
"                    background: rgb(31, 32, 35);\n"
"                    border: 1px solid rgb(60, 63, 68);\n"
"                    border-radius: 4px;\n"
"                    font-size: 20px;\n"
"                    color: rgb(247, 248, 248);\n"
"                    height: 46px;\n"
"                    appearance: none;\n"
"                    transition: border 0.15s ease 0s;\n"
"}\n"
"")
        self.chatDisplay.setObjectName("chatDisplay")
        self.chatDisplay.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.sendButton.clicked.connect(self.sendMsg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.messageInput.setPlaceholderText(_translate("MainWindow", "What\'s Up XD "))
        self.sendButton.setText(_translate("MainWindow", "SEND"))
        self.sendButton.setShortcut(_translate("MainWindow", "Return"))
        self.chatDisplay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
