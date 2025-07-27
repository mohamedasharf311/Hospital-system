from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt
import mysql.connector

class SignUpApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setGeometry(300, 200, 925, 500)
        self.setStyleSheet("background-color: white;")
        self.setFixedSize(925, 500)

        # Load the image using PIL (ImageQt)
        image_path = 'image/ae.png'
        img = Image.open(image_path)
        img = img.resize((350, 390))  # Resize the image
        qimg = ImageQt.ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(qimg)

        # Create a Label to display the image
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(1, 40, 350, 390))

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(480, 50, 350, 390))
        self.frame.setStyleSheet("background-color: #fff;")

        self.heading = QtWidgets.QLabel(self.frame)
        self.heading.setText('Sign Up')
        self.heading.move(100, 5)
        self.heading.setStyleSheet("color: #57a1f8; font-size: 23pt; font-weight: bold;")

        self.user = QtWidgets.QLineEdit(self.frame)
        self.user.setGeometry(QtCore.QRect(30, 80, 295, 30))
        self.user.setStyleSheet("border: none; border-bottom: 1px solid black; background-color: white;")
        self.user.setPlaceholderText('Username')
        self.user.returnPressed.connect(self.user.clear)

        self.code = QtWidgets.QLineEdit(self.frame)
        self.code.setGeometry(QtCore.QRect(30, 150, 295, 30))
        self.code.setStyleSheet("border: none; border-bottom: 1px solid black; background-color: white;")
        self.code.setPlaceholderText('Password')
        self.code.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.code.returnPressed.connect(self.code.clear)

        self.conform_code = QtWidgets.QLineEdit(self.frame)
        self.conform_code.setGeometry(QtCore.QRect(30, 220, 295, 30))
        self.conform_code.setStyleSheet("border: none; border-bottom: 1px solid black; background-color: white;")
        self.conform_code.setPlaceholderText('Confirm Password')
        self.conform_code.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.conform_code.returnPressed.connect(self.conform_code.clear)

        # Add a ComboBox for user type selection
        self.user_type = QtWidgets.QComboBox(self.frame)
        self.user_type.setGeometry(QtCore.QRect(30, 260, 295, 30))
        self.user_type.setStyleSheet("border: none; border-bottom: 1px solid black; background-color: white;")
        self.user_type.addItems(["Select user type", "dr", "n", "a"])

        self.signup_button = QtWidgets.QPushButton(self.frame)
        self.signup_button.setGeometry(QtCore.QRect(35, 310, 295, 40))
        self.signup_button.setText('Sign Up')
        self.signup_button.setStyleSheet("background-color: #57a178; color: white; border: none; font-weight: bold;")
        self.signup_button.clicked.connect(self.signup)

        # Sign in widgets
        self.signin_label = QtWidgets.QLabel(self.frame)
        self.signin_label.setText('I have an account')
        self.signin_label.setGeometry(QtCore.QRect(200, 370, 120, 30))
        self.signin_label.setStyleSheet("color: black; font-size: 9pt;")

        self.signin_button = QtWidgets.QPushButton(self.frame)
        self.signin_button.setGeometry(QtCore.QRect(100, 370, 70, 30))
        self.signin_button.setText('Sign In')
        self.signin_button.setStyleSheet("background-color: white; color: #57a178; border: none;")
        self.signin_button.clicked.connect(self.signin_action)

        # Database connection
        self.db_connection = mysql.connector.connect(
            host='localhost',
            user='MA',
            password='01158820082baba',
            database='signup'
        )

    def signup(self):
        username = self.user.text()
        password = self.code.text()
        confirm_password = self.conform_code.text()
        user_type = self.user_type.currentText()

        # Check if passwords match
        if password != confirm_password:
            QtWidgets.QMessageBox.critical(self, "Error", "Passwords do not match")
            # Clear password fields
            self.code.clear()
            self.conform_code.clear()
            return

        # Check if user type is selected
        if user_type == "Select user type":
            QtWidgets.QMessageBox.critical(self, "Error", "Please select a user type")
            return

        try:
            cursor = self.db_connection.cursor()

            # Check if the username already exists in the selected table
            check_query = f"SELECT * FROM {user_type} WHERE e = %s"
            cursor.execute(check_query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                QtWidgets.QMessageBox.critical(self, "Error", "Username already exists")
                # Clear password fields
                self.code.clear()
                self.conform_code.clear()
            else:
                # Insert the new user into the appropriate table based on user type
                insert_query = f"INSERT INTO {user_type} (e, p) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, password))
                self.db_connection.commit()

                QtWidgets.QMessageBox.information(self, "Success", "Sign up successful")

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Database error: {err}")

        finally:
            if 'cursor' in locals():
                cursor.close()

    def signin_action(self):
        # Define the action to be performed when the user clicks "Sign In"
        QtWidgets.QMessageBox.information(self, "Sign In", "Sign in action will be performed here.")

# Start the PyQt application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SignUpApp()
    window.show()
    sys.exit(app.exec())
