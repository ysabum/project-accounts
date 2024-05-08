from PyQt6.QtWidgets import *
from graphics.resources import *
from gui import *
from logic_bankingInterface import *
from logic_signUp import *

import csv
import os

class Logic(Banking_Interface, Sign_Up):
    '''
    Class for adding logic for Eggshells Embargo Online Banking Service GUI.
    Responsible for handling the login screen.
    '''
    
    def __init__(self) -> None:
        '''
        Initializes Logic object.
        '''
        
        Banking_Interface.__init__(self)

        # Hides banking interface by default
        self.BANKIF_amount_entry_deposit.setVisible(False)
        self.BANKIF_amount_entry_withdraw.setVisible(False)
        self.BANKIF_amount_label.setVisible(False)
        self.BANKIF_balance_label.setVisible(False)
        self.BANKIF_balance_error.setVisible(False)
        self.BANKIF_deposit_button.setVisible(False)
        self.BANKIF_logout_button.setVisible(False)
        self.BANKIF_submit_button_deposit.setVisible(False)
        self.BANKIF_submit_button_withdraw.setVisible(False)
        self.BANKIF_welcome_label.setVisible(False)
        self.BANKIF_withdraw_button.setVisible(False)
        
        # Hides signup interface by default
        self.SIGNUP_background.setVisible(False)
        self.SIGNUP_backtologin.setVisible(False)
        self.SIGNUP_cardnumber_entry.setVisible(False)
        self.SIGNUP_cardnumber_label.setVisible(False)
        self.SIGNUP_deposit_entry.setVisible(False)
        self.SIGNUP_deposit_label.setVisible(False)
        self.SIGNUP_error_label.setVisible(False)
        self.SIGNUP_first_name_entry.setVisible(False)
        self.SIGNUP_first_name_label.setVisible(False)
        self.SIGNUP_last_name_entry.setVisible(False)
        self.SIGNUP_last_name_label.setVisible(False)
        self.SIGNUP_password_entry.setVisible(False)
        self.SIGNUP_password_label.setVisible(False)
        self.SIGNUP_pin_entry.setVisible(False)
        self.SIGNUP_pin_label.setVisible(False)
        self.SIGNUP_signup_button.setVisible(False)
        self.SIGNUP_signup_message.setVisible(False)
        self.SIGNUP_username_entry.setVisible(False)
        self.SIGNUP_username_label.setVisible(False)
        
        # Button events
        self.ATM_signin_button.clicked.connect(lambda:self.submit())
        self.ATM_signup_label.clicked.connect(lambda:self.sign_up())
        
        self.BANKIF_deposit_button.clicked.connect(lambda:self.deposit())
        self.BANKIF_withdraw_button.clicked.connect(lambda:self.withdraw())
        self.BANKIF_logout_button.clicked.connect(lambda:self.login_screen())
        
        self.BANKIF_submit_button_deposit.clicked.connect(lambda:self.deposit_submit())
        self.BANKIF_submit_button_withdraw.clicked.connect(lambda:self.withdraw_submit())
        
        self.SIGNUP_backtologin.clicked.connect(lambda:self.login_screen())
        self.SIGNUP_signup_button.clicked.connect(lambda:self.sign_up_submit())
     
         
    def submit(self) -> None:
        '''
        Method called when the sign in button is pushed on the main login screen.
        '''
    
        self.username = self.ATM_login_username_entry.text()
        self.password = self.ATM_login_password_entry.text()
        
        if self.username == '' or self.password == '':
            self.ATM_login_error_blankForm.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:9pt; color:#a10000;\">A username and password must be entered.</span></p></body></html>"))
        
        else:
            self.ATM_login_error_blankForm.setText('')

            with open('account_information/logins.csv', 'r') as logins:
                login_information = csv.reader(logins)
                
                for row in login_information:
                    individual_username = row[0]
                    individual_password = row[1]
                    
                    if self.username == individual_username and self.password == individual_password:
                        self.first_name = row[2]
                        self.last_name = row[3]
                        self.card_number = row[4]
                        self.pin = row[5]
                        
                        self.online_bank()
                    
                    else:
                        self.ATM_login_error_blankForm.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:9pt; color:#a10000;\">Incorrect username or password.</span></p></body></html>"))
        
        
    def login_screen(self) -> None:
        '''
        Method called when after user logs out.
        '''
        
        # Shows main login screen
        self.ATM_login_error_blankForm.setText('')
        self.ATM_ad.setVisible(True)
        self.ATM_login_background.setVisible(True)
        self.ATM_login_error_blankForm.setVisible(True)
        self.ATM_login_label.setVisible(True)
        self.ATM_login_password_entry.clear()
        self.ATM_login_password_entry.setVisible(True)
        self.ATM_login_password_label.setVisible(True)
        self.ATM_login_username_entry.clear()
        self.ATM_login_username_entry.setVisible(True)
        self.ATM_login_username_label.setVisible(True)
        self.ATM_signin_button.setVisible(True)
        self.ATM_signup_label.setVisible(True)
        
        # Hides banking interface
        self.BANKIF_amount_label.setVisible(False)
        self.BANKIF_amount_entry_deposit.setVisible(False)
        self.BANKIF_amount_entry_withdraw.setVisible(False)
        self.BANKIF_balance_error.setText('')
        self.BANKIF_balance_error.setVisible(False)
        self.BANKIF_balance_label.setVisible(False)
        self.BANKIF_deposit_button.setVisible(False)
        self.BANKIF_logout_button.setVisible(False)
        self.BANKIF_submit_button_deposit.setVisible(False)
        self.BANKIF_submit_button_withdraw.setVisible(False)
        self.BANKIF_welcome_label.setVisible(False)
        self.BANKIF_withdraw_button.setVisible(False)
        self.BANKIF_welcome_label.setText('')
        self.BANKIF_welcome_label.setVisible(False)
        
        self.BANKIF_withdraw_button.setStyleSheet("background-color: rgb(27, 48, 53); border:0 solid; color:white")
        self.BANKIF_deposit_button.setStyleSheet("background-color: rgb(27, 48, 53); border:0 solid; color:white")
        
        # Hides sign up interface by default and clears entries
        self.SIGNUP_background.setVisible(False)
        self.SIGNUP_backtologin.setVisible(False)
        self.SIGNUP_cardnumber_entry.setVisible(False)
        self.SIGNUP_cardnumber_label.setVisible(False)
        self.SIGNUP_deposit_entry.setVisible(False)
        self.SIGNUP_deposit_label.setVisible(False)
        self.SIGNUP_error_label.setText('')
        self.SIGNUP_error_label.setVisible(False)
        self.SIGNUP_first_name_entry.setVisible(False)
        self.SIGNUP_first_name_label.setVisible(False)
        self.SIGNUP_last_name_entry.setVisible(False)
        self.SIGNUP_last_name_label.setVisible(False)
        self.SIGNUP_password_entry.setVisible(False)
        self.SIGNUP_password_label.setVisible(False)
        self.SIGNUP_pin_entry.setVisible(False)
        self.SIGNUP_pin_label.setVisible(False)
        self.SIGNUP_signup_button.setVisible(False)
        self.SIGNUP_signup_message.setVisible(False)
        self.SIGNUP_username_entry.setVisible(False)
        self.SIGNUP_username_label.setVisible(False)
        
        self.SIGNUP_username_entry.clear()
        self.SIGNUP_password_entry.clear()
        self.SIGNUP_first_name_entry.clear()
        self.SIGNUP_last_name_entry.clear()
        self.SIGNUP_cardnumber_entry.clear()
        self.SIGNUP_pin_entry.clear()
        self.SIGNUP_deposit_entry.clear()