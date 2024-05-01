from PyQt6.QtWidgets import *
from graphics.resources import *
from gui import *
import csv

class Banking_Interface(QMainWindow, Ui_ATM_Main):
    '''
    Class for adding logic for Eggshells Embargo Online Banking Service GUI.
    Responsible for handling the banking interface.
    '''
    
    TRANSLATE = QtCore.QCoreApplication.translate
    
    
    def __init__(self):
        '''
        Method to set default values for Banking_Interface object.
        '''
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
    def online_bank(self) -> None:
        '''
        Method called after user correctly enters an existing username and password.
        Switches to main banking interface for depositing or withdrawing money from the login screen.
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
        
        # Shows banking interface
        self.BANKIF_balance_error.setText('')
        self.BANKIF_balance_error.setVisible(True)
        self.BANKIF_deposit_button.setVisible(True)
        self.BANKIF_logout_button.setVisible(True)
        self.BANKIF_welcome_label.setVisible(True)
        self.BANKIF_withdraw_button.setVisible(True)
        self.BANKIF_welcome_label.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">{self.first_name} {self.last_name}, what would you like to do today?</span></p></body></html>"))
        self.BANKIF_welcome_label.setVisible(True)
        
        with open('account_information/account_information.csv', 'r+') as account_info:
            self.account_information = csv.reader(account_info)
            for row in self.account_information:
                if row[0] == self.card_number:
                    self.balance = float(row[2])
            
            
    def deposit(self) -> None:
        '''
        Method called after clicking the deposit button.
        '''
        
        self.BANKIF_amount_entry_deposit.clear()
        self.BANKIF_amount_entry_withdraw.clear()
        
        #Changes clicked button color
        self.BANKIF_withdraw_button.setStyleSheet("background-color: rgb(27, 48, 53); border:0 solid; color:white")
        self.BANKIF_deposit_button.setStyleSheet("background-color: rgb(150, 65, 67); border:0 solid; color:white")
        
        #Shows entry for user to input amount to deposit or withdraw from account
        self.BANKIF_balance_error.setText('')
        self.BANKIF_amount_label.setVisible(True)
        self.BANKIF_amount_entry_deposit.setVisible(True)
        self.BANKIF_amount_entry_withdraw.setVisible(False)
        self.BANKIF_balance_label.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Your balance is ${self.balance:.2f}</span></p></body></html>"))
        self.BANKIF_balance_label.setVisible(True)
        self.BANKIF_submit_button_withdraw.setVisible(False)
        self.BANKIF_submit_button_deposit.setVisible(True)
        
        
    def deposit_submit(self) -> None:
        '''
        Method called after clicking the submit button while on the deposit screen.
        '''
        
        self.BANKIF_balance_error.setText('')
        self.amount = self.BANKIF_amount_entry_deposit.text()
        
        try:
            self.amount = float(self.amount)
            if self.amount < 0:
                raise ValueError
        except ValueError:
            self.BANKIF_balance_error.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#640000;\">Amount must be numeric and greater than 0.</span></p></body></html>"))
        else:
            self.balance += self.amount
            
            self.BANKIF_balance_error.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p><span style=\" font-size:12pt; color:#640000;\">Deposited {self.amount:.2f}.</span></p></body></html>"))
            self.BANKIF_balance_label.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Your balance is ${self.balance:.2f}</span></p></body></html>"))
       
       
    def withdraw(self) -> None:
        '''
        Method called after clicking the withdraw button.
        '''
        
        self.BANKIF_amount_entry_deposit.clear()
        self.BANKIF_amount_entry_withdraw.clear()
        
        #Changes clicked button color
        self.BANKIF_deposit_button.setStyleSheet("background-color: rgb(27, 48, 53); border:0 solid; color:white")
        self.BANKIF_withdraw_button.setStyleSheet("background-color: rgb(150, 65, 67); border:0 solid; color:white")
        
        #Shows entry for user to input amount to deposit or withdraw from account
        self.BANKIF_amount_label.setVisible(True)
        self.BANKIF_amount_entry_deposit.setVisible(False)
        self.BANKIF_amount_entry_withdraw.setVisible(True)
        self.BANKIF_balance_label.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Your balance is ${self.balance:.2f}</span></p></body></html>"))
        self.BANKIF_balance_label.setVisible(True)
        self.BANKIF_balance_error.setText('')
        self.BANKIF_submit_button_deposit.setVisible(False)
        self.BANKIF_submit_button_withdraw.setVisible(True)
        
            
    def withdraw_submit(self) -> None:
        '''
        Method called after clicking the submit button while on the withdraw screen.
        '''
        
        self.BANKIF_balance_error.setText('')
        self.amount = self.BANKIF_amount_entry_withdraw.text()
        
        try:
            self.amount = float(self.amount)
            if self.amount < 0:
                raise ValueError
            elif self.balance - self.amount < 0:
                raise NameError
        except ValueError:
            self.BANKIF_balance_error.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#640000;\">Amount must be numeric and greater than 0.</span></p></body></html>"))
        except NameError:
            self.BANKIF_balance_error.setText(self.TRANSLATE("ATM_Main", "<html><head/><body><p><span style=\" font-size:12pt; color:#640000;\">Cannot withdraw more than balance.</span></p></body></html>"))
        else:
            self.balance -= self.amount
            
            self.BANKIF_balance_error.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p><span style=\" font-size:12pt; color:#640000;\">Withdrew {self.amount:.2f}.</span></p></body></html>"))
            self.BANKIF_balance_label.setText(self.TRANSLATE("ATM_Main", f"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Your balance is ${self.balance:.2f}</span></p></body></html>"))