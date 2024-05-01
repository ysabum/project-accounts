from logic import *
import sys

def main():   
    application = QApplication([])
    window = Logic()
    window.setWindowTitle('ATM')
    window.setWindowIcon(QtGui.QIcon(":/ATM_graphics/atm_cash-point.png"))
    window.show()
    application.exec()
    sys.exit()
    
if __name__ == '__main__':
    main()
    