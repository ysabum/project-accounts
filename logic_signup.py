from PyQt6.QtWidgets import *
from graphics.resources import *
from gui import *
import csv

class Sign_Up(QMainWindow, Ui_ATM_Main):
    '''
    Class for adding logic for Eggshells Embargo Online Banking Service GUI.
    Responsible for handling the interface to create new users.
    '''
    
    TRANSLATE = QtCore.QCoreApplication.translate
    
    
    def __init__(self) -> None:
        '''
        Method to set default values for Sign_Up object.
        '''
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
    def sign_up(self) -> None:
        '''
        Method called after user clicks the sign up button on the sign in screen.
        Switches to the sign up interface.
        '''
        
        # Hides main login screen
        self.ATM_ad.setVisible(False)
        self.ATM_forget_login_label.setVisible(False)
        self.ATM_login_background.setVisible(False)
        self.ATM_login_error_blankForm.setVisible(False)
        self.ATM_login_label.setVisible(False)
        self.ATM_login_password_entry.setVisible(False)
        self.ATM_login_password_label.setVisible(False)
        self.ATM_login_username_entry.setVisible(False)
        self.ATM_login_username_label.setVisible(False)
        self.ATM_signin_button.setVisible(False)
        self.ATM_signup_label.setVisible(False)
        
        # Show sign up screen
        self.SIGNUP_background.setVisible(True)
        self.SIGNUP_backtologin.setVisible(True)
        self.SIGNUP_cardnumber_entry.setVisible(True)
        self.SIGNUP_cardnumber_label.setVisible(True)
        self.SIGNUP_deposit_entry.setVisible(True)
        self.SIGNUP_deposit_label.setVisible(True)
        self.SIGNUP_error_label.setText('')
        self.SIGNUP_error_label.setVisible(True)
        self.SIGNUP_first_name_entry.setVisible(True)
        self.SIGNUP_first_name_label.setVisible(True)
        self.SIGNUP_last_name_entry.setVisible(True)
        self.SIGNUP_last_name_label.setVisible(True)
        self.SIGNUP_password_entry.setVisible(True)
        self.SIGNUP_password_label.setVisible(True)
        self.SIGNUP_pin_entry.setVisible(True)
        self.SIGNUP_pin_label.setVisible(True)
        self.SIGNUP_signup_button.setVisible(True)
        self.SIGNUP_signup_message.setVisible(True)
        self.SIGNUP_username_entry.setVisible(True)
        self.SIGNUP_username_label.setVisible(True)
        
        
    def sign_up_submit(self) -> None:
        '''
        Method called after user clicks the sign up button on the sign up interface.
        '''
        
        self.signup_username = self.SIGNUP_username_entry.text()
        self.signup_password = self.SIGNUP_password_entry.text()
        self.signup_first_name = self.SIGNUP_first_name_entry.text()
        self.signup_last_name = self.SIGNUP_last_name_entry.text()
        self.signup_cardnumber = self.SIGNUP_cardnumber_entry.text()
        self.signup_pin = self.SIGNUP_pin_entry.text()
        self.signup_deposit = self.SIGNUP_deposit_entry.text()
        
        #check if all forms are fills
        #check if cardnumber is 16 digits
        #check if pin is 4 digits
        #check is deposit is >0
        
        #open logins.csv -> check if username and cardnumber are unique
        #else successfully append to logins.csv and go back to login screen