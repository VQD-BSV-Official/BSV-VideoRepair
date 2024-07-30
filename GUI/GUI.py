# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 301, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border-radius: 5px; border: 1px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 301, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setAccessibleDescription("")
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("border-radius: 5px; border: 1px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.b_Select = QtWidgets.QPushButton(parent=self.groupBox)
        self.b_Select.setGeometry(QtCore.QRect(320, 20, 91, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.b_Select.setFont(font)
        self.b_Select.setObjectName("b_Select")
        self.b_Select_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.b_Select_2.setGeometry(QtCore.QRect(320, 50, 91, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.b_Select_2.setFont(font)
        self.b_Select_2.setObjectName("b_Select_2")
        self.label_Copyright = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Copyright.setGeometry(QtCore.QRect(10, 320, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.label_Copyright.setFont(font)
        self.label_Copyright.setText("")
        self.label_Copyright.setObjectName("label_Copyright")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(440, 19, 181, 291))
        self.listWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.listWidget.setObjectName("listWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 421, 211))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.progressBar = QtWidgets.QProgressBar(parent=self.groupBox_2)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 180, 411, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 20)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 401, 151))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 629, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(parent=self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHome = QtWidgets.QMenu(parent=self.menuBar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.repair = QtGui.QAction(parent=MainWindow)
        self.repair.setObjectName("repair")
        self.actionClear = QtGui.QAction(parent=MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHome.addAction(self.actionClear)
        self.menuHome.addAction(self.repair)
        self.menuBar.addAction(self.menuHome.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BSV Video Repair"))
        self.groupBox.setTitle(_translate("MainWindow", "Browse Path"))
        self.lineEdit.setText(_translate("MainWindow", "                      Corrupted/Encrypted Folder"))
        self.lineEdit_2.setText(_translate("MainWindow", "                              Repaired Folder"))
        self.b_Select.setText(_translate("MainWindow", "Select"))
        self.b_Select_2.setText(_translate("MainWindow", "Select"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Logs"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.repair.setText(_translate("MainWindow", "Advanced Repair"))
        self.repair.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
