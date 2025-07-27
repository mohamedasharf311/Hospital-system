import sys
from PySide6 import QtWidgets, QtCore, QtGui
import mysql.connector

class DatabaseTreeView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.page_size = 20
        self.current_page = 1
        self.modify_widgets_displayed = False

        # Mapping of backend table names to display names
        self.table_name_mapping = {
            "a1": "وحده احمد قداح",
            "a2": "وحده شريف قداح",
            "a3": "وحده الكلي",
            "a4": "وحده محمد جنينه",
            "a5": "رعاية السابع",
            "a6": "وحده امراض الدم",
            "a7": "الحاضانات",
            "a8": "رعاية السادس",
            "a9": "رعاية الثاني",
            "a10": "الغدد والسكر",
            "a11": "الجهاز الهضمي",
            # Add more mappings as needed
        }

        # Mapping of column names to display labels
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

        self.init_ui()
        self.fetch_table_names()

    def init_ui(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="MA",
            password="01158820082baba",
            database="f11",
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

        layout = QtWidgets.QVBoxLayout(self)

        font = QtGui.QFont("Arial", 12)
        self.setFont(font)

        header_label = QtWidgets.QLabel("ابو الريش المنيره اطفال")
        header_font = QtGui.QFont("Arial", 24, QtGui.QFont.Bold)
        header_label.setFont(header_font)
        header_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(header_label)

        search_frame = QtWidgets.QWidget()
        search_layout = QtWidgets.QHBoxLayout(search_frame)
        search_label = QtWidgets.QLabel("بحث:")
        search_layout.addWidget(search_label)
        self.search_entry = QtWidgets.QLineEdit()
        search_layout.addWidget(self.search_entry)
        search_button = QtWidgets.QPushButton("بحث")
        search_button.clicked.connect(self.search)
        search_layout.addWidget(search_button)
        layout.addWidget(search_frame)

        self.table_var = QtWidgets.QComboBox()
        self.table_var.currentIndexChanged.connect(self.fetch_table_data)
        layout.addWidget(self.table_var)

        self.destination_table_var = QtWidgets.QComboBox()
        layout.addWidget(self.destination_table_var)

        self.tree = QtWidgets.QTreeWidget()
        layout.addWidget(self.tree)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QHBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        self.name_frame = QtWidgets.QWidget()
        layout.addWidget(self.name_frame)
        self.column_entries = []

        modify_button = QtWidgets.QPushButton("تعديل")
        modify_button.clicked.connect(self.toggle_modify_widgets)
        layout.addWidget(modify_button)

        move_button = QtWidgets.QPushButton("نقل المريض المحدد")
        move_button.clicked.connect(self.move_selected_row)
        layout.addWidget(move_button)

        delete_button = QtWidgets.QPushButton("حذف المريض المحدد")
        delete_button.clicked.connect(self.delete_selected_row)
        layout.addWidget(delete_button)

        rename_table_frame = QtWidgets.QWidget()
        rename_table_layout = QtWidgets.QHBoxLayout(rename_table_frame)
        rename_table_label = QtWidgets.QLabel("إعادة تسمية الجدول إلى:")
        rename_table_layout.addWidget(rename_table_label)
        self.new_table_name_entry = QtWidgets.QLineEdit()
        rename_table_layout.addWidget(self.new_table_name_entry)
        rename_table_button = QtWidgets.QPushButton("إعادة تسمية")
        rename_table_button.clicked.connect(self.rename_table)
        rename_table_layout.addWidget(rename_table_button)
        layout.addWidget(rename_table_frame)

        self.status_label = QtWidgets.QLabel()
        layout.addWidget(self.status_label)

        pagination_frame = QtWidgets.QWidget()
        pagination_layout = QtWidgets.QHBoxLayout(pagination_frame)
        prev_button = QtWidgets.QPushButton("السابق")
        prev_button.clicked.connect(self.previous_page)
        pagination_layout.addWidget(prev_button)
        next_button = QtWidgets.QPushButton("التالي")
        next_button.clicked.connect(self.next_page)
        pagination_layout.addWidget(next_button)
        self.page_label = QtWidgets.QLabel()
        pagination_layout.addWidget(self.page_label)
        layout.addWidget(pagination_frame)

        self.apply_styles()

    def fetch_table_names(self):
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]

        self.display_names = [self.table_name_mapping.get(table, table) for table in tables]

        self.table_var.addItems(self.display_names)
        self.destination_table_var.addItems(self.display_names)

    def get_real_table_name(self, display_name):
        for real_name, display in self.table_name_mapping.items():
            if display == display_name:
                return real_name
        return display_name

    def fetch_table_data(self):
        selected_display_name = self.table_var.currentText()
        real_table_name = self.get_real_table_name(selected_display_name)
        self.column_names = self.get_column_names(real_table_name)
        column_labels = [self.column_name_mapping.get(col, col) for col in self.column_names]
        self.tree.setHeaderLabels(column_labels)
        self.load_page()
        self.create_editing_widgets()  # Update editing widgets for the new table

    def get_column_names(self, table_name):
        self.cursor.execute(f"DESCRIBE {table_name}")
        columns = self.cursor.fetchall()
        return [column[0] for column in columns]

    def load_page(self):
        selected_display_name = self.table_var.currentText()
        real_table_name = self.get_real_table_name(selected_display_name)
        offset = (self.current_page - 1) * self.page_size
        self.cursor.execute(f"SELECT * FROM {real_table_name} LIMIT {self.page_size} OFFSET {offset}")
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            self.tree.clear()
            for row in rows:
                self.tree.addTopLevelItem(QtWidgets.QTreeWidgetItem([str(col) for col in row]))
            self.page_label.setText(f"الصفحة {self.current_page}")

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.load_page()

    def next_page(self):
        self.current_page += 1
        self.load_page()

    def search(self):
        search_term = self.search_entry.text()
        selected_display_name = self.table_var.currentText()
        real_table_name = self.get_real_table_name(selected_display_name)
        search_column = self.column_names[1]  # Adjust this index based on the column you want to search on
        self.cursor.execute(f"SELECT * FROM {real_table_name} WHERE {search_column} LIKE '%{search_term}%'")
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            self.tree.clear()
            for row in rows:
                self.tree.addTopLevelItem(QtWidgets.QTreeWidgetItem([str(col) for col in row]))

    def move_selected_row(self):
        selected_items = self.tree.selectedItems()
        if not selected_items:
            self.status_label.setText("يرجى تحديد المريض لنقله")
            return

        selected_display_name = self.table_var.currentText()
        selected_table = self.get_real_table_name(selected_display_name)
        destination_display_name = self.destination_table_var.currentText()
        destination_table = self.get_real_table_name(destination_display_name)

        if selected_table == destination_table:
            self.status_label.setText("لا يمكن نقل المريض إلى نفس الجدول.")
            return

        selected_row = selected_items[0]
        source_columns = self.get_column_names(selected_table)
        dest_columns = self.get_column_names(destination_table)

        # Fetch values based on source columns
        row_values = [selected_row.text(source_columns.index(col)) for col in source_columns]

        try:
            insert_query = f"INSERT INTO {destination_table} ({', '.join(dest_columns)}) VALUES ({', '.join(['%s'] * len(dest_columns))})"
            delete_query = f"DELETE FROM {selected_table} WHERE id = %s"
            
            print(f"Insert Query: {insert_query}")
            print(f"Delete Query: {delete_query}")
            print(f"Row Values: {row_values}")

            self.cursor.execute(insert_query, row_values)
            self.cursor.execute(delete_query, (row_values[0],))
            self.conn.commit()
            
            self.status_label.setText("تم نقل المريض بنجاح!")
            self.load_page()
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.status_label.setText(f"خطأ في MySQL: {err}")

    def delete_selected_row(self):
        selected_items = self.tree.selectedItems()
        if not selected_items:
            self.status_label.setText("يرجى تحديد المريض لحذفه")
            return

        selected_display_name = self.table_var.currentText()
        selected_table = self.get_real_table_name(selected_display_name)
        selected_row_id = selected_items[0].text(0)  # Assuming the first column is the ID

        # Fetch the actual column name for the primary key, assuming it's the first column in column_names
        primary_key_column = self.column_names[0]  # Adjust if the primary key column is different

        try:
            delete_query = f"DELETE FROM {selected_table} WHERE {primary_key_column} = %s"
            
            print(f"Delete Query: {delete_query}")
            print(f"Selected Row ID: {selected_row_id}")
            
            self.cursor.execute(delete_query, (selected_row_id,))
            self.conn.commit()
            
            self.status_label.setText("تم حذف المريض بنجاح!")
            self.load_page()
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.status_label.setText(f"خطأ في MySQL: {err}")

    def toggle_modify_widgets(self):
        if not self.tree.selectedItems():
            self.status_label.setText("يرجى تحديد صف لتعديله")
            return

        self.modify_widgets_displayed = not self.modify_widgets_displayed
        self.scroll_area.setVisible(self.modify_widgets_displayed)

        if self.modify_widgets_displayed:
            selected_item = self.tree.selectedItems()[0]
            for index, value in enumerate([selected_item.text(i) for i in range(selected_item.columnCount())]):
                if index == 0:
                    continue  # Skip the ID column
                self.column_entries[index - 1].setText(value)  # -1 to skip 'id'

    def create_editing_widgets(self):
        # Clear old widgets
        for widget in self.column_entries:
            self.scroll_layout.removeWidget(widget)
            widget.deleteLater()
        self.column_entries = []

        # Add new widgets in a horizontal layout
        for col_name in self.column_names:
            if col_name == "id":
                continue
            label = QtWidgets.QLabel(self.column_name_mapping.get(col_name, col_name))
            entry = QtWidgets.QLineEdit()
            entry.setFixedWidth(200)  # Adjust this width as needed
            self.scroll_layout.addWidget(label)
            self.scroll_layout.addWidget(entry)
            self.column_entries.append(entry)

        self.scroll_content.setLayout(self.scroll_layout)

    def rename_table(self):
        current_display_name = self.table_var.currentText()
        current_table_name = self.get_real_table_name(current_display_name)
        new_table_name = self.new_table_name_entry.text()
        
        if new_table_name:
            try:
                self.cursor.execute(f"RENAME TABLE {current_table_name} TO {new_table_name}")
                self.conn.commit()
                self.status_label.setText(f"تم إعادة تسمية الجدول إلى {new_table_name}")
                self.fetch_table_names()
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                self.status_label.setText(f"خطأ في MySQL: {err}")

    def apply_styles(self):
        # Define the stylesheet
        stylesheet = """
        QWidget {
            background-color: #f0f0f0;
        }
        QLineEdit {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 4px;
            padding: 4px;
        }
        QPushButton {
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QComboBox {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 4px;
            padding: 4px;
        }
        QTreeWidget {
            background-color: #ffffff;
            border: 1px solid #cccccc;
        }
        QHeaderView::section {
            background-color: #dddddd;
            padding: 4px;
            border: 1px solid #cccccc;
        }
        QLabel {
            color: #333333;
        }
        """
        # Apply the stylesheet
        self.setStyleSheet(stylesheet)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DatabaseTreeView()
    window.show()
    sys.exit(app.exec())
