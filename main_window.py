from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from app import App
import account_information_window
import sign_up_window

class MainWindow(QMainWindow, App):
    def __init__(self):
        super().__init__()
        self.title = 'Online Banking'
        self.initUI()


    # Check if username and password are correct
    def check_sign_in(self):
        self.success_message = QMessageBox(self)
        items = self.db.c.execute("SELECT * FROM clients").fetchall()
        for item in items:
            self.dic[item[0]] = item[1]
        
        
        if self.username.text() in self.dic and self.dic[self.username.text()] == self.password.text():
            self.success_message.setText("Success")
            self.success_message.setWindowTitle("Banking Online")
            self.success_message.exec()
            self.show_new_window(account_information_window.AccountInformation)

        else:
            self.success_message.setText("Invalid username or password")
            self.success_message.setWindowTitle("Banking Online")
            self.success_message.exec()
            self.username.clear()
            self.password.clear()


    # Check sign up is pressed
    def check_sign_up(self):
        if self.sign_up.isChecked():
            self.show_new_window(sign_up_window.SignUp)


    # Goes back to the main window
    def show_new_window(self, obj):
            self.another_window = obj()
            self.another_window.show()
            self.hide()


    # Detects enter key press
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == Qt.Key_Return: 
            self.check_sign_in()
        else:
            super().keyPressEvent(qKeyEvent)

      
    def initUI(self):
        # Title and Icon
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('img/icon.png'))

        # Create background
        screen_width = self.width
        screen_height = self.height
        self.insert_background(QLabel("", self), "img/background_login.jpg", screen_width, screen_height)

        mid_screen = int(screen_width/2)
        container_background = QLabel("", self)
        container_background.move(mid_screen - 190, 100)
        self.insert_background(container_background, "img/background_container.jpg", 400, 400)

        # Add login title 
        input_width = 250
        input_height = 40
        self.login_title = QLabel("Online Banking", self)
        self.login_title.setStyleSheet("font-size: 30px")
        self.login_title.move(mid_screen - self.login_title.width(), 140)
        self.login_title.resize(input_width, input_height)
        
        # Add username text
        self.username_title = QLabel("Username", self)
        self.username_title.move(mid_screen - self.username_title.width() - 20, 230)

        # Create username box
        self.username = QLineEdit(self)
        self.username.resize(input_width, input_height)
        self.username.move(mid_screen - self.username.width() + 130, 250)

        # Add password text
        screen_width = self.width
        self.password_title = QLabel("Password", self)
        self.password_title.move(mid_screen - self.password_title.width() - 18, 290)

        # Create password box
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.resize(input_width, input_height)
        self.password.move(mid_screen - self.password.width() + 130, 310)


        # Sign in button
        self.sign_in = QPushButton(parent=self, text='Sign in')
        self.sign_in.setCheckable(True)
        self.sign_in.clicked.connect(self.check_sign_in)
        self.sign_in.move(mid_screen - self.sign_in.width(), 400)

        # Sign up button
        self.sign_up = QPushButton(parent=self, text='Sign up')
        self.sign_up.setCheckable(True)
        self.sign_up.clicked.connect(self.check_sign_up)
        self.sign_up.move(mid_screen - self.sign_in.width() + 120, 400)


        # Display GUI 
        self.show()