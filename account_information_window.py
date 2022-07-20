from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from app import App

    
class AccountInformation(QMainWindow, App):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.insert_background(QLabel("", self), "img/background_account.jpg", 1200, 800)
         

        layout = QHBoxLayout()
        widget = QWidget(self)
        transaction = QPushButton("New Transaction")
        withdraw = QPushButton("Withdraw")
        all_transactions = QPushButton("All Transactions")
        search_transactions = QPushButton("Search Transactions")


        layout.addWidget(transaction)
        layout.addWidget(search_transactions)
        layout.addWidget(all_transactions)
        layout.addWidget(withdraw)


        for i in range(layout.count()):
           layout.itemAt(i).widget().setFixedWidth(150)
           layout.itemAt(i).widget().setFixedHeight(150)

        widget.setLayout(layout)
        widget.setGeometry(0, 200, 1200, 300)
        widget.show()
