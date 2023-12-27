# A desktop PyQt6 GUI app for managing university student data with an SQL database backend.
# Connects to sqlite db
import sys
import sqlite3
import mysql.connector
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon


class DatabaseConnection:
    """Connect to Database"""

    def __init__(self, host="localhost", user="root", password="Zarah2013!", database="school"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """Connect to db method"""
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        return connection


class MainWindow(QMainWindow):
    """Main Menu"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        # File and Help Menu Bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        # File and Help submenu items
        add_student_action = QAction(
            QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        # This needs to be used if the menu does not show
        # about_action.setMenuRole(QAction.MenuRole.NoRole)

        # Add Table with 4 columns and column names
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Status Bar

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a cell click

        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        """Loads the status bar when user clicks table"""
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self):
        """Loads data from the sql database to the tables"""
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()        
        cursor.execute("SELECT * FROM students")
        query = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(query):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number,
                                   QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        """Loads the insert dialog"""
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        """Search Dialog"""
        search_dialog = SearchDialog()
        search_dialog.exec()

    def edit(self):
        """Edit Dialog"""
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        """Delete Dialog"""
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        """Loads about Dialog"""
        dialog = AboutDialog()
        dialog.exec()


class EditDialog(QDialog):
    """Edit Record Menu"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Record")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        index = main_window.table.currentRow()
        student_name = main_window.table.item(index, 1).text()

        # Get id from selected row
        self.student_id = main_window.table.item(index, 0).text()

        # Edit Student Name
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Edit Courses
        course_name = main_window.table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ["English", "Afrikaans", "Mathematics",
                   "Accounting", "Physics", "Computer Science", "Biology"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        # Edit Mobile Number
        mobile_number = main_window.table.item(index, 3).text()
        self.mobile_number = QLineEdit(mobile_number)
        self.mobile_number.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile_number)

        # Add Submit Button
        button = QPushButton("Submit")
        button.clicked.connect(self.edit_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def edit_student(self):
        """edit student data"""
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()
        student_id = self.student_id

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE Id = %s",
                       (name, course, mobile, student_id))
        connection.commit()
        cursor.close()
        connection.close()

        main_window.load_data()
        self.student_name.setText("")
        self.mobile_number.setText("")


class DeleteDialog(QDialog):
    """Delete Record Menu"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Record")

        layout = QGridLayout()
        confirmation = QLabel(
            "Are you sure that you want to delete this record?")
        button_yes = QPushButton("Yes")
        button_no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(button_yes, 1, 0)
        layout.addWidget(button_no, 1, 1)

        self.setLayout(layout)

        button_yes.clicked.connect(self.delete_record)
        button_no.clicked.connect(self.close)

    def delete_record(self):
        """Delete Record from db"""

        index = main_window.table.currentRow()
        student_id = main_window.table.item(index, 0).text()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE Id = %s", (student_id,))
        connection.commit()
        cursor.close()
        connection.close()

        main_window.load_data()
        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("Record has been deleted")
        confirmation_widget.exec()


class InsertDialog(QDialog):
    """Insert a new record dialog"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Record")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add Student Name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add Courses
        self.course_name = QComboBox()
        courses = ["English", "Afrikaans", "Mathematics",
                   "Accounting", "Physics", "Computer Science", "Biology"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add Mobile Number
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile_number)

        # Add Submit Button
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        """add student data"""
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, course, mobile) VALUES (%s,%s,%s)", (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()
        self.student_name.setText("")
        self.mobile_number.setText("")


class SearchDialog(QDialog):
    """ Search for a student Dialog Menu """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add Student Name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add Submit Button
        button = QPushButton("Search")
        button.clicked.connect(self.search_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_student(self):
        """Function that checks data for the search results"""
        name = self.student_name.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        result = cursor.fetchall()
        rows = list(result)
        items = main_window.table.findItems(
            name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            main_window.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()


class AboutDialog(QMessageBox):
    """About the App"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app was created while learning Python
        This is a student record system that stores Student data in a sqlite db
        You can modify the program if you would like to add more tables etc
        """
        self.setText(content)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
