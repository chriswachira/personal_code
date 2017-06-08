"""
    - UI Program to generate Kenyan phone numbers 
    - Uses the numgen module functionality to generate numbers
"""
__author__ = "Chris Wachira"
__maintainer__ = "chriskane816@gmail.com"
__version__ = 0.1
__status__ = "Prototype"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from numgen import PhoneNumber

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 465)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 4, 1, 1)

        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 10, 2, 1, 2)
        self.lblCarrierSelect = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)

        self.lblCarrierSelect.setFont(font)
        self.lblCarrierSelect.setObjectName("lblCarrierSelect")
        self.gridLayout.addWidget(self.lblCarrierSelect, 3, 0, 1, 3)
        self.pledtNums = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pledtNums.setObjectName("pledtNums")
        self.gridLayout.addWidget(self.pledtNums, 3, 5, 8, 1)

        self.cmbCarrier = QtWidgets.QComboBox(self.centralwidget)
        self.cmbCarrier.setObjectName("cmbCarrier")
        self.gridLayout.addWidget(self.cmbCarrier, 4, 0, 1, 4)

        self.lblSearch = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblSearch.setFont(font)
        self.lblSearch.setObjectName("lblSearch")
        self.gridLayout.addWidget(self.lblSearch, 6, 0, 1, 1)

        self.radioOn = QtWidgets.QRadioButton(self.centralwidget)
        self.radioOn.setObjectName("radioOn")
        self.gridLayout.addWidget(self.radioOn, 6, 1, 1, 2)

        self.radioOff = QtWidgets.QRadioButton(self.centralwidget)
        self.radioOff.setObjectName("radioOff")
        self.gridLayout.addWidget(self.radioOff, 6, 3, 1, 1)

        self.ledtNumSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtNumSearch.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ledtNumSearch.setFont(font)
        self.ledtNumSearch.setObjectName("ledtNumSearch")
        self.gridLayout.addWidget(self.ledtNumSearch, 7, 0, 1, 4)

        self.lblNumCheck = QtWidgets.QLabel(self.centralwidget)
        self.lblNumCheck.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblNumCheck.setFont(font)
        self.lblNumCheck.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNumCheck.setObjectName("lblNumCheck")
        self.gridLayout.addWidget(self.lblNumCheck, 8, 0, 1, 4)

        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 10, 0, 1, 2)

        self.lblAuthor = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblAuthor.setFont(font)
        self.lblAuthor.setObjectName("lblAuthor")
        self.gridLayout.addWidget(self.lblAuthor, 1, 5, 1, 1)

        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 1, 0, 1, 3)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnStop.setText(_translate("MainWindow", "STOP"))
        self.lblCarrierSelect.setText(_translate("MainWindow", "Select Carrier:"))
        self.lblSearch.setText(_translate("MainWindow", "Search:"))
        self.radioOn.setText(_translate("MainWindow", "O&N"))
        self.radioOff.setText(_translate("MainWindow", "OFF"))
        self.lblNumCheck.setText(_translate("MainWindow", "TextLabel"))
        self.btnStart.setText(_translate("MainWindow", "START"))
        self.lblAuthor.setText(_translate("MainWindow", "by Chris Wachira   </chriskane816@gmail.com>"))
        self.lblTitle.setText(_translate("MainWindow", "NumGEN_KE"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    window.move(QtWidgets.QApplication.desktop().screen().rect().center() - window.rect().center())
    sys.exit(app.exec_())