import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QTimer
from random import randint

fonts=QFont("times", 12)

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(60,60,1500,900)
        self.setWindowTitle("JackPot")
        self.UI()

    def UI(self):
        #top label
        self.label=QLabel("Welcome To Jackpot!!!",self)
        self.label.move(500,20)
        self.label.setFont(QFont("times",20))
        #instruction label
        self.label1=QLabel("When all three slot gives the same numbers then you win the prize of same number.",self)
        self.label1.move(300,80)
        self.label1.setFont(fonts)
        self.label2=QLabel("When you hit 777, you hit the Jackpot.",self)
        self.label2.move(500,120)
        self.label2.setFont(QFont("Arial",14))


        #image
        self.image1=QLabel(self)
        self.image1.setPixmap(QPixmap("1.png"))
        self.image1.move(100,200)
        self.image1.resize(450,450)

        self.image2 = QLabel(self)
        self.image2.setPixmap(QPixmap("1.png"))
        self.image2.move(550, 200)
        self.image2.resize(450, 450)

        self.image3 = QLabel(self)
        self.image3.setPixmap(QPixmap("1.png"))
        self.image3.move(1000,200)
        self.image3.resize(450, 450)

        #playing button
        button1=QPushButton("Play",self)
        button1.move(500,750)
        button1.setFont(QFont("Times",14))
        button1.clicked.connect(self.start)

        button2=QPushButton("Stop",self)
        button2.move(700,750)
        button2.setFont(QFont("Times",14))
        button2.clicked.connect(self.stop)

        #changes in number
        self.timer=QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.HitIt)

        self.show()

    def start(self):
        self.timer.start()

    def HitIt(self):

        self.random1= randint(1,7)
        self.random2 = randint(1,7)
        self.random3 = randint(1,7)

        # first slot
        if self.random1 ==1:
            self.image1.setPixmap(QPixmap("1.png"))
        elif self.random1==2:
            self.image1.setPixmap(QPixmap("2.png"))
        elif self.random1 == 3:
            self.image1.setPixmap(QPixmap("3.png"))
        elif self.random1==4:
            self.image1.setPixmap(QPixmap("4.png"))
        elif self.random1==5:
            self.image1.setPixmap(QPixmap("5.jpg"))
        elif self.random1==6:
            self.image1.setPixmap(QPixmap("6.png"))
        else:
            self.image1.setPixmap(QPixmap("7.jpg"))

        #second Slot

        if self.random2 == 1:
            self.image2.setPixmap(QPixmap("1.png"))
        elif self.random2 == 2:
            self.image2.setPixmap(QPixmap("2.png"))
        elif self.random2 == 3:
            self.image2.setPixmap(QPixmap("3.png"))
        elif self.random2 == 4:
            self.image2.setPixmap(QPixmap("4.png"))
        elif self.random2 == 5:
            self.image2.setPixmap(QPixmap("5.jpg"))
        elif self.random2 == 6:
            self.image2.setPixmap(QPixmap("6.png"))
        else:
            self.image2.setPixmap(QPixmap("7.jpg"))

            # third slot
        if self.random3 == 1:
            self.image3.setPixmap(QPixmap("1.png"))
        elif self.random3 == 2:
            self.image3.setPixmap(QPixmap("2.png"))
        elif self.random3 == 3:
            self.image3.setPixmap(QPixmap("3.png"))
        elif self.random3 == 4:
            self.image3.setPixmap(QPixmap("4.png"))
        elif self.random3 == 5:
            self.image3.setPixmap(QPixmap("5.jpg"))
        elif self.random3 == 6:
            self.image3.setPixmap(QPixmap("6.png"))
        else:
            self.image3.setPixmap(QPixmap("7.jpg"))

    def stop(self):
        self.timer.stop()

        if self.random1==self.random2==self.random3:
            if self.random1==7 and self.random2==7 and self.random3==7:
                mbox = QMessageBox.information(self, "Result", "you won a JACKPOT")
            else:
                mbox = QMessageBox.information(self, "Result", "you won the number")

        else:
            mbox = QMessageBox.information(self, "Result!!", "Sorry! you Lose!! \n Do you want to try again?",QMessageBox.Yes | QMessageBox.No)
            if mbox==QMessageBox.No:
                sys.exit()


def main():
    App=QApplication(sys.argv)
    window= Windows()
    #window.start()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
