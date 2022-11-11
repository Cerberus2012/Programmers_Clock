# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2032, 1082)
        MainWindow.setStyleSheet("*{\n"
"    background-color: #2A2E32;\n"
"    border: None;\n"
"}\n"
"QFrame#analog_clock_frame{\n"
"    border: 1px solid white;\n"
"    border-radius: 4px;\n"
"}\n"
"QFrame#binary_clock_frame{\n"
"    border: 1px solid white;\n"
"    border-radius: 4px;\n"
"}\n"
"QFrame#hex_clock_frame{\n"
"    border: 1px solid white;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_window_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_window_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_window_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_window_frame.setObjectName("main_window_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.main_window_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.analog_clock_frame = QtWidgets.QFrame(self.main_window_frame)
        self.analog_clock_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analog_clock_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analog_clock_frame.setObjectName("analog_clock_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.analog_clock_frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.analog_clock_frame)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.analog_clock_frame_contents = QtWidgets.QFrame(self.analog_clock_frame)
        self.analog_clock_frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analog_clock_frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analog_clock_frame_contents.setObjectName("analog_clock_frame_contents")
        self.verticalLayout_12.addWidget(self.analog_clock_frame_contents)
        self.gridLayout.addWidget(self.analog_clock_frame, 0, 0, 2, 1)
        self.hex_clock_frame = QtWidgets.QFrame(self.main_window_frame)
        self.hex_clock_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hex_clock_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hex_clock_frame.setObjectName("hex_clock_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.hex_clock_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.hex_clock_frame_contents = QtWidgets.QFrame(self.hex_clock_frame)
        self.hex_clock_frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hex_clock_frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hex_clock_frame_contents.setObjectName("hex_clock_frame_contents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.hex_clock_frame_contents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hex_clock_label = QtWidgets.QLabel(self.hex_clock_frame_contents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.hex_clock_label.setFont(font)
        self.hex_clock_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hex_clock_label.setObjectName("hex_clock_label")
        self.verticalLayout_8.addWidget(self.hex_clock_label)
        self.hex_clock_time_frame = QtWidgets.QFrame(self.hex_clock_frame_contents)
        self.hex_clock_time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hex_clock_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hex_clock_time_frame.setObjectName("hex_clock_time_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.hex_clock_time_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hex_clock_hours_frame = QtWidgets.QFrame(self.hex_clock_time_frame)
        self.hex_clock_hours_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hex_clock_hours_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hex_clock_hours_frame.setObjectName("hex_clock_hours_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.hex_clock_hours_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hex_clock_hours_label = QtWidgets.QLabel(self.hex_clock_hours_frame)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.hex_clock_hours_label.setFont(font)
        self.hex_clock_hours_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hex_clock_hours_label.setObjectName("hex_clock_hours_label")
        self.verticalLayout_4.addWidget(self.hex_clock_hours_label)
        self.horizontalLayout.addWidget(self.hex_clock_hours_frame)
        self.hex_clock_semicolon_frame = QtWidgets.QFrame(self.hex_clock_time_frame)
        self.hex_clock_semicolon_frame.setMinimumSize(QtCore.QSize(50, 0))
        self.hex_clock_semicolon_frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.hex_clock_semicolon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hex_clock_semicolon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hex_clock_semicolon_frame.setObjectName("hex_clock_semicolon_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.hex_clock_semicolon_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hex_clock_semicolon_label = QtWidgets.QLabel(self.hex_clock_semicolon_frame)
        font = QtGui.QFont()
        font.setPointSize(41)
        self.hex_clock_semicolon_label.setFont(font)
        self.hex_clock_semicolon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hex_clock_semicolon_label.setObjectName("hex_clock_semicolon_label")
        self.verticalLayout_3.addWidget(self.hex_clock_semicolon_label)
        self.horizontalLayout.addWidget(self.hex_clock_semicolon_frame)
        self.hex_clock_minutes_frame = QtWidgets.QFrame(self.hex_clock_time_frame)
        self.hex_clock_minutes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hex_clock_minutes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hex_clock_minutes_frame.setObjectName("hex_clock_minutes_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.hex_clock_minutes_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.hex_clock_minutes_label = QtWidgets.QLabel(self.hex_clock_minutes_frame)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.hex_clock_minutes_label.setFont(font)
        self.hex_clock_minutes_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hex_clock_minutes_label.setObjectName("hex_clock_minutes_label")
        self.verticalLayout_10.addWidget(self.hex_clock_minutes_label)
        self.horizontalLayout.addWidget(self.hex_clock_minutes_frame)
        self.verticalLayout_8.addWidget(self.hex_clock_time_frame)
        self.verticalLayout_11.addWidget(self.hex_clock_frame_contents, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.hex_clock_frame, 0, 1, 1, 1)
        self.binary_clock_frame = QtWidgets.QFrame(self.main_window_frame)
        self.binary_clock_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binary_clock_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.binary_clock_frame.setObjectName("binary_clock_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.binary_clock_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.binary_clock_frame_contents = QtWidgets.QFrame(self.binary_clock_frame)
        self.binary_clock_frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binary_clock_frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.binary_clock_frame_contents.setObjectName("binary_clock_frame_contents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.binary_clock_frame_contents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.binary_clock_label = QtWidgets.QLabel(self.binary_clock_frame_contents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.binary_clock_label.setFont(font)
        self.binary_clock_label.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_clock_label.setObjectName("binary_clock_label")
        self.verticalLayout_9.addWidget(self.binary_clock_label)
        self.binary_clock_time_frame = QtWidgets.QFrame(self.binary_clock_frame_contents)
        self.binary_clock_time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binary_clock_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.binary_clock_time_frame.setObjectName("binary_clock_time_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.binary_clock_time_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.binary_clock_hours_frame = QtWidgets.QFrame(self.binary_clock_time_frame)
        self.binary_clock_hours_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binary_clock_hours_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.binary_clock_hours_frame.setObjectName("binary_clock_hours_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.binary_clock_hours_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.binary_clock_hours_label = QtWidgets.QLabel(self.binary_clock_hours_frame)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.binary_clock_hours_label.setFont(font)
        self.binary_clock_hours_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.binary_clock_hours_label.setObjectName("binary_clock_hours_label")
        self.verticalLayout_5.addWidget(self.binary_clock_hours_label)
        self.horizontalLayout_2.addWidget(self.binary_clock_hours_frame)
        self.binary_clock_semicolon_frame = QtWidgets.QFrame(self.binary_clock_time_frame)
        self.binary_clock_semicolon_frame.setMinimumSize(QtCore.QSize(50, 0))
        self.binary_clock_semicolon_frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.binary_clock_semicolon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binary_clock_semicolon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.binary_clock_semicolon_frame.setObjectName("binary_clock_semicolon_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.binary_clock_semicolon_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.binary_clock_semicolon_label = QtWidgets.QLabel(self.binary_clock_semicolon_frame)
        font = QtGui.QFont()
        font.setPointSize(41)
        self.binary_clock_semicolon_label.setFont(font)
        self.binary_clock_semicolon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_clock_semicolon_label.setObjectName("binary_clock_semicolon_label")
        self.verticalLayout_6.addWidget(self.binary_clock_semicolon_label)
        self.horizontalLayout_2.addWidget(self.binary_clock_semicolon_frame)
        self.binary_clock_minutes_frame = QtWidgets.QFrame(self.binary_clock_time_frame)
        self.binary_clock_minutes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binary_clock_minutes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.binary_clock_minutes_frame.setObjectName("binary_clock_minutes_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.binary_clock_minutes_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.binary_clock_minutes_label = QtWidgets.QLabel(self.binary_clock_minutes_frame)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.binary_clock_minutes_label.setFont(font)
        self.binary_clock_minutes_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.binary_clock_minutes_label.setObjectName("binary_clock_minutes_label")
        self.verticalLayout_7.addWidget(self.binary_clock_minutes_label)
        self.horizontalLayout_2.addWidget(self.binary_clock_minutes_frame)
        self.verticalLayout_9.addWidget(self.binary_clock_time_frame)
        self.verticalLayout_2.addWidget(self.binary_clock_frame_contents, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.binary_clock_frame, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.main_window_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Zero Indexed Analog Clock"))
        self.hex_clock_label.setText(_translate("MainWindow", "Hex Clock"))
        self.hex_clock_hours_label.setText(_translate("MainWindow", "<hours>"))
        self.hex_clock_semicolon_label.setText(_translate("MainWindow", ":"))
        self.hex_clock_minutes_label.setText(_translate("MainWindow", "<minutes>"))
        self.binary_clock_label.setText(_translate("MainWindow", "Binary Clock"))
        self.binary_clock_hours_label.setText(_translate("MainWindow", "<hours>"))
        self.binary_clock_semicolon_label.setText(_translate("MainWindow", ":"))
        self.binary_clock_minutes_label.setText(_translate("MainWindow", "<minutes>"))