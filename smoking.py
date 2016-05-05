from datetime import datetime
import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QPushButton, QApplication)



class Smoke(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        
    def read_text():
    	f = []
    	f = open('s.txt').read().split('C')
    	f.reverse()
    	return ''.join(f)

    # also need add Smoking Minutes
    def initUI(self):
        self.lbl = QLabel(Smoke.read_text(), self)
        # without this f() QLable display badly 
        self.lbl.adjustSize()
        self.lbl.move(50, 150)

        self.btnGo = QPushButton('Go', self)
        self.btnWent = QPushButton('Went', self)
        self.btnWent.move(210, 0)
        self.btnGo.clicked.connect(self.go)
        self.btnWent.clicked.connect(self.went)

        self.setGeometry(9999, 0, 300, 550)
        self.setWindowTitle('=+=+=+=+=+=+=+=+=+=+=')
        self.show()

        # make one button witch check IN or OUT and write (need?)
    def go(self):        	
        f = open('s.txt', 'a')
        time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")
        f.write('C> '+time+'\n')
        f.close()

        self.lbl.setText(Smoke.read_text())
        self.lbl.adjustSize()

    def went(self):        	
        self.f = open('s.txt', 'a')
        time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")
        self.f.write('C< '+time+'\n')
        self.f.close()

        self.lbl.setText(Smoke.read_text())
        self.lbl.adjustSize()


    # def closeEvent(self, event):
        # reply = QMessageBox.question(self, 'Message',
        #     "quit?", QMessageBox.Yes |
        #     QMessageBox.No, QMessageBox.No)

        # if reply == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

# W           T            F
# if __name__ == '__main__':

app = QApplication(sys.argv)
ss = Smoke()
sys.exit(app.exec_())