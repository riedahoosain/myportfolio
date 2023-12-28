# Build an Intelligent ChatBot with ChatGPT and PyQt

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow, QTextEdit
from PyQt6.QtGui import QAction, QIcon
from backend import ChatBot


class ChatBotWindow(QMainWindow):
    """Frontend Chat GUI"""

    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 480)
        self.chatbot = ChatBot()

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add Button
        self.submit_button = QPushButton("Send", self)
        self.submit_button.setGeometry(500, 340, 100, 40)
        self.submit_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me: {user_input}")
        self.input_field.clear()

        
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {response}")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
