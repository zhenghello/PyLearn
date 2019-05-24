# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyLearn\BpyQt\d190523_addOne3\addOne.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addOne(object):
    def setupUi(self, addOne):
        addOne.setObjectName("addOne")
        addOne.resize(246, 287)
        self.verticalLayout = QtWidgets.QVBoxLayout(addOne)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(addOne)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(addOne)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_end = QtWidgets.QPushButton(addOne)
        self.pushButton_end.setObjectName("pushButton_end")
        self.verticalLayout.addWidget(self.pushButton_end)

        self.retranslateUi(addOne)
        self.pushButton_end.clicked.connect(addOne.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(addOne)

    def retranslateUi(self, addOne):
        _translate = QtCore.QCoreApplication.translate
        addOne.setWindowTitle(_translate("addOne", "自加一"))
        self.label.setText(_translate("addOne", "显示"))
        self.pushButton.setText(_translate("addOne", "加1"))
        self.pushButton_end.setText(_translate("addOne", "结束"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addOne = QtWidgets.QWidget()
    ui = Ui_addOne()
    ui.setupUi(addOne)
    addOne.show()
    sys.exit(app.exec_())

