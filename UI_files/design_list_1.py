# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desing_list_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1452, 756)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(60, 60, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.state_1 = QtWidgets.QPushButton(self.centralwidget)
        self.state_1.setEnabled(False)
        self.state_1.setGeometry(QtCore.QRect(60, 170, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.state_1.setFont(font)
        self.state_1.setCheckable(False)
        self.state_1.setObjectName("state_1")
        self.state_2 = QtWidgets.QPushButton(self.centralwidget)
        self.state_2.setEnabled(False)
        self.state_2.setGeometry(QtCore.QRect(60, 230, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.state_2.setFont(font)
        self.state_2.setObjectName("state_2")
        self.state_3 = QtWidgets.QPushButton(self.centralwidget)
        self.state_3.setEnabled(False)
        self.state_3.setGeometry(QtCore.QRect(60, 290, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.state_3.setFont(font)
        self.state_3.setObjectName("state_3")
        self.state_4 = QtWidgets.QPushButton(self.centralwidget)
        self.state_4.setEnabled(False)
        self.state_4.setGeometry(QtCore.QRect(60, 350, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.state_4.setFont(font)
        self.state_4.setObjectName("state_4")
        self.state_5 = QtWidgets.QPushButton(self.centralwidget)
        self.state_5.setEnabled(False)
        self.state_5.setGeometry(QtCore.QRect(60, 410, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.state_5.setFont(font)
        self.state_5.setObjectName("state_5")
        self.state_6 = QtWidgets.QPushButton(self.centralwidget)
        self.state_6.setEnabled(False)
        self.state_6.setGeometry(QtCore.QRect(60, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.state_6.setFont(font)
        self.state_6.setObjectName("state_6")
        self.runRecognitionButton = QtWidgets.QPushButton(self.centralwidget)
        self.runRecognitionButton.setEnabled(False)
        self.runRecognitionButton.setGeometry(QtCore.QRect(60, 610, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.runRecognitionButton.setFont(font)
        self.runRecognitionButton.setObjectName("runRecognitionButton")
        self.midiSettButton = QtWidgets.QPushButton(self.centralwidget)
        self.midiSettButton.setEnabled(False)
        self.midiSettButton.setGeometry(QtCore.QRect(340, 610, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.midiSettButton.setFont(font)
        self.midiSettButton.setObjectName("midiSettButton")
        self.runMidiButtom = QtWidgets.QPushButton(self.centralwidget)
        self.runMidiButtom.setEnabled(False)
        self.runMidiButtom.setGeometry(QtCore.QRect(520, 610, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.runMidiButtom.setFont(font)
        self.runMidiButtom.setObjectName("runMidiButtom")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(1180, 140, 201, 451))
        self.textEdit_3.setObjectName("textEdit_3")
        self.devSettButton = QtWidgets.QPushButton(self.centralwidget)
        self.devSettButton.setEnabled(False)
        self.devSettButton.setGeometry(QtCore.QRect(1180, 60, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.devSettButton.setFont(font)
        self.devSettButton.setObjectName("devSettButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 60, 891, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.y_scale_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.y_scale_combo_box.setEnabled(False)
        self.y_scale_combo_box.setGeometry(QtCore.QRect(710, 20, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.y_scale_combo_box.setFont(font)
        self.y_scale_combo_box.setObjectName("y_scale_combo_box")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.y_scale_combo_box.addItem("")
        self.x_scale_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.x_scale_combo_box.setEnabled(False)
        self.x_scale_combo_box.setGeometry(QtCore.QRect(960, 20, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.x_scale_combo_box.setFont(font)
        self.x_scale_combo_box.setObjectName("x_scale_combo_box")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        self.x_scale_combo_box.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Neurotrone music"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.state_1.setText(_translate("MainWindow", "State 1"))
        self.state_2.setText(_translate("MainWindow", "State 2"))
        self.state_3.setText(_translate("MainWindow", "State 3"))
        self.state_4.setText(_translate("MainWindow", "State 4"))
        self.state_5.setText(_translate("MainWindow", "State 5"))
        self.state_6.setText(_translate("MainWindow", "State 6"))
        self.runRecognitionButton.setText(_translate("MainWindow", "Run\n"
"recognition"))
        self.midiSettButton.setText(_translate("MainWindow", "MIDI\n"
"settings"))
        self.runMidiButtom.setText(_translate("MainWindow", "Run MIDI"))
        self.devSettButton.setText(_translate("MainWindow", "Device settings"))
        self.y_scale_combo_box.setCurrentText(_translate("MainWindow", "1 uV/mm"))
        self.y_scale_combo_box.setItemText(0, _translate("MainWindow", "1 uV/mm"))
        self.y_scale_combo_box.setItemText(1, _translate("MainWindow", "2 uV/mm"))
        self.y_scale_combo_box.setItemText(2, _translate("MainWindow", "5 uV/mm"))
        self.y_scale_combo_box.setItemText(3, _translate("MainWindow", "7 uV/mm"))
        self.y_scale_combo_box.setItemText(4, _translate("MainWindow", "10 uV/mm"))
        self.y_scale_combo_box.setItemText(5, _translate("MainWindow", "15 uV/mm"))
        self.y_scale_combo_box.setItemText(6, _translate("MainWindow", "20 uV/mm"))
        self.y_scale_combo_box.setItemText(7, _translate("MainWindow", "25 uV/mm"))
        self.y_scale_combo_box.setItemText(8, _translate("MainWindow", "30 uV/mm"))
        self.y_scale_combo_box.setItemText(9, _translate("MainWindow", "60 uV/mm"))
        self.y_scale_combo_box.setItemText(10, _translate("MainWindow", "65 uV/mm"))
        self.y_scale_combo_box.setItemText(11, _translate("MainWindow", "70 uV/mm"))
        self.y_scale_combo_box.setItemText(12, _translate("MainWindow", "100 uV/mm"))
        self.y_scale_combo_box.setItemText(13, _translate("MainWindow", "125 uV/mm"))
        self.y_scale_combo_box.setItemText(14, _translate("MainWindow", "200 uV/mm"))
        self.y_scale_combo_box.setItemText(15, _translate("MainWindow", "350 uV/mm"))
        self.y_scale_combo_box.setItemText(16, _translate("MainWindow", "500 uV/mm"))
        self.y_scale_combo_box.setItemText(17, _translate("MainWindow", "750 uV/mm"))
        self.y_scale_combo_box.setItemText(18, _translate("MainWindow", "1000 uV/mm"))
        self.x_scale_combo_box.setItemText(0, _translate("MainWindow", "1 mm/sec"))
        self.x_scale_combo_box.setItemText(1, _translate("MainWindow", "2 mm/sec"))
        self.x_scale_combo_box.setItemText(2, _translate("MainWindow", "5 mm/sec"))
        self.x_scale_combo_box.setItemText(3, _translate("MainWindow", "7 mm/sec"))
        self.x_scale_combo_box.setItemText(4, _translate("MainWindow", "10 mm/sec"))
        self.x_scale_combo_box.setItemText(5, _translate("MainWindow", "15 mm/sec"))
        self.x_scale_combo_box.setItemText(6, _translate("MainWindow", "20 mm/sec"))
        self.x_scale_combo_box.setItemText(7, _translate("MainWindow", "25 mm/sec"))
        self.x_scale_combo_box.setItemText(8, _translate("MainWindow", "30 mm/sec"))
        self.x_scale_combo_box.setItemText(9, _translate("MainWindow", "60 mm/sec"))
        self.x_scale_combo_box.setItemText(10, _translate("MainWindow", "65 mm/sec"))
        self.x_scale_combo_box.setItemText(11, _translate("MainWindow", "70 mm/sec"))
        self.x_scale_combo_box.setItemText(12, _translate("MainWindow", "100 mm/sec"))
        self.x_scale_combo_box.setItemText(13, _translate("MainWindow", "150 mm/sec"))