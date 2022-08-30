import os
import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QWidget, QFileDialog, QGridLayout

# screen1 -> home window
# screen2 -> register
# screen3 -> about
# screen4 -> Login window
# screen5 -> Nutrition_page
# screen6 -> Patient_info_page
# screen7 -> Contact_page

#button1 -> Register
#button2 -> About
#button10 -> Nutrition
#button19 -> Contact

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow,self).__init__()
        uic.loadUi("./home_window.ui",self)

        self.button = self.findChild(QPushButton, "Register_Button")
        self.button.clicked.connect(self.register_call)

        self.button2 = self.findChild(QPushButton, "About_button")
        self.button2.clicked.connect(self.about_call)
        
        self.button10 = self.findChild(QPushButton,"Nutrition_button")
        self.button10.clicked.connect(self.nutrition_call)

        self.button19 = self.findChild(QPushButton,"Contact_button")
        self.button19.clicked.connect(self.contact_call)
        
    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def nutrition_call(self):
        screen5 = NutritionWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button3 -> Home
#button  -> login
#button21 -> Contact
class AboutWindow(QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        uic.loadUi("./About_page.ui",self)

        self.button3 = self.findChild(QPushButton, "Home_button")
        self.button3.clicked.connect(self.home_call)

        self.button4 = self.findChild(QPushButton, "Login_Button")
        self.button4.clicked.connect(self.login_call)

        self.button21 = self.findChild(QPushButton,"Contact_button")
        self.button21.clicked.connect(self.contact_call)

    def login_call(self):
        screen4 = LoginWindow()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button5 -> home
#button6 -> about
#button20 -> contact
class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        uic.loadUi("./register_window.ui", self)

        self.button5 = self.findChild(QPushButton,"Home_button")
        self.button5.clicked.connect(self.home_call)

        self.button6 = self.findChild(QPushButton, "About_button")
        self.button6.clicked.connect(self.about_call)

        self.button20 = self.findChild(QPushButton,"Contact_button")
        self.button20.clicked.connect(self.contact_call)

    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button7 -> home
#button8 -> about
#button9 -> register
#button18 -> patient_info
#button19 -> contact
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi("./Login_window.ui", self)
        
        self.button7 = self.findChild(QPushButton,"Home_Button")
        self.button7.clicked.connect(self.home_call)

        self.button8 = self.findChild(QPushButton,"About_Button")
        self.button8.clicked.connect(self.about_call)

        self.button9 = self.findChild(QPushButton,"Register_Button")
        self.button9.clicked.connect(self.register_call)

        self.button18 = self.findChild(QPushButton,"Login_button")
        self.button18.clicked.connect(self.patient_info_call)

        self.button19 = self.findChild(QPushButton,"Contact_button")
        self.button19.clicked.connect(self.contact_call)

    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def patient_info_call(self):
        screen6 = Patient_info_Window()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex()+1)


#button11 -> home
#button12 -> about
#button13 -> register
#button17 -> contact

class NutritionWindow(QMainWindow):
    def __init__(self):
        super(NutritionWindow, self).__init__()
        uic.loadUi("./Nutrition_page.ui", self)

        self.button11 = self.findChild(QPushButton,"Home_Button")
        self.button11.clicked.connect(self.home_call)

        self.button12 = self.findChild(QPushButton, "About_Button")
        self.button12.clicked.connect(self.about_call)

        self.button13 = self.findChild(QPushButton, "Register_button")
        self.button13.clicked.connect(self.register_call)

        self.button17 = self.findChild(QPushButton, "Contact_button")
        self.button17.clicked.connect(self.contact_call)

    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button14 -> home
#button15 -> about
#button16 -> contact
class Patient_info_Window(QMainWindow):
    def __init__(self):
        super(Patient_info_Window, self).__init__()
        uic.loadUi("./Patient_info_page.ui", self)

        self.button14 = self.findChild(QPushButton,"Home_button")
        self.button14.clicked.connect(self.home_call)

        self.button15 = self.findChild(QPushButton, "About_button")
        self.button15.clicked.connect(self.about_call)

        self.button16 = self.findChild(QPushButton, "Contact_button")
        self.button16.clicked.connect(self.contact_call)

    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)
#button17 -> home
#button18 -> about
class ContactWindow(QMainWindow):
    def __init__(self):
        super(ContactWindow, self).__init__()
        uic.loadUi("./Contact_window.ui", self)
        
        self.button17 = self.findChild(QPushButton,"Home_Button")
        self.button17.clicked.connect(self.home_call)

        self.button18 = self.findChild(QPushButton,"About_Button")
        self.button18.clicked.connect(self.about_call)

    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
app = QApplication(sys.argv)
widget = QStackedWidget()
mainwindow = HomeWindow()
widget.addWidget(mainwindow)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting...")