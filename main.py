# pyuic6 -x "D:\Documents\```GitHub\CIST 1620\PROJECT\accounts\accounts_gui.ui" -o "D:\Documents\```GitHub\CIST 1620\PROJECT\accounts\gui.py"
# pyside6-rcc "D:\Documents\```GitHub\CIST 1620\PROJECT\accounts\graphics\resources.qrc" -o "D:\Documents\```GitHub\CIST 1620\PROJECT\accounts\graphics\resources.py"
# from PyQt6 import QtCore

from logic import *

def main():   
    application = QApplication([])
    window = Logic()
    window.setWindowTitle('ATM')
    window.show()
    application.exec()
    
    
if __name__ == '__main__':
    main()
    