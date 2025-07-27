import sys
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QComboBox, QLabel, QFileDialog, QHBoxLayout, QDialog, QListWidget, QListWidgetItem
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QThread, Signal


class PhotoViewer(QDialog):
    def __init__(self, photo_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Photo Viewer")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.photo_label = QLabel(self)
        self.photo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.photo_label)

        self.setLayout(layout)
        self.display_photo(photo_path)

    def display_photo(self, photo_path):
        pixmap = QPixmap(photo_path)
        if not pixmap.isNull():
            self.photo_label.setPixmap(pixmap.scaled(800, 600, Qt.KeepAspectRatio))
        else:
            self.photo_label.setText("Failed to load photo.")


class MySQLViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initDB()
        self.current_table = None

    def initUI(self):
        self.setWindowTitle('MySQL Viewer')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        self.table_selector = QComboBox(self)
        self.table_selector.setStyleSheet(
            "QComboBox {"
            "  font-size: 16px;"
            "  padding: 5px;"
            "}"
        )
        main_layout.addWidget(self.table_selector)

        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText('Enter name to search')
        self.search_input.setStyleSheet(
            "QLineEdit {"
            "  font-size: 16px;"
            "  padding: 5px;"
            "  margin-bottom: 10px;"
            "}"
        )
        main_layout.addWidget(self.search_input)

        self.search_button = QPushButton('Search', self)
        self.search_button.setStyleSheet(
            "QPushButton {"
            "  font-size: 16px;"
            "  padding: 10px;"
            "  background-color: #5cb85c;"
            "  color: white;"
            "  border: none;"
            "  border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "  background-color: #4cae4c;"
            "}"
        )
        self.search_button.clicked.connect(self.perform_search)
        main_layout.addWidget(self.search_button)

        self.result_table = QTableWidget(self)
        self.result_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.result_table.setStyleSheet(
            "QTableWidget {"
            "  font-size: 14px;"
            "}"
        )
        self.result_table.clicked.connect(self.row_selected)
        main_layout.addWidget(self.result_table)

        button_layout = QHBoxLayout()

        self.upload_photo_button = QPushButton('Upload Photo', self)
        self.upload_photo_button.setStyleSheet(
            "QPushButton {"
            "  font-size: 16px;"
            "  padding: 10px;"
            "  background-color: #f0ad4e;"
            "  color: white;"
            "  border: none;"
            "  border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "  background-color: #ec971f;"
            "}"
        )
        self.upload_photo_button.clicked.connect(self.upload_photo)
        self.upload_photo_button.setEnabled(False)
        button_layout.addWidget(self.upload_photo_button)

        self.display_photo_button = QPushButton('Display Photo', self)
        self.display_photo_button.setStyleSheet(
            "QPushButton {"
            "  font-size: 16px;"
            "  padding: 10px;"
            "  background-color: #5bc0de;"
            "  color: white;"
            "  border: none;"
            "  border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "  background-color: #46b8da;"
            "}"
        )
        self.display_photo_button.clicked.connect(self.display_photos)
        self.display_photo_button.setEnabled(False)
        button_layout.addWidget(self.display_photo_button)

        main_layout.addLayout(button_layout)

        self.photo_list = QListWidget(self)
        self.photo_list.setStyleSheet(
            "QListWidget {"
            "  font-size: 14px;"
            "  margin-top: 10px;"
            "  border: 1px solid #ddd;"
            "  padding: 10px;"
            "}"
        )
        self.photo_list.itemClicked.connect(self.show_large_photo)
        main_layout.addWidget(self.photo_list)

        self.setLayout(main_layout)

    def initDB(self):
        self.db_connection = mysql.connector.connect(
                host='192.168.1.4',
                user='MA',
                password='01158820082baba',
                database='f11'
        )
        self.cursor = self.db_connection.cursor()

        self.table_name_mapping = {
            "وحدة احمد قداح": "a1",
            "وحدة شريف قداح": "a2",
            "وحدة الكلي": "a3",
            " وحدة محمد جنينة": "a4",
            " رعاية السابع": "a5",
            "وحدة امراض الدم": "a6",
            "الحضانات": "a7",
            "وحدة رعاية السادس": "a8",
            "رعاية الثاني": "a9",
            "الغدد والسكر": "a10",
            " الجهاز الهضمي": "a11",
         
            # Add more mappings as needed
        }

        self.column_name_mapping = {
            'id': 'ID',
            'namep': 'اسم المريض',
            'age': ' السن',
            'namef': 'اسم الاب',
            'namem': 'اسم الام',
            'numberid': 'ررقم البطاقة القومي ',
            'addears': 'العنوان ',
            'numberf': 'رقم التليفون',
            'namec': ' اسم الوحده',
            'namer': ' المرافق',
            'timee': 'وقت الدخول ',
            'timex': 'وقت الخروج ',
            'g': ' الجنسية',

            # Add more mappings as needed
        }

        self.show_tables()

    def ensure_table_and_columns_exist(self, table_name):
        # Check if the table exists, and if not, create it
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY
            )
        """)
        self.db_connection.commit()

        # Check if 'namep' column exists, and if not, create it
        self.cursor.execute(f"""
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = DATABASE()
            AND TABLE_NAME = %s
            AND COLUMN_NAME = 'namep'
        """, (table_name,))
        namep_column_exists = self.cursor.fetchone()[0]

        if not namep_column_exists:
            self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN namep VARCHAR(255) NOT NULL")
            self.db_connection.commit()

        # Create the photos table if it does not exist
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS photos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                record_id INT,
                photo_blob LONGBLOB,
                FOREIGN KEY (record_id) REFERENCES {table_name}(id) ON DELETE CASCADE
            )
        """)
        self.db_connection.commit()

        # Check if the index exists, and if not, create it
        self.cursor.execute(f"""
            SELECT COUNT(1)
            FROM INFORMATION_SCHEMA.STATISTICS
            WHERE TABLE_SCHEMA = DATABASE()
            AND TABLE_NAME = %s
            AND INDEX_NAME = 'idx_namep'
        """, (table_name,))
        index_exists = self.cursor.fetchone()[0]

        if not index_exists:
            self.cursor.execute(f"CREATE INDEX idx_namep ON {table_name}(namep)")
            self.db_connection.commit()

    def show_tables(self):
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()

        self.table_selector.clear()
        for table in tables:
            for display_name, actual_name in self.table_name_mapping.items():
                if actual_name == table[0]:
                    self.table_selector.addItem(display_name)
                    break

    def perform_search(self):
        search_term = self.search_input.text()
        selected_display_name = self.table_selector.currentText()
        selected_table = self.table_name_mapping[selected_display_name]
        self.current_table = selected_table

        if selected_table:
            self.ensure_table_and_columns_exist(selected_table)  # Ensure the table and columns exist

            # Asynchronous search operation
            self.search_thread = SearchThread(self.db_connection, selected_table, search_term, self.column_name_mapping)
            self.search_thread.search_completed.connect(self.update_table)
            self.search_thread.start()

    def update_table(self, results, column_names):
        display_column_names = [self.column_name_mapping.get(col, col) for col in column_names]
        self.result_table.setColumnCount(len(display_column_names))
        self.result_table.setHorizontalHeaderLabels(display_column_names)

        self.result_table.setRowCount(len(results))
        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.result_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.upload_photo_button.setEnabled(True)
        self.display_photo_button.setEnabled(True)

    def row_selected(self):
        self.display_photo_button.setEnabled(True)

    def row_selected(self):
        selected_row = self.result_table.currentRow()
        if selected_row >= 0:
           for column in range(self.result_table.columnCount()):
            item = self.result_table.item(selected_row, column)
            if item is not None:
                item.setFlags(Qt.ItemIsEnabled)  # Ensure the item is read-only
        self.display_photo_button.setEnabled(True)


    def upload_photo(self):
        selected_row = self.result_table.currentRow()
        if selected_row >= 0:
            row_id = self.result_table.item(selected_row, 0).text()  # Assuming the first column is the ID

            file_dialog = QFileDialog(self)
            file_dialog.setFileMode(QFileDialog.ExistingFiles)
            file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")

            if file_dialog.exec():
                selected_files = file_dialog.selectedFiles()
                for file_path in selected_files:
                    with open(file_path, 'rb') as file:
                        photo_blob = file.read()

                    query = f"INSERT INTO photos (record_id, photo_blob) VALUES (%s, %s)"
                    self.cursor.execute(query, (row_id, photo_blob))
                    self.db_connection.commit()

                # Update the result table to indicate the photo blob is stored
                self.photo_list.addItem(f"Photos for record ID {row_id} uploaded")

    def display_photos(self):
        selected_row = self.result_table.currentRow()
        if (selected_row >= 0) and (self.current_table):
            row_id = self.result_table.item(selected_row, 0).text()  # Assuming the first column is the ID

            query = f"SELECT id, photo_blob FROM photos WHERE record_id = %s"
            self.cursor.execute(query, (row_id,))
            results = self.cursor.fetchall()

            self.photo_list.clear()
            for photo_id, photo_blob in results:
                temp_photo_path = f"temp_photo_{photo_id}.png"
                with open(temp_photo_path, 'wb') as file:
                    file.write(photo_blob)

                list_item = QListWidgetItem(f"Photo ID: {photo_id}")
                list_item.setData(Qt.UserRole, temp_photo_path)
                self.photo_list.addItem(list_item)

    def show_large_photo(self, item):
        photo_path = item.data(Qt.UserRole)
        if photo_path:
            self.photo_viewer = PhotoViewer(photo_path, self)
            self.photo_viewer.exec()


class SearchThread(QThread):
    search_completed = Signal(list, list)

    def __init__(self, db_connection, table_name, search_term, column_name_mapping):
        super().__init__()
        self.db_connection = db_connection
        self.table_name = table_name
        self.search_term = search_term
        self.column_name_mapping = column_name_mapping

    def run(self):
        cursor = self.db_connection.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE namep LIKE %s"
        cursor.execute(query, ('%' + self.search_term + '%',))

        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]

        self.search_completed.emit(results, column_names)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MySQLViewer()
    viewer.show()
    sys.exit(app.exec())
