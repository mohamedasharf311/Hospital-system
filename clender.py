import sys
import json
import mysql.connector
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QInputDialog

class MyForm(QMainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        self.setWindowTitle("Calendar List")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.calendar = QCalendarWidget(self.central_widget)
        self.layout.addWidget(self.calendar)
        self.calendar.clicked.connect(self.update_table)

        # Set the initial row and column count to 50
        self.table_widget = QTableWidget(50, 50, self.central_widget)
        self.layout.addWidget(self.table_widget)

        self.add_button = QPushButton("Add Item", self.central_widget)
        self.add_button.clicked.connect(self.add_item)
        self.layout.addWidget(self.add_button)

        self.save_button = QPushButton("Save", self.central_widget)
        self.save_button.clicked.connect(self.save_list)
        self.layout.addWidget(self.save_button)

        # MySQL Connection
        self.cnx = mysql.connector.connect(
            host='localhost',
            user='MA',
            password='01158820082baba',
            database='aer'
        )

        self.ensure_table_exists()

        # Load list when initializing
        self.update_table()

        # Timer to update list automatically every day
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_table)
        self.timer.start(24 * 60 * 60 * 1000)  # Trigger every 24 hours (24 * 60 * 60 * 1000 milliseconds)

    def ensure_table_exists(self):
        cursor = self.cnx.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS date_time (
                    year INT NOT NULL,
                    month INT NOT NULL,
                    day INT NOT NULL,
                    schedule JSON,
                    PRIMARY KEY (year, month, day)
                )
            """)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print("Error creating table:", err)
        finally:
            cursor.close()

    def update_table(self):
        selected_date = self.calendar.selectedDate().toPython()
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day

        cursor = self.cnx.cursor()

        try:
            cursor.execute("SELECT schedule FROM date_time WHERE year = %s AND month = %s AND day = %s", (year, month, day))
            rows = cursor.fetchall()  # Fetch all rows
            print("Fetched rows:", rows)

            schedule_json = {}
            for row in rows:
                if row[0] is not None:
                    schedule_json.update(json.loads(row[0]))  # Parse JSON if available and update schedule

            print("Schedule JSON:", schedule_json)
            self.populate_table(schedule_json)

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()  # Close the cursor after fetching results

    def populate_table(self, schedule):
        # Clear the table before populating it with new data
        self.table_widget.clearContents()
        
        # Populate the table with items from the schedule
        for key, value in schedule.items():
            i, j = map(int, key.split('_'))
            item_str = str(value) if value is not None else ""
            table_item = QTableWidgetItem(item_str)
            self.table_widget.setItem(i, j, table_item)

    def add_item(self):
        item_text, ok = QInputDialog.getText(self, "Enter Item Text", "Item:")
        if ok:
            selected_row = self.table_widget.currentRow()
            selected_column = self.table_widget.currentColumn()
            if selected_row != -1 and selected_column != -1:
                table_item = QTableWidgetItem(item_text)
                self.table_widget.setItem(selected_row, selected_column, table_item)

    def save_list(self):
        selected_date = self.calendar.selectedDate().toPython()
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day

        # Load existing schedule if available
        cursor = self.cnx.cursor()
        try:
            existing_schedule = {}
            for i in range(self.table_widget.rowCount()):
                for j in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(i, j)
                    if item:
                        key = f"{i}_{j}"
                        existing_schedule[key] = item.text()

            # Save the updated schedule
            cursor.execute("REPLACE INTO date_time (year, month, day, schedule) VALUES (%s, %s, %s, %s)", (year, month, day, json.dumps(existing_schedule)))
            self.cnx.commit()
            print("Schedule saved to MySQL")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyForm()
    my_app.show()
    sys.exit(app.exec())
