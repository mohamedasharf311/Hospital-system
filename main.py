from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, 
    QDialog, QDialogButtonBox, QListWidget, QAbstractItemView, 
    QPushButton, QLineEdit, QMessageBox, QLabel, QScrollArea, QSizePolicy, 
    QHBoxLayout, QFormLayout, QSpinBox, QListWidgetItem, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt, QThread, Signal
from ui_main import Ui_MainWindow  # Adjust import according to your structure
from convert import *
from clender import MyForm
from search import DatabaseTreeView
from ui_functions import *
from todo import *
from cure import TaskManagerWindow
from bed import NameCounterApp
import mysql.connector
import asyncio
import websockets
from start_server import *


class TableListDialog(QDialog):
    def __init__(self, display_names):
        super().__init__()
        self.setWindowTitle("Select Table")
        self.resize(300, 400)
        
        layout = QVBoxLayout()
        
        self.table_list = QListWidget()
        self.table_list.addItems(display_names)
        self.table_list.setSelectionMode(QAbstractItemView.SingleSelection)
        
        layout.addWidget(self.table_list)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        layout.addWidget(buttons)
        
        self.setLayout(layout)

    def get_selected_table(self):
        selected_items = self.table_list.selectedItems()
        if selected_items:
            return selected_items[0].text()
        return None

class SetTableCapacityDialog(QDialog):
    def __init__(self, display_names):
        super().__init__()
        self.setWindowTitle("Set Table Capacities")

        self.table_names = display_names
        self.table_capacity = {}

        layout = QFormLayout()
        self.capacity_inputs = {}

        for table_name in display_names:
            spin_box = QSpinBox()
            spin_box.setMinimum(0)
            self.capacity_inputs[table_name] = spin_box
            layout.addRow(QLabel(table_name), spin_box)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def accept(self):
        for table_name, spin_box in self.capacity_inputs.items():
            self.table_capacity[table_name] = spin_box.value()
        super().accept()

class DisplayTablesDialog(QDialog):
    def __init__(self, tables_with_counts_and_remaining, main_window):
        super().__init__()
        self.setWindowTitle("Tables and Name Counts")
        self.resize(400, 600)

        self.main_window = main_window
        layout = QVBoxLayout()

        self.table_list = QListWidget()
        for table, (count, remaining) in tables_with_counts_and_remaining.items():
            remaining_display = "∞" if remaining == float('inf') else remaining
            self.table_list.addItem(f"{table}: {count} names, {remaining_display} remaining")

        self.table_list.itemClicked.connect(self.item_clicked)

        layout.addWidget(self.table_list)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def item_clicked(self, item):
        table_name = item.text().split(':')[0]
        self.main_window.display_table_contents_by_display_name(table_name)
        self.accept()

class DisplayNamesDialog(QDialog):
    def __init__(self, table_name, names, main_window):
        super().__init__()
        self.setWindowTitle(f"Contents of Table: {table_name}")
        self.resize(400, 600)
        
        self.table_name = table_name
        self.names = names
        self.main_window = main_window
        
        layout = QVBoxLayout()
        
        self.name_list = QListWidget()
        self.name_list.addItems(names)
        self.name_list.setSelectionMode(QAbstractItemView.SingleSelection)
        
        layout.addWidget(self.name_list)
        
        self.remove_button = QPushButton("Remove Selected Name")
        self.remove_button.clicked.connect(self.remove_selected_name)
        
        layout.addWidget(self.remove_button)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)
        
        self.setLayout(layout)

    def remove_selected_name(self):
        selected_items = self.name_list.selectedItems()
        if selected_items:
            selected_name = selected_items[0].text()
            reply = QMessageBox.question(self, 'Remove Name', 
                                         f"Are you sure you want to remove '{selected_name}' from {self.table_name}?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    connection = mysql.connector.connect(
            host='localhost',
            user='MA',
            password='01158820082baba',
            database='f11'
                    )
                    cursor = connection.cursor()
                    cursor.execute(f"DELETE FROM {self.main_window.get_actual_name(self.table_name)} WHERE name = %s", (selected_name,))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    self.name_list.takeItem(self.name_list.row(selected_items[0]))
                    QMessageBox.information(self, "Success", f"'{selected_name}' removed successfully.")
                except mysql.connector.Error as error:
                    QMessageBox.critical(self, "Database Error", f"Error: {error}")





class WebSocketThread(QThread):
    server_started = Signal(str)

    def run(self):
        asyncio.run(self.start_server())

    async def start_server(self):
        try:
            await start_server()  # This should now refer to the above-defined start_server function
            self.server_started.emit("Server started on ws://0.0.0.0:8765")
        except Exception as e:
            self.server_started.emit(f"Server failed: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.websocket_thread = WebSocketThread()
        self.websocket_thread.server_started.connect(self.update_server_status)
        self.websocket_thread.start()

        self.server_status_label = QLabel("Starting WebSocket server...", self)
        self.ui.verticalLayout.addWidget(self.server_status_label)


        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btn_page_1.clicked.connect(self.show_page_1)
        self.ui.btn_page_2.clicked.connect(self.show_page_2)
        self.ui.btn_page_3.clicked.connect(self.show_page_3)
        self.ui.btn_page_4.clicked.connect(self.show_page_4)
        self.ui.btn_page_5.clicked.connect(self.show_page_5)
        self.ui.btn_page_6.clicked.connect(self.show_page_6)
        self.ui.pushButton_7.clicked.connect(lambda: on_pushButton_7_clicked(self))
        self.ui.pushButton_5.clicked.connect(self.save_to_mysql)
        self.ui.lineEdit_11.mousePressEvent = self.show_tables

        # Track layout initialization
        self.page_4_layout_set = False
        self.page_2_layout_set = False



        # Initialize containers
        self.database_tree_view_container = DatabaseTreeView()
        self.task_manager_window = None
        self.name_counter_app = None

        # Initialize table capacities
        self.table_capacity = {}
        self.table_counts = {}

        # Map display names to actual table names
        self.table_name_map = {
            "a1": "a1",
            " a2": "a2",
            "a3": "a3",
            " a4": "a4",
            "a5": "a5",
            "a6": "a6",
            "a7": "a7",
            " a8 ": "a8",
            " a9": "a9",
            " a10": "a10",
            " a11": "a11",
        }
        
        self.update_table_counts()

        self.set_default_capacities()

       
    def get_display_name(self, actual_name):
        for display_name, table_name in self.table_name_map.items():
            if table_name == actual_name:
                return display_name
        return actual_name

    def display_table_contents_by_display_name(self, display_name):
        actual_name = self.get_actual_name(display_name)
        try:
            connection = mysql.connector.connect(
                host='192.168.1.4',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()

            # Get column names
            cursor.execute(f"SHOW COLUMNS FROM {actual_name}")
            columns = cursor.fetchall()
            if not columns:
                raise ValueError("No columns found in the table.")
            
            # Print column names for debugging
            print("Columns:", columns)

            # Try to find a column that contains 'name'
            name_column = None
            for col in columns:
                if 'name' in col[0].lower():
                    name_column = col[0]
                    break

            # If no column with 'name' found, use the first column
            if not name_column:
                name_column = columns[0][0]
            
            # Print the selected column for debugging
            print("Selected column for names:", name_column)

            # Retrieve names
            cursor.execute(f"SELECT {name_column} FROM {actual_name}")
            names = [row[0] for row in cursor.fetchall()]
            cursor.close()
            connection.close()

            dialog = DisplayNamesDialog(display_name, names, self)
            dialog.exec()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error retrieving table contents: {err}")
        except ValueError as ve:
            QMessageBox.critical(self, "Error", f"Error: {ve}")


    def handle_websocket_message(self, message):
        # Handle the received WebSocket message here
        print(f"WebSocket message received: {message}")

    def show_page_1(self):
        print("Showing page 1")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

    def show_page_2(self):
        print("Showing page 2")
        self.set_page_2_layout()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def show_page_3(self):
        print("Showing page 3")
        self.clear_layout(self.ui.page_3)  # Clear the layout

        # Create a new layout for page 3
        layout = QVBoxLayout(self.ui.page_3)

        # Create a button and add it to the layout at the bottom
        bottom_button = QPushButton("عرض اسامي الوحدات", self.ui.page_3)
        bottom_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # Apply styles to the button
        bottom_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                padding: 20px;
                font-size: 18px;
                min-height: 50px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
        """)
        
        layout.addWidget(bottom_button)

        # Connect the button's clicked signal to display_tables method
        bottom_button.clicked.connect(self.display_tables)

        # Add the capacity setting button
        set_capacity_button = QPushButton("تحديد عدد السراير", self.ui.page_3)
        set_capacity_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        set_capacity_button.setStyleSheet("""
            QPushButton {
                background-color: #e67e22;
                color: white;
                border-radius: 10px;
                padding: 20px;
                font-size: 18px;
                min-height: 50px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
            QPushButton:pressed {
                background-color: #e74c3c;
            }
        """)
        
        layout.addWidget(set_capacity_button)
        
        # Connect the set capacity button to the set_table_capacities method
    
        set_capacity_button.clicked.connect(self.set_table_capacities)
    
        if self.table_counts and self.table_capacity:
           counts_label = QLabel(self.ui.page_3)
           counts_text = "<b>Current Table Counts and Capacities:</b><br>"
           for table_name, count in self.table_counts.items():
               remaining = self.table_capacity.get(table_name, float('inf')) - count
               counts_text += f"{self.get_display_name(table_name)}: {count} names, {remaining} remaining<br>"
           counts_label.setText(counts_text)
           layout.addWidget(counts_label)
       
        self.display_table_capacities(layout)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def show_page_4(self):
        print("Showing page 4")
        self.set_page_4_layout()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def show_page_5(self):
        print("Showing page 5")
        self.set_page_5_layout()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        self.toggle_page_5_fullscreen()

    def show_page_6(self):
        print("Showing page 6")
        if not self.task_manager_window:
            self.task_manager_window = TaskManagerWindow()
            if not self.ui.page_6.layout():
                layout = QVBoxLayout()
                self.ui.page_6.setLayout(layout)
            self.ui.page_6.layout().addWidget(self.task_manager_window)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
        self.task_manager_window.show()
        print("TaskManagerWindow should be visible on page 6")

    def set_page_4_layout(self):
        self.clear_layout(self.ui.page_4)
        my_form = MyForm()
        my_form_container = QWidget()
        my_form_layout = QVBoxLayout(my_form_container)
        my_form_layout.addWidget(my_form)
        self.ui.page_4.setLayout(my_form_layout)

    def set_page_2_layout(self):
        if not self.page_2_layout_set:
            page_2_layout = self.ui.page_2.layout()
            if self.database_tree_view_container and page_2_layout:
                page_2_layout.addWidget(self.database_tree_view_container)
                self.page_2_layout_set = True

    def set_page_5_layout(self):
        if not self.ui.page_5.layout():
            self.clear_layout(self.ui.page_5)
            mysql_viewer = MySQLViewer()
            self.ui.page_5.setLayout(QVBoxLayout())
            self.ui.page_5.layout().addWidget(mysql_viewer)

    def clear_layout(self, widget):
        layout = widget.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            QWidget().setLayout(layout)

    def toggle_page_5_fullscreen(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.page_5:
            self.showFullScreen()

    def show_tables(self, event):
        display_names = list(self.table_name_map.keys())
        dialog = TableListDialog(display_names)
        if dialog.exec() == QDialog.Accepted:
            selected_display_name = dialog.get_selected_table()
            if selected_display_name:
                self.selected_table = self.get_actual_name(selected_display_name)
                self.ui.lineEdit_11.setText(selected_display_name)


    def get_actual_name(self, display_name):
        return self.table_name_map.get(display_name, display_name)

    def set_selected_table(self):
        selected_table = self.ui.lineEdit_12.text()  # Or however you determine the table name
        if selected_table:
            self.selected_table = selected_table
        else:
             QMessageBox.warning(self, "Input Error", "Please enter a table name.")

    def save_to_mysql(self):
        if not self.selected_table:
            QMessageBox.warning(self, "Selection Error", "Please select a table first.")
            return

        table_name = self.selected_table
        if table_name not in self.table_counts:
            QMessageBox.warning(self, "Table Error", "Selected table is not tracked.")
            return

        if self.table_counts[table_name] >= self.table_capacity.get(table_name, float('inf')):
            QMessageBox.warning(self, "Capacity Error", f"Table '{table_name}' has reached its capacity.")
            return

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
        )
            cursor = connection.cursor()
            query = f"INSERT INTO {table_name} (namep, age, namef, namem, numberid, addears, numberf, namec, namer, timee, timex, g) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                self.ui.lineEdit_9.text(),
                self.ui.lineEdit_5.text(),
                self.ui.lineEdit_4.text(),
                self.ui.lineEdit_10.text(),
                self.ui.lineEdit_11.text(),
                self.ui.lineEdit_7.text(),
                self.ui.lineEdit_21.text(),
                self.ui.lineEdit_6.text(),
                self.ui.lineEdit_3.text(),
                self.ui.lineEdit.text(),
                self.ui.lineEdit_22.text(),
                self.ui.lineEdit_8.text()
        )

            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()

            self.table_counts[table_name] += 1  # Update the count
            QMessageBox.information(self, "Success", "Data saved successfully.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error saving data: {err}")

    def display_tables(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()
            tables_with_counts = {}

            for table in self.table_name_map.values():
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                tables_with_counts[table] = count

            cursor.close()
            connection.close()

            self.table_counts = tables_with_counts

            tables_with_display_names = {self.get_display_name(table): count for table, count in tables_with_counts.items()}
            dialog = DisplayTablesDialog(tables_with_display_names, self)
            dialog.exec()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error retrieving tables: {err}")

    def display_table_names(self):
        tables_with_counts = {self.get_display_name(table): self.table_counts.get(table, 0) for table in self.table_name_map.values()}
        dialog = DisplayTablesDialog(tables_with_counts, self)
        dialog.exec()
    def get_display_name(self, table_name):
        for display_name, actual_name in self.table_name_map.items():
            if actual_name == table_name:
                return display_name
        return table_name


    def set_table_capacities(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
        )
            cursor = connection.cursor()
        
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]

            dialog = SetTableCapacityDialog(table_names)
            if dialog.exec() == QDialog.Accepted:
                self.table_capacity = dialog.table_capacity
                self.save_table_capacities()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error retrieving table capacities: {err}")
   
    def set_table_capacities(self):
        dialog = SetTableCapacityDialog(self.table_name_map.keys())
        if dialog.exec() == QDialog.Accepted:
            self.table_capacity = dialog.table_capacity
            print("Updated table capacities:", self.table_capacity)
            # Here you can save the updated capacities if needed
            # self.save_table_capacities()
            self.update_ui_with_new_display_names()

   
    def update_ui_with_new_display_names(self):
        # Update any UI components that display the table names with the new display names
        self.show_page_3()
  
    def display_table_capacities(self, layout):
        for display_name, capacity in self.table_capacity.items():
            capacity_label = QLabel(f"{display_name}: {capacity}")
            layout.addWidget(capacity_label)

    def update_table_counts(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
        )
            cursor = connection.cursor()
            self.table_counts = {}

            for display_name, table_name in self.table_name_map.items():
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                self.table_counts[table_name] = count

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error retrieving table counts: {err}")


    def set_table_capacities(self):
        dialog = SetTableCapacityDialog(self.table_name_map.keys())
        if dialog.exec() == QDialog.Accepted:
           self.table_capacity = dialog.table_capacity
           self.save_table_capacities()
           self.update_ui_with_new_display_names()

    def display_tables(self):
        self.update_table_counts()
        tables_with_counts_and_remaining = {}

        for table, count in self.table_counts.items():
            capacity = self.table_capacity.get(table, float('inf'))
            remaining = capacity - count if capacity != float('inf') else '∞'
            tables_with_counts_and_remaining[table] = (count, remaining)

        tables_with_display_names = {
            self.get_display_name(table): (count, remaining)
            for table, (count, remaining) in tables_with_counts_and_remaining.items()
    }

        dialog = DisplayTablesDialog(tables_with_display_names, self)
        dialog.exec()
    def set_default_capacities(self):
        self.table_capacity = {
        "a1": 100,
        "a2": 100,
        "a3": 100,
        "a4": 100,
        "a5": 100,
        "a6": 100,
        "a7": 100,
        "a8": 100,
        "a9": 100,
        "a10": 100,
        "a11": 100,
    }


    def save_table_capacities(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()

            for table_name, capacity in self.table_capacity.items():
                sql = "REPLACE INTO table_capacities (table_name, capacity) VALUES (%s, %s)"
                cursor.execute(sql, (self.get_actual_name(table_name), capacity))

            connection.commit()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error saving capacities to MySQL: {err}")
        finally:
            cursor.close()
            connection.close()
    def load_table_counts(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()
            for actual_name in self.table_name_map.values():
                cursor.execute(f"SELECT COUNT(*) FROM {actual_name}")
                count = cursor.fetchone()[0]
                self.table_counts[actual_name] = count
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error loading table counts from MySQL: {err}")
        finally:
            cursor.close()
            connection.close()
    def save_to_mysql(self):
        if not self.selected_table:
            QMessageBox.warning(self, "Selection Error", "Please select a table first.")
            return

        if self.selected_table not in self.table_capacity:
            QMessageBox.warning(self, "Capacity Error", "Table capacity not set.")
            return

        if self.table_counts.get(self.selected_table, 0) >= self.table_capacity[self.selected_table]:
            QMessageBox.warning(self, "Capacity Error", "Table has reached its capacity limit.")
            return

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()
            sql = f"INSERT INTO {self.selected_table} (name) VALUES (%s)"
            val = (self.ui.lineEdit_12.text(),)
            cursor.execute(sql, val)
            connection.commit()

            self.table_counts[self.selected_table] = self.table_counts.get(self.selected_table, 0) + 1
            self.ui.lineEdit_12.clear()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error saving to MySQL: {err}")
        finally:
            cursor.close()
            connection.close()

    def save_table_capacities(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()

            for table_name, capacity in self.table_capacity.items():
                sql = "REPLACE INTO table_capacities (table_name, capacity) VALUES (%s, %s)"
                cursor.execute(sql, (self.get_actual_name(table_name), capacity))

            connection.commit()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error saving capacities to MySQL: {err}")
        finally:
            cursor.close()
            connection.close()
    def save_table_capacities(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()

            for table_name, capacity in self.table_capacity.items():
                sql = "REPLACE INTO table_capacities (table_name, capacity) VALUES (%s, %s)"
                cursor.execute(sql, (self.get_actual_name(table_name), capacity))

            connection.commit()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error saving capacities to MySQL: {err}")
        finally:
            cursor.close()
            connection.close()

    def load_table_counts(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()
            for actual_name in self.table_name_map.values():
                cursor.execute(f"SELECT COUNT(*) FROM {actual_name}")
                count = cursor.fetchone()[0]
                self.table_counts[actual_name] = count
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error loading table counts from MySQL: {err}")
        finally:
            cursor.close()
            connection.close()
    def save_to_mysql(self):
        if not self.selected_table:
            QMessageBox.warning(self, "Selection Error", "Please select a table first.")
            return

        if self.selected_table not in self.table_capacity:
            QMessageBox.warning(self, "Capacity Error", "Table capacity not set.")
            return

        if self.table_counts.get(self.selected_table, 0) >= self.table_capacity[self.selected_table]:
            QMessageBox.warning(self, "Capacity Error", "Table has reached its capacity limit.")
            return

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='MA',
                password='01158820082baba',
                database='f11'
            )
            cursor = connection.cursor()
            sql = f"INSERT INTO {self.selected_table} (name) VALUES (%s)"
            val = (self.ui.lineEdit_12.text(),)
            cursor.execute(sql, val)
            connection.commit()

            self.table_counts[self.selected_table] = self.table_counts.get(self.selected_table, 0) + 1
            self.ui.lineEdit_12.clear()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error saving to MySQL: {err}")
        finally:
            cursor.close()
            connection.close()

    def update_table_capacity(self, table_name, capacity):
        self.table_capacity[table_name] = capacity

    def update_server_status(self, status):
        self.server_status_label.setText(status)
        print(status)
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
