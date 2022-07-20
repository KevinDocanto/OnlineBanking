from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from app import App
import main_window


class SignUp(QMainWindow, App):
    def __init__(self):
        super().__init__()
        self.initUI()

    

    # Detects enter key press
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == Qt.Key_Return: 
            self.show()
        else:
            super().keyPressEvent(qKeyEvent)


      # Show main window when sign up button is pressed
    def show_new_window(self):
        self.db.execute2("""SELECT username
                   FROM clients
                   WHERE username=?""",
                (self.username.text(),))
        
        result = self.db.c.fetchone()

        message = QMessageBox(self)

        if result:
            message.setText("Username already exists!")
            message.setWindowTitle("Banking Online")
            message.exec()
            self.username.clear()
            self.password.clear()
            return
       
        
        self.db.execute1(f"""INSERT INTO clients VALUES ('{self.username.text()}', '{self.password.text()}') 
                        """)
         
        self.db.close()

        if self.another_window is None: 
            self.another_window = main_window.MainWindow()
            self.another_window.show()
            self.hide()

        else:
            self.another_window.close()  # Close window.
            self.another_window = None  # Discard reference.


    def initUI(self):
        # Positioning variables
        screen_width = self.width
        screen_height = self.height
        mid_screen = int(screen_width/2)
        input_width = 250
        input_height = 40

        self.insert_background(QLabel("", self), "img/background_login.jpg", screen_width, screen_height)


        
        # Container background
        container_background = QLabel("", self)
        container_background.move(mid_screen - 190, 100)
        self.insert_background(container_background, "img/background_container.jpg", 400, 400)

        # Add login title 
        self.login_title = QLabel("Sign up", self)
        self.login_title.setStyleSheet("font-size: 30px")
        self.login_title.move(mid_screen - 40, 140)
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


        # Sign up button
        self.finish = QPushButton(parent=self, text='Sign up')
        self.finish.clicked.connect(self.show_new_window)
        self.finish.move(mid_screen - 40, 400)

        # Display GUI
        self.show()
