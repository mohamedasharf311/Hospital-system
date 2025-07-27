from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from signup import SignUpApp
import subprocess  # Import subprocess to run another script
import os  # Import os to check if file exists

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(839, 565)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QtCore.QRect(-10, 10, 821, 500))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"	color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(610, 120, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(570, 200, 190, 40))
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 270, 190, 40))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(570, 320, 190, 40))
        font2 = QtGui.QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QtCore.QRect(580, 380, 181, 16))
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 210);")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 130))
        self.label_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 75);")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(50, 80, 180, 40))
        font3 = QtGui.QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:rgba(255, 255, 255, 200);")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QtCore.QRect(50, 145, 220, 50))
        font4 = QtGui.QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color:rgba(255, 255, 255, 170);")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QtCore.QRect(460, 370, 171, 51))
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(-220, 20, 751, 471))
        self.label.setPixmap(QtGui.QPixmap(u"image/ae.png"))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(600, 400, 131, 41))
        font5 = QtGui.QFont()
        font5.setFamily(u"Malgun Gothic Semilight")
        font5.setPointSize(20)
        self.pushButton_2.setFont(font5)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or password?"))
        self.label_7.setText(_translate("Form", "Abu Al-Raish "))
        self.label_8.setText(_translate("Form", "Hi,"
"Welcome to Abu Al-Raish Al-Muneera.\n"
" If you don't have an account yet,\n please press 'Sign Up'."))
        self.pushButton_2.setText(_translate("Form", "Sign Up"))

class LoginForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.signin)
        self.pushButton_2.clicked.connect(self.signup)
        self.dr = None
        self.n = None
        self.a = None

    def signin(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Connect to MySQL and verify username and password
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="MA",
                password="01158820082baba",
                database="signup"
            )
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            user_found = False

            for table in tables:
                table_name = table[0]
                try:
                    query = f"SELECT * FROM {table_name} WHERE e=%s AND p=%s"
                    cursor.execute(query, (username, password))
                    result = cursor.fetchone()
                    if result:
                        user_found = True
                        if table_name == "dr":
                            self.dr = result
                        elif table_name == "n":
                            self.n = result
                        elif table_name == "a":
                            self.a = result
                        break
                except mysql.connector.Error as err:
                    print(f"Skipping table {table_name} due to error: {err}")
                    continue

            if user_found:
                if os.path.isfile("main.py"):
                    subprocess.Popen(["python", "main.py"])
                else:
                    QtWidgets.QMessageBox.warning(None, "Error", "main.py not found")
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Invalid username or password")

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def signup(self):
        self.sign_up_window = SignUpApp()
        self.sign_up_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())
