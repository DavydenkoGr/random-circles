import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 484)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Желтые окружности"))
        self.pushButton.setText(_translate("Form", "Нарисовать"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.rep)
        self.cp = False

    def rep(self):
        self.cp = True
        self.repaint()

    def paintEvent(self, event):
        if self.cp:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()

    def run(self, qp):
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        n = randint(20, 250)
        qp.drawEllipse(278 - n // 2, 278 - n // 2 , n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())