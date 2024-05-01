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
        
        self.SIGNUP_error_label.clear()
        
        if self.signup_username == '' or self.signup_password == '' or self.signup_first_name == '' or self.signup_last_name == '' or self.signup_cardnumber == '' or self.signup_pin == '' or self.signup_deposit == '':
            self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#a10000;\">Please fill out all forms.</span></p></body></html>"))
        else:
            if len(self.signup_cardnumber) != 16 or str(self.signup_cardnumber).isnumeric() == False:
                self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#a10000;\">Please input an accurate card number. Must be a 16 digit number.</span></p></body></html>"))
            elif len(self.signup_pin) != 4 or str(self.signup_pin).isnumeric() == False:
                self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#a10000;\">Please input an accurate pin number. Must be a 4 digit number.</span></p></body></html>"))
            else:
                try:
                    self.signup_deposit =  float(self.signup_deposit)
                    if self.signup_deposit <= 0:
                        raise ValueError
                except ValueError:
                    self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#a10000;\">Deposit amount must be numeric and greater than 0.</span></p></body></html>"))
                else:
                    duplicate_check = []
                    
                    with open('account_information/logins.csv', 'r') as logins:
                        logins_information = csv.reader(logins)
                        for row_login_information in logins_information:
                            for individual_logins in row_login_information:
                                if individual_logins == row_login_information[0] or individual_logins == row_login_information[4]:
                                    duplicate_check.append(individual_logins)
                    
                    if self.signup_username in duplicate_check:
                        self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#a10000;\">Username already exists. Please use another username.</span></p></body></html>"))
                    elif self.signup_cardnumber in duplicate_check:
                        self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#a10000;\">Card number belongs to another user's account. Please use another card number.</span></p></body></html>"))
                    else:
                        with open('account_information/logins.csv', 'a', newline = '') as logins:
                            write_logins = csv.writer(logins)
                            logins_information = [self.signup_username, self.signup_password, self.signup_first_name, self.signup_last_name, self.signup_cardnumber, self.signup_pin]
                            write_logins.writerow(logins_information)
                            
                        with open('account_information/account_information.csv', 'a', newline = '') as account_information_csv:
                            new_account_info = [self.signup_cardnumber, self.signup_pin, f'{self.signup_deposit:.2f}']
                            self.account_information_writer = csv.writer(account_information_csv)
                            self.account_information_writer.writerow(new_account_info)
             
                        # clear all forms from sign up
                        self.SIGNUP_username_entry.clear()
                        self.SIGNUP_password_entry.clear()
                        self.SIGNUP_first_name_entry.clear()
                        self.SIGNUP_last_name_entry.clear()
                        self.SIGNUP_cardnumber_entry.clear()
                        self.SIGNUP_pin_entry.clear()
                        self.SIGNUP_deposit_entry.clear()
                            
                        self.SIGNUP_error_label.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Signup successful. You may now return to the login screen to sign in.</span></p></body></html>"))
                
            #check is deposit is >0
        
        #open logins.csv -> check if username and cardnumber are unique
        #else successfully append to logins.csv and go back to login screen