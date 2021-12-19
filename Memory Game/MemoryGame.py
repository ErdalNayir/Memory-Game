import os
from PyQt5.QtCore import* # QApplication oluşturmak için
import sys # sayfanın oluşması ve kapatılması için
from PyQt5 import*
from PyQt5.QtWidgets import*  # tableWidgetin kullanılması için
from PyQt5.QtGui import*
from PyQt5.QtCore import QTimer
import random as rn

class KullaniciArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 1074
        self.height = 671
        self.qtRectangle = self.frameGeometry()
        self.centerPoint=QDesktopWidget().availableGeometry().center()
        self.msg= QMessageBox()
        self.timer1=QTimer()
        self.timer1.timeout.connect(self.Bekle)
        self.timer2=QTimer()
        self.timer2.timeout.connect(self.GameControl)
        self.msg= QMessageBox()
        self.is_Continuing=False
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Memory Game")
        self.setFixedSize(self.width,self.height)
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())
        self.setWindowIcon(QIcon("icon.jfif"))
        self.myFont=QFont('Times', 10)
        self.myFont.setBold(True)

        self.Start = QPushButton('Start',self)
        self.Start.setFixedSize(311,71)
        self.Start.move(715,330)
        self.Start.clicked.connect(self.Basla)
        self.Start.setStyleSheet("""background-color: white;
                                       border-style: outset;
                                       border-radius: 5px; border: 2px groove gray;
                                    """)
        self.ReStart = QPushButton('Give Up',self)
        self.ReStart.setFixedSize(311,71)
        self.ReStart.move(715,410)
        self.ReStart.clicked.connect(self.PesEt)
        self.ReStart.setStyleSheet("""background-color: white;
                                       border-style: outset;
                                       border-radius: 5px; border: 2px groove gray;
                                    """)
        self.Lives= QLabel(self)
        self.Lives.setText("Lives: ")
        self.Lives.setFont(self.myFont)
        self.Lives.setFixedSize(75,36)
        self.Lives.move(715,245)
        self.Lives.setStyleSheet("background-color: rgba(0,0,0,0%)")

        self.Difficulty= QLabel(self)
        self.Difficulty.setText("Difficulty: ")
        self.Difficulty.setFont(self.myFont)
        self.Difficulty.setFixedSize(191,61)
        self.Difficulty.move(715,285)
        self.Difficulty.setStyleSheet("background-color: rgba(0,0,0,0%)")

        self.Score= QLabel(self)
        self.Score.setText("Score: ")
        self.Score.setFont(self.myFont)
        self.Score.setFixedSize(141,61)
        self.Score.move(715,260)
        self.Score.setStyleSheet("background-color: rgba(0,0,0,0%)")

        self.Buttons=[]
        for i in range(7):
            row=[]
            for j in range(7):
                row.append((QPushButton(self)))
            self.Buttons.append(row)
        y=90
        x=90
        for i in range(7):
            for j in range(7):
                self.Buttons[i][j].setGeometry(x*j+20,y*i+20,91,91)
                self.Buttons[i][j].setFont(QFont(QFont('Times', 17)))
                self.Buttons[i][j].setStyleSheet("background-color:rgb(225,225,225);color: rgb(225,225,225);")
                self.Buttons[i][j].setText("0")
                self.Buttons[i][j].setDisabled(True)
                self.Buttons[i][j].clicked.connect(self.RenkDegistir)
        self.ReStart.setDisabled(True)
        self.show()

    def RenkDegistir(self):
        button=self.sender()
        if button.text()=="0":
            button.setStyleSheet("background-color:rgb(0, 0, 74);color: rgb(0, 0,74);")
            button.setText("1")
        elif button.text()=="1":
            button.setStyleSheet("background-color:rgb(225,225,225);color: rgb(225,225,225);")
            button.setText("0")

    def Basla(self):
        if self.is_Continuing==False:
            self.lives=3
            self.difficulty="Easy"
            self.score=0
            self.Score.setText("Score: {}".format(self.score))
            self.Difficulty.setText("Difficulty: {}".format(self.difficulty))
            self.Lives.setText("Lives: {}".format(self.lives))
            self.is_Continuing=True
            self.Game()
        else:
            self.DisplayMessage("Game is running!","Your Turn is continuing",QMessageBox.Critical)

    def Game(self):
        self.x_coordinate=[]
        self.y_coordinate=[]
        self.Location=[]
        for i in range(7):
            for j in range(7):
                self.Buttons[j][i].setStyleSheet("background-color:rgb(225,225,225);color: rgb(225,225,225);")
                self.Buttons[j][i].setText("0")
                self.Buttons[j][i].setEnabled(False)

        if self.lives!=0:
            if self.score>=0 and self.score<50:
                for i in range(5):
                    x= rn.randint(0,6)
                    y=rn.randint(0,6)

                    loc="({},{})".format(x,y)
                    if loc not in self.Location:
                        self.x_coordinate.append(x)
                        self.y_coordinate.append(y)
                        self.Location.append(loc)
                        print(x,y)
                        self.Buttons[x][y].setStyleSheet("background-color:rgb(0, 0, 74);color:rgb(0, 0, 74);")
                        self.Buttons[x][y].setText("1")
                    else:
                        i-=1
            elif self.score>=50 and self.score<100:
                self.difficulty="Medium"
                self.lives=3
                self.Lives.setText(self.lives)
                self.Difficulty.setText("Difficulty: {}".format(self.difficulty))
                for i in range(7):
                    x= rn.randint(0,6)
                    y=rn.randint(0,6)
                    loc="({},{})".format(x,y)
                    if loc not in self.Location:
                        self.x_coordinate.append(x)
                        self.y_coordinate.append(y)
                        self.Location.append(loc)
                        print(x,y)
                        self.Buttons[x][y].setStyleSheet("background-color:rgb(0, 0, 74);color:rgb(0, 0, 74);")
                        self.Buttons[x][y].setText("1")
                    else:
                        i-=1

            elif self.score>=100 and self.score<150:
                self.difficulty="Hard"
                self.lives=3
                self.Lives.setText(self.lives)
                self.Difficulty.setText("Difficulty: {}".format(self.difficulty))
                for i in range(9):
                    x= rn.randint(0,6)
                    y=rn.randint(0,6)
                    loc="({},{})".format(x,y)
                    if loc not in self.Location:
                        self.x_coordinate.append(x)
                        self.y_coordinate.append(y)
                        self.Location.append(loc)
                        print(x,y)
                        self.Buttons[x][y].setStyleSheet("background-color:rgb(0, 0, 74);color:rgb(0, 0, 74);")
                        self.Buttons[x][y].setText("1")
                    else:
                        i-=1

            elif self.score>=150:
                self.difficulty="Extremely Hard"
                self.lives=3
                self.Lives.setText(self.lives)
                self.Difficulty.setText("Difficulty: {}".format(self.difficulty))
                for i in range(11):
                    x= rn.randint(0,6)
                    y=rn.randint(0,6)
                    loc="({},{})".format(x,y)
                    if loc not in self.Location:
                        self.x_coordinate.append(x)
                        self.y_coordinate.append(y)
                        self.Location.append(loc)
                        print(x,y)
                        self.Buttons[x][y].setStyleSheet("background-color:rgb(0, 0, 74);color:rgb(0, 0, 74);")
                        self.Buttons[x][y].setText("1")
                    else:
                        i-=1
        else:
            self.GameOver()
            self.timer2.stop()
            self.timer1.stop()
            return 0
        self.timer1.start(5000)
        self.timer2.start(15000)

    def GameControl(self):
        NumOfClrflBttns=0
        for i in range(7):
            for j in range(7):
                if self.Buttons[i][j].text()=="1":
                    NumOfClrflBttns+=1
        if NumOfClrflBttns==len(self.x_coordinate):
            for i in range(len(self.x_coordinate)):
                if self.Buttons[self.x_coordinate[i]][self.y_coordinate[i]].text()=="1":
                    self.Buttons[self.x_coordinate[i]][self.y_coordinate[i]].setStyleSheet("background-color:rgb(0, 255, 0);color:rgb(0, 255, 0);")
                else:
                    for i in range(len(self.x_coordinate)):
                        self.Buttons[self.x_coordinate[i]][self.y_coordinate[i]].setStyleSheet("background-color:rgb(0, 255, 0);color:rgb(0, 255, 0);")

                    for i in range(7):
                        for j in range(7):

                            self.ReStart.setDisabled(True)
                    self.lives=self.lives-1
                    self.Lives.setText("Lives: {}".format(self.lives))
                    self.DisplayMessage("Kalan Can","Kalan Canınız: {}".format(self.lives),QMessageBox.Information)
                    self.Game()
                    return 0
        else:
            for i in range(len(self.x_coordinate)):
                self.Buttons[self.x_coordinate[i]][self.y_coordinate[i]].setStyleSheet("background-color:rgb(0, 255, 0);color:rgb(0, 255, 0);")

            for i in range(7):
                for j in range(7):

                    self.ReStart.setDisabled(True)
            self.lives=self.lives-1
            self.Lives.setText("Lives: {}".format(self.lives))
            self.DisplayMessage("Kalan Can","Kalan Canınız: {}".format(self.lives),QMessageBox.Information)
            self.Game()
            return 0

        self.score=self.score+10
        self.Score.setText("Score: {}".format(self.score))
        self.DisplayMessage("Doğru!","Yeni Skorunuz: {}".format(self.score),QMessageBox.Information)
        self.Game()

    def Bekle(self):
        print(1)
        for i in range(7):
            for j in range(7):
                self.Buttons[j][i].setStyleSheet("background-color:rgb(225,225,225);color: rgb(225,225,225);")
                self.Buttons[j][i].setText("0")
                self.Buttons[j][i].setEnabled(True)
        self.ReStart.setEnabled(True)
        self.timer1.stop()

    def PesEt(self):
        result=self.showDialog()
        if result==1:
            self.Lives.setText("Lives: ")
            self.Difficulty.setText("Difficulty: ")
            self.Score.setText("Score: ")
            for i in range(7):
                for j in range(7):
                    self.Buttons[j][i].setStyleSheet("background-color:rgb(225,225,225);color: rgb(225,225,225);")
                    self.Buttons[j][i].setText("0")
                    self.Buttons[j][i].setEnabled(False)
            self.ReStart.setDisabled(True)
            self.is_Continuing=False
            self.DisplayMessage("Pes Ettiniz!","Oyun Sonu Skorunuz: {}".format(self.score),QMessageBox.Information)
            self.timer2.stop()
            self.timer1.stop()
        else:
            return 0

    def GameOver(self):
        self.Lives.setText("Lives: ")
        self.Difficulty.setText("Difficulty: ")
        self.Score.setText("Score: ")
        for i in range(7):
            for j in range(7):
                self.Buttons[j][i].setStyleSheet("background-color:rgb(225,225,225);color: rgb(225,225,225);")
                self.Buttons[j][i].setText("0")
                self.Buttons[j][i].setEnabled(False)
        self.ReStart.setDisabled(True)
        self.is_Continuing=False
        self.DisplayMessage("Oyun Bitti","Kaybettiniz! Skorunuz: {}".format(self.score),QMessageBox.Information)

    def showDialog(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Are You Sure ?")
        self.msg.setWindowTitle("Sure?")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = self.msg.exec_()
        if returnValue == QMessageBox.Ok:
            return 1
        else:
            return 0

    def DisplayMessage(self,title,text,Icon):
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.setIcon(Icon)
        x = self.msg.exec_()

def main():
    app = QApplication(sys.argv)
    ary = KullaniciArayuzu()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
