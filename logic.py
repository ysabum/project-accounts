from PyQt6.QtWidgets import *
from graphics.resources import *
from gui import *
import csv

class Logic(QMainWindow, Ui_ATM_Main):
    '''
    Class for adding logic for Eggshells Embargo Online Banking Service (EEOBS) GUI.
    '''
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.ATM_signin_button.clicked.connect(lambda:self.submit())
        
        
    def submit(self):
        username = self.ATM_login_username_entry.text()
        password = self.ATM_login_password_entry.text()
        
        with open('account_information/test_logins.csv', 'r+') as logins:
            logins_information = csv.reader(logins)
            for individual_login_information in logins_information:
                individual_username, individual_password = individual_login_information[0], individual_login_information[1]
                if username == individual_username and password == individual_password:
                    print('OK!')
                    break
                else:
                    print('OOPS!')