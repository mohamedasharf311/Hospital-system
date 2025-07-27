from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QScrollArea
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import mysql.connector
import sys

class NameCounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Name Counter")
        self.setStyleSheet("background-color: #f0f0f0;")
        self.layout = QVBoxLayout()

        # Create big font label at the top
        big_font_label = QLabel("Table Name Counter")
        big_font_label.setAlignment(Qt.AlignCenter)
        big_font_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.layout.addWidget(big_font_label)

        # Connect to MySQL database
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123123123",
                database="f11"
            )
            self.cursor = self.connection.cursor()

            # Retrieve list of tables
            self.cursor.execute("SHOW TABLES")
            self.tables = [table[0] for table in self.cursor.fetchall()]

            # Create widgets
            self.table_labels = {}
            self.spin_boxes = {}
            for table in self.tables:
                label = QLabel(f"{table}: 0 names")
                self.table_labels[table] = label
                self.layout.addWidget(label)

                spin_box = QSpinBox()
                spin_box.setRange(0, 100)  # Set a reasonable maximum number
                self.spin_boxes[table] = spin_box
                self.layout.addWidget(spin_box)

            self.update_button = QPushButton("Update Limits")
            self.update_button.clicked.connect(self.update_limits)
            self.layout.addWidget(self.update_button)

            self.setLayout(self.layout)

        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            sys.exit(1)

    def update_limits(self):
        try:
            for table in self.tables:
                max_names = self.spin_boxes[table].value()
                self.cursor.execute(f"UPDATE {table} SET max_names = {max_names}")

                # Refresh name count
                self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
                name_count = self.cursor.fetchone()[0]
                self.table_labels[table].setText(f"{table}: {name_count} names")

            self.connection.commit()  # Commit changes to database

        except mysql.connector.Error as e:
            print(f"Error updating limits: {e}")

    def closeEvent(self, event):
        try:
            self.cursor.close()
            self.connection.close()
        except mysql.connector.Error as e:
            print(f"Error closing MySQL connection: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create scrollable area
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    # Create widget and layout
    widget = QWidget()
    layout = QVBoxLayout(widget)
    layout.addWidget(NameCounterApp())

    # Set widget to scroll area
    scroll_area.setWidget(widget)

    # Show scroll area
    scroll_area.show()

    # Execute application
    sys.exit(app.exec())
