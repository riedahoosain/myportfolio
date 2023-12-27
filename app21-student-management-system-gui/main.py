import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon


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
        connection = sqlite3.connect('database.db')
        query = connection.execute("SELECT * FROM students")
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
        search_dialog = SearchDialog()
        search_dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()


class EditDialog(QDialog):

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

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE Id = ?",
                       (name, course, mobile, student_id))
        connection.commit()
        cursor.close()
        connection.close()
        
        main_window.load_data()
        self.student_name.setText("")
        self.mobile_number.setText("")


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()


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
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, course, mobile) VALUES (?,?,?)", (name, course, mobile))
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
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute(
            "SELECT * FROM students WHERE name = ?", (name,))
        rows = list(result)
        items = main_window.table.findItems(
            name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            main_window.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
