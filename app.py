from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from db import DB

class App:
    def __init__(self):
        self.title = 'Online Banking'
        self.another_window = None 
        self.left = 400
        self.top = 100
        self.width = 1200
        self.height = 800
        self.db = DB()
        self.dic = {}
        
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setGeometry(self.left, self.top, self.width, self.height)

    
    # Insert background
    def insert_background(self, widget, img_url, width, height):
        background_stylesheet = f'''
            background-image: url({img_url});
            background-repeat: no-repeat;
            background-position: center;
        '''

        widget.resize(width, height)
        widget.setStyleSheet(background_stylesheet)
    

    # Asks the user if they are sure they want to leave current window
    def closeEvent(self, event):
            message_box = QMessageBox(self)
            close = message_box.question(self, "Online Banking", "Are you sure you want to leave?",
                QMessageBox.Yes, QMessageBox.No)

            if close == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

            