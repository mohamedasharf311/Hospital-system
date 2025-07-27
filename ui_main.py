# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainjrzYIE.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

import reso_from_qt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1484, 711)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u";background-color:white;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#tableWidget{\n"
"background-color:white\n"
"}\n"
"\n"
"#pushButton_5, #pushButton_6, #pushButton_7, #pushButton_8, #pushButton_9, #pushButton_10 {\n"
"  position: relative;\n"
"  display: inline-flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  width: 150px;\n"
"  height: 50px; /* Set a fixed height for each button */\n"
"  background: #00abf0;\n"
"  border: 2px solid #00abf0;\n"
"  border-radius: 8px;\n"
"  font-size: 19px;\n"
"  color: #081b29;\n"
"  text-decoration: none;\n"
"  font-weight: 600;\n"
"  letter-spacing: 1px;\n"
"  z-index: 1;\n"
"  overflow: hidden;\n"
"  transition: .5s;\n"
"  align-self: flex-end;\n"
"  margin-bottom: 5px; /* Add some bottom margin to create spacing between buttons */\n"
"}\n"
"\n"
"#pushButton_5:hover, #pushButton_6:hover, #pushButton_7:hover, #pushButton_8:hover, #pushButton_9:hover, #pushButton_10:hover {\n"
"  color: white;\n"
"}\n"
"\n"
"#pushButton_5::before, #pushButton_6::before, #pushButton_7::before, #pushButton_8::before, #pushButton_9::before"
                        ", #pushButton_10::before {\n"
"  content: '';\n"
"  position: absolute;\n"
"  top: 0;\n"
"  left: 0;\n"
"  width: 0;\n"
"  height: 100%;\n"
"  background: #081b29;\n"
"  z-index: -1;\n"
"  transition: .5s;\n"
"}\n"
"\n"
"#pushButton_5:hover::before, #pushButton_6:hover::before, #pushButton_7:hover::before, #pushButton_8:hover::before, #pushButton_9:hover::before, #pushButton_10:hover::before {\n"
"  width: 100%;\n"
"}\n"
"\n"
"\n"
"\n"
"#frame{\n"
"background-image: url(:/newPrefix/D:/pintrest/abu.png);\n"
" background-position: center;\n"
"\n"
"}\n"
"\n"
"\n"
"#lineEdit{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_1{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_2{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit"
                        "_3{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_4{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_5{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_6{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_7{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_8{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_9{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-ra"
                        "dius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_10{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_11{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_12{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"#lineEdit_13{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_14{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_15{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_16{\n"
"  background: #00abf0;\n"
"\n"
"   "
                        " border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_17{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_18{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_19{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#lineEdit_20{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_21{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"#lineEdit_22{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"#lineEdit_2"
                        "3{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"#lineEdit_24{\n"
"  background: #00abf0;\n"
"\n"
"    border: 2px solid #8d371c;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#widget_5 {\n"
"  background: white;\n"
"}\n"
"\n"
"#widget_6 {\n"
"  background:white;\n"
";\n"
"}\n"
"\n"
"#frame{background: url(:/images/D:/pintrest/abu.png)\n"
";}\n"
"\n"
"\n"
"#label,\n"
"#label_1,\n"
"#label_2,\n"
"#label_3,\n"
"#label_5,\n"
"#label_6,\n"
"#label_7,\n"
"#label_8,\n"
"#label_9,\n"
"#label_10,\n"
"#label_11,\n"
"#label_12,\n"
"#label_13,\n"
"#label_14,\n"
"#label_15,\n"
"#label_16,\n"
"#label_17,\n"
"#label_18,\n"
"#label_19,\n"
"#label_20,\n"
"#label_21,\n"
"#label_22,\n"
"#label_23,\n"
"#label_24,\n"
"#label_25,\n"
"#label_26,\n"
"#label_27,\n"
"#label_28,\n"
"#label_29,\n"
"#label_30,\n"
"#label_33,\n"
"#label_34,\n"
"#label_35,\n"
"\n"
"#label_31,\n"
"#label_32 {\n"
"  border: 2px solid black;\n"
"  pad"
                        "ding: 5px 10px;\n"
"  border-radius: 5px;\n"
"}\n"
"#pushButton_11, #pushButton_12, #pushButton_13, #pushButton_14, #pushButton_15 {\n"
"  position: relative;\n"
"  display: inline-flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  width: 150px;\n"
"  height: 50px; /* Set a fixed height for each button */\n"
"  background: #00abf0;\n"
"  border: 2px solid #00abf0;\n"
"  border-radius: 8px;\n"
"  font-size: 19px;\n"
"  color: #081b29;\n"
"  text-decoration: none;\n"
"  font-weight: 600;\n"
"  letter-spacing: 1px;\n"
"  z-index: 1;\n"
"  overflow: hidden;\n"
"  transition: .5s;\n"
"  align-self: flex-end;\n"
"  margin-bottom: 5px; /* Add some bottom margin to create spacing between buttons */\n"
"}\n"
"\n"
"#pushButton_11:hover, #pushButton_12:hover, #pushButton_13:hover, #pushButton_14:hover, #pushButton_15:hover {\n"
"  color: white;\n"
"}\n"
"\n"
"#pushButton_11::before, #pushButton_12::before, #pushButton_13::before, #pushButton_14::before, #pushButton_15::before {\n"
"  content: '';\n"
" "
                        " position: absolute;\n"
"  top: 0;\n"
"  left: 0;\n"
"  width: 0;\n"
"  height: 100%;\n"
"  background: #081b29;\n"
"  z-index: -1;\n"
"  transition: .5s;\n"
"}\n"
"\n"
"#pushButton_11:hover::before, #pushButton_12:hover::before, #pushButton_13:hover::before, #pushButton_14:hover::before, #pushButton_15:hover::before {\n"
"  width: 100%;\n"
"}\n"
"#pushButton_3 {\n"
"  position: relative;\n"
"  display: inline-flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  width: 150px;\n"
"  height: 50px; /* Set a fixed height for each button */\n"
"  background: #00abf0;\n"
"  border: 2px solid #00abf0;\n"
"  border-radius: 8px;\n"
"  font-size: 19px;\n"
"  color: #081b29;\n"
"  text-decoration: none;\n"
"  font-weight: 600;\n"
"  letter-spacing: 1px;\n"
"  z-index: 1;\n"
"  overflow: hidden;\n"
"  transition: .5s;\n"
"  align-self: flex-end;\n"
"  margin-bottom: 5px; /* Add some bottom margin to create spacing between buttons */\n"
"}\n"
"\n"
"#pushButton_3:hover {\n"
"  color: white;\n"
"}\n"
"\n"
"#"
                        "pushButton_3::before {\n"
"  content: '';\n"
"  position: absolute;\n"
"  top: 0;\n"
"  left: 0;\n"
"  width: 0;\n"
"  height: 100%;\n"
"  background: #081b29;\n"
"  z-index: -1;\n"
"  transition: .5s;\n"
"}\n"
"\n"
"#pushButton_3:hover::before {\n"
"  width: 100%;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_top)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_top)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_top, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_5 = QPushButton(self.frame_top_menus)
        self.btn_page_5.setObjectName(u"btn_page_5")
        self.btn_page_5.setMinimumSize(QSize(0, 40))
        self.btn_page_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_5.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.btn_page_5)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cil-calendar-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_4.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.btn_page_4)

        self.btn_page_7 = QPushButton(self.frame_top_menus)
        self.btn_page_7.setObjectName(u"btn_page_7")
        self.btn_page_7.setMinimumSize(QSize(0, 40))
        self.btn_page_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cil-envelope-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_7.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.btn_page_7)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/ser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_2.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_6 = QPushButton(self.frame_top_menus)
        self.btn_page_6.setObjectName(u"btn_page_6")
        self.btn_page_6.setMinimumSize(QSize(0, 40))
        self.btn_page_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_6.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.btn_page_6)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/cil-paperclip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_3.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus)

        self.pushButton_4 = QPushButton(self.frame_left_menu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon9)

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_1)
        self.widget.setObjectName(u"widget")
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 3, 3, 1, 2)

        self.lineEdit_22 = QLineEdit(self.widget)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout.addWidget(self.lineEdit_22, 6, 3, 1, 2)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setPointSize(7)
        self.label_20.setFont(font)
        self.label_20.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_20, 3, 8, 1, 1)

        self.lineEdit_14 = QLineEdit(self.widget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout.addWidget(self.lineEdit_14, 2, 9, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_27, 4, 5, 1, 1)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_26, 3, 5, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_2, 5, 3, 1, 2)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_23, 6, 8, 1, 1)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_22, 5, 8, 1, 1)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(QFont.Bold)
        font1.setStrikeOut(False)
        self.pushButton_7.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_7, 8, 0, 1, 2)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.lineEdit_24 = QLineEdit(self.widget)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout.addWidget(self.lineEdit_24, 6, 9, 1, 1)

        self.lineEdit_18 = QLineEdit(self.widget)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout.addWidget(self.lineEdit_18, 4, 9, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_5, 1, 6, 1, 2)

        self.lineEdit_23 = QLineEdit(self.widget)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout.addWidget(self.lineEdit_23, 3, 6, 1, 2)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_18, 1, 8, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 6, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.widget)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout.addWidget(self.lineEdit_20, 6, 6, 1, 2)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon11)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_8, 8, 7, 1, 2)

        self.lineEdit_15 = QLineEdit(self.widget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout.addWidget(self.lineEdit_15, 5, 6, 1, 2)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.widget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout.addWidget(self.lineEdit_13, 2, 6, 1, 2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_29, 6, 5, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/cil-av-timer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon12)
        self.pushButton_9.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_9, 8, 9, 1, 1)

        self.lineEdit_19 = QLineEdit(self.widget)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout.addWidget(self.lineEdit_19, 5, 9, 1, 1)

        self.lineEdit_21 = QLineEdit(self.widget)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_19, 2, 8, 1, 1)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setIcon(icon10)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_5, 8, 4, 1, 3)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_21, 4, 8, 1, 1)

        self.lineEdit_16 = QLineEdit(self.widget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout.addWidget(self.lineEdit_16, 3, 9, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 2)

        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 4, 3, 1, 2)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 7, 0, 1, 10)

        self.lineEdit_17 = QLineEdit(self.widget)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout.addWidget(self.lineEdit_17, 4, 6, 1, 2)

        self.lineEdit_11 = QLineEdit(self.widget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 2, 3, 1, 2)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_15, 4, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout.addWidget(self.lineEdit_12, 1, 9, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_16, 5, 2, 1, 1)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_24, 1, 5, 1, 1)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)
        self.label_28.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_28, 5, 5, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 1)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_17, 6, 2, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_25, 2, 5, 1, 1)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon13)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_6, 8, 2, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"Aldhabi")
        font2.setPointSize(48)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 5, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_1)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 10, 1061, 501))
        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.formLayout = QFormLayout(self.page_6)
        self.formLayout.setObjectName(u"formLayout")
        self.stackedWidget.addWidget(self.page_6)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(200, 110, 621, 301))
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.btn_page_1.setText("")
        self.btn_page_5.setText("")
        self.btn_page_4.setText("")
        self.btn_page_7.setText("")
        self.btn_page_2.setText("")
        self.btn_page_6.setText("")
        self.btn_page_3.setText("")
        self.pushButton_4.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0631\u0627\u0641\u0642", None))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062c\u0646\u0633\u064a\u0647", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"amenities", None))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name_cLass", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Mother's Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a \u0627\u0644\u062e\u0631\u0648\u062c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Exit_Time", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0628\u0627\u0639\u0647/print", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0627\u0628", None))
        self.lineEdit_24.setText("")
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entry_Time", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0627\u0645", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.lineEdit_23.setText("")
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"age", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Phone_Number", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0631\u064a\u0636", None))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0627\u0628", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0648\u062d\u062f\u0647", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641/delete", None))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Father_ID", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0644\u064a\u0641\u0648\u0646", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0627\u0645", None))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Father's Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0646", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a/time", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Exit_Time", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0646", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0631\u0627\u0641\u0642", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"name_cLass", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0638/save", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Entry_Time", None))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"amenities", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0644\u064a\u0641\u0648\u0646", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a \u0627\u0644\u062f\u062e\u0648\u0644", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0628\u0637\u0627\u0642\u0647 \u0627\u0644\u0642\u0648\u0645\u064a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0631\u064a\u0636", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0646", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062c\u0646\u0633\u064a\u0629", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0627\u0628", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0627\u0645", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0628\u0637\u0627\u0642\u0647 \u0627\u0644\u0627\u0645", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u0644\u0641\u0648\u0646", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0648\u062d\u062f\u0647", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0631\u0627\u0641\u0642", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a \u0627\u0644\u062f\u062e\u0648\u0644", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a \u0627\u0644\u062e\u0631\u0648\u062c", None));
        self.lineEdit_17.setText("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mother's Name", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0648\u062d\u062f\u0647", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a \u0627\u0644\u062f\u062e\u0648\u0644", None))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone_Number", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0642\u062a \u0627\u0644\u062e\u0631\u0648\u062c", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Father_ID", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0631\u064a\u0636", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0628\u0637\u0627\u0642\u0647 \u0627\u0644\u0642\u0648\u0645\u064a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062c\u0646\u0633\u064a\u0647", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Father's Name", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u064a\u0644/Edit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0633\u062c\u064a\u0644 \u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0644\u0645\u0631\u064a\u0636", None))
    # retranslateUi

