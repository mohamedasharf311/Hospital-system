from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox,
    QTableWidget, QTableWidgetItem, QMessageBox, QLabel, QAbstractItemView, 
    QPushButton, QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import sys
import mysql.connector

class TaskManagerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("دواء المريض")
        self.setStyleSheet(self.get_stylesheet())
        self.init_database_connections()
        self.table_name_map = self.get_table_name_mapping()
        self.init_ui()
        self.check_and_create_todo_list_table()

    def get_stylesheet(self):
        return """
        QWidget {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        QLabel#titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        QLineEdit {
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            background-color: #fff;
        }
        QTableWidget {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        QTableWidget::item {
            padding: 4px;
        }
        QHeaderView::section {
            background-color: #e0e0e0;
            padding: 4px;
            border: 1px solid #dcdcdc;
        }
        QPushButton {
            padding: 8px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0056b3;
        }
        QListWidget, QDialog {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        QDialogButtonBox {
            padding: 8px;
        }
        QMessageBox {
            font-size: 14px;
        }
        """

    def init_database_connections(self):
        self.cure_conn = mysql.connector.connect(
            host='localhost',
            user='MA',
            password='01158820082baba',
            database='aer'
        )
        self.cure_cursor = self.cure_conn.cursor()

        self.f11_conn = mysql.connector.connect(
            host='localhost',
            user='MA',
            password='01158820082baba',
            database='f11'
        )
        self.f11_cursor = self.f11_conn.cursor()

    def get_table_name_mapping(self):
        return {
            "وحدة احمد قداح": "a1",
            "وحدة شريف قداح": "a2",
            "وحدة الكلي": "a3",
            " وحدة محمد جنينة": "a4",
            " رعاية السابع": "a5",
            "وحدة امراض الدم": "a6",
            "الحضانات": "a7",
            "رعايه السادس": "a8",
            "رعاية الثاني": "a9",
            "الغدد والسكر": "a10",
            " الجهاز الهضمي": "a11",
        }

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel("دواء المريض", self)
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search by name...")
        self.search_bar.returnPressed.connect(self.search_database)
        self.layout.addWidget(self.search_bar)

        self.setLayout(self.layout)

    def check_and_create_todo_list_table(self):
        self.cure_cursor.execute("SHOW TABLES LIKE 'todo_list'")
        if not self.cure_cursor.fetchone():
            self.cure_cursor.execute("""
                CREATE TABLE todo_list (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    column_name VARCHAR(255),
                    item VARCHAR(255),
                    status ENUM('done', 'still') NOT NULL DEFAULT 'still',
                    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
                    row_id VARCHAR(255) NOT NULL
                )
            """)
            self.cure_conn.commit()
            print("Table todo_list created.")
        else:
            self.cure_cursor.execute("SHOW COLUMNS FROM todo_list LIKE 'row_id'")
            if not self.cure_cursor.fetchone():
                self.cure_cursor.execute("ALTER TABLE todo_list ADD COLUMN row_id VARCHAR(255) NOT NULL")
                self.cure_conn.commit()
                print("Column row_id added to todo_list table.")

    def search_database(self):
        search_text = self.search_bar.text().strip()
        if not search_text:
            QMessageBox.warning(self, "Warning", "Search term must not be empty!")
            return

        results = self.query_database(search_text)
        if results:
            self.display_results(results)
        else:
            QMessageBox.information(self, "No Results", "No matching records found.")

    def query_database(self, search_text):
        results = []
        added_rows = set()
        try:
            for user_friendly_name, table_name in self.table_name_map.items():
                self.f11_cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = [col[0] for col in self.f11_cursor.fetchall()]

                name_columns = ['namep', 'namef', 'namem', 'namec', 'namer']
                for name_column in name_columns:
                    if name_column in columns:
                        self.f11_cursor.execute(
                            f"SELECT * FROM {table_name} WHERE {name_column} LIKE %s", 
                            (f"%{search_text}%",)
                        )
                        table_results = self.f11_cursor.fetchall()
                        for row in table_results:
                            row_identifier = (table_name, row[0])
                            if row_identifier not in added_rows:
                                results.append((user_friendly_name, table_name, columns, row))
                                added_rows.add(row_identifier)
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"MySQL error: {err}")
        return results

    def display_results(self, results):
        dialog = QDialog(self)
        dialog.setWindowTitle("Search Results")
        layout = QVBoxLayout(dialog)

        table_widget = QTableWidget(len(results), len(results[0][2]), dialog)
        table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        table_widget.setHorizontalHeaderLabels(results[0][2])

        for row_idx, (user_friendly_name, table_name, columns, row) in enumerate(results):
            for col_idx, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setData(Qt.UserRole, (table_name, row[0]))  # Store table name and row ID
                table_widget.setItem(row_idx, col_idx, item)

        table_widget.cellDoubleClicked.connect(self.open_todo_list)
        layout.addWidget(table_widget)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)

        dialog.setLayout(layout)
        dialog.exec()

    def open_todo_list(self, row, column):
        item = self.sender().item(row, column)
        if item:
            table_name, row_id = item.data(Qt.UserRole)
            dialog = TodoListDialog(self.cure_conn, self.cure_cursor, table_name, row_id, self)
            dialog.exec()

class TodoListDialog(QDialog):
    def __init__(self, cure_conn, cure_cursor, table_name, row_id, parent=None):
        super().__init__(parent)
        self.cure_conn = cure_conn
        self.cure_cursor = cure_cursor
        self.table_name = table_name
        self.row_id = row_id
        self.setWindowTitle("To-Do List")
        self.setStyleSheet(parent.get_stylesheet())  # Use the same stylesheet
        self.init_ui()
        self.load_tasks()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a task...")
        self.layout.addWidget(self.task_input)

        self.add_task_button = QPushButton("Add Task", self)
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        self.task_list = QListWidget(self)
        self.task_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.layout.addWidget(self.task_list)

        self.finished_task_list = QListWidget(self)
        self.finished_task_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.layout.addWidget(QLabel("Finished Tasks"))
        self.layout.addWidget(self.finished_task_list)

        self.mark_as_done_button = QPushButton("Mark as Done", self)
        self.mark_as_done_button.clicked.connect(self.mark_as_done)
        self.layout.addWidget(self.mark_as_done_button)

        self.setLayout(self.layout)

    def load_tasks(self):
        self.task_list.clear()
        self.finished_task_list.clear()
        self.cure_cursor.execute("SELECT id, item, status, date_added FROM todo_list WHERE row_id = %s", (self.row_id,))
        tasks = self.cure_cursor.fetchall()
        for task in tasks:
            item_text = f"{task[1]} - {task[3]}"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, task[0])  # Store the task ID
            if task[2] == 'still':
                self.task_list.addItem(item)
            else:
                self.finished_task_list.addItem(item)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.cure_cursor.execute("INSERT INTO todo_list (item, row_id) VALUES (%s, %s)", (task, self.row_id))
            self.cure_conn.commit()
            QMessageBox.information(self, "Success", "Task added successfully!")
            self.load_tasks()  # Refresh the task list
        else:
            QMessageBox.warning(self, "Warning", "Task must not be empty!")

    def mark_as_done(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_id = selected_item.data(Qt.UserRole)
            self.cure_cursor.execute("UPDATE todo_list SET status = 'done' WHERE id = %s", (task_id,))
            self.cure_conn.commit()
            QMessageBox.information(self, "Success", "Task marked as done!")
            self.load_tasks()  # Refresh the task list
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to mark as done.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManagerWindow()
    window.show()
    sys.exit(app.exec())
