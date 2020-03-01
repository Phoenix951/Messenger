import requests
import clientui
from PyQt5 import QtWidgets, QtCore
from datetime import datetime

class MessangerWindow(QtWidgets.QMainWindow, clientui.Ui_Messanger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_message_time = 0
        self.pushButton.pressed.connect(self.sendMessage)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)

    def sendMessage(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()

        if not username:
            self.addText("ERROR: username is empty.")
            return
        if not password:
            self.addText("ERROR: password is empty.")
            return

        response = requests.post(
            "http://127.0.0.1:5000/send",
            json={"username": username, "password": password, "text": text}
        )
        if not response.json()["ok"]:
            self.addText("ERROR: Access denied")
            return

        if not text:
            self.addText("ERROR: text is empty.")

        self.textEdit.clear()
        self.textEdit.repaint()

    def addText(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

    def getUpdates(self):
        response = requests.get(
            "http://127.0.0.1:5000/history",
            params={"after": self.last_message_time}
        )
        data = response.json()
        for message in data["messages"]:
            beuty_time = datetime.fromtimestamp(message["time"])
            beuty_time = beuty_time.strftime("%Y/%m/%d %H:%M:%S")
            self.addText(beuty_time + " " + message["username"])
            self.addText(message["text"])
            self.addText("")
            self.last_message_time = message["time"]


app = QtWidgets.QApplication([])
window = MessangerWindow()
window.show()
app.exec_()
