from PyQt6.QtWidgets import *
from graphics.resources import *
from gui import *
from logic_bankingIF import *
from logic_signup import *
import csv
import os

class Logic(Banking_Interface, Sign_Up):
    '''
    Class for adding logic for Eggshells Embargo Online Banking Service GUI.
    Responsible for handling the login screen.
    '''
    
    def __init__(self) -> None:
        '''
        Method to set default values for Logic object.
        '''
        
        Banking_Interface.__init__(self)

        self.file_path_remove = 'account_information/account_information.csv'
        
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
        
        # unused asset
        self.ATM_forget_login_label.setVisible(False)
        
        # Button events
        self.ATM_signin_button.clicked.connect(lambda:self.submit())
        self.ATM_signup_label.clicked.connect(lambda:self.sign_up())
        
        self.BANKIF_deposit_button.clicked.connect(lambda:self.deposit())
        self.BANKIF_withdraw_button.clicked.connect(lambda:self.withdraw())
        self.BANKIF_logout_button.clicked.connect(lambda:self.logout())
        
        self.BANKIF_submit_button_deposit.clicked.connect(lambda:self.deposit_submit())
        self.BANKIF_submit_button_withdraw.clicked.connect(lambda:self.withdraw_submit())
        
        self.SIGNUP_backtologin.clicked.connect(lambda:self.login_screen())
        self.SIGNUP_signup_button.clicked.connect(lambda:self.sign_up_submit())
     
         
    def submit(self) -> None:
        '''
        Method called when the submit button is pushed on the main login screen.
        '''
    
        self.username = self.ATM_login_username_entry.text()
        self.password = self.ATM_login_password_entry.text()
        
        if self.username == '' or self.password == '':
            self.ATM_login_error_blankForm.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:9pt; color:#a10000;\">A username and password must be entered.</span></p></body></html>"))
        else:
            self.ATM_login_error_blankForm.setText('')
            with open('account_information/logins.csv', 'r+') as logins:
                self.logins_information = csv.reader(logins)
                for individual_login_information in self.logins_information:
                    individual_username, individual_password = individual_login_information[0], individual_login_information[1]
                    if self.username == individual_username and self.password == individual_password:
                        self.first_name = individual_login_information[2]
                        self.last_name = individual_login_information[3]
                        self.card_number = individual_login_information[4]
                        self.pin = individual_login_information[5]
                        
                        self.online_bank()
                    else:
                        self.ATM_login_error_blankForm.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:9pt; color:#a10000;\">Incorrect username or password.</span></p></body></html>"))
        
    
    def logout(self) -> None:
        '''
        Method called when user clicks the logout button.
        Saves changes made to balance and updates account_information.csv.
        '''
        
        self.new_account_information = [self.card_number, self.pin, f'{self.balance:.2f}']
        
        with open('account_information/account_information.csv', 'r+') as account_info:
            with open('account_information/new_account_information.csv', 'w', newline = '') as new_account_info:
                self.account_information = csv.reader(account_info)
                self.output_info = csv.writer(new_account_info)
                
                for row in self.account_information:
                    if row[0] == self.new_account_information[0] and row[1] == self.new_account_information[1]:
                        self.output_info.writerow(self.new_account_information)
                    else:
                        self.output_info.writerow(row)
        
        if os.path.exists(self.file_path_remove):
            os.remove(self.file_path_remove)
        os.rename('account_information/new_account_information.csv', 'account_information/account_information.csv')
        
        self.login_screen()
        
        
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
        
        # Hides signup interface by default
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
        
