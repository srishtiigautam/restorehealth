import os
import sys
import hashlib
import mysql.connector as mc
from PyQt5 import QtWidgets,uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import *



# screen1 -> home window
# screen2 -> register
# screen3 -> about
# screen4 -> Login window
# screen5 -> Nutrition_page
# screen6 -> Patient_info_display_page
# screen7 -> Contact_page
# screen8 -> Mental_health_page
# screen9 -> Consult_page
# screen10 -> Patient_info_edit_page

#------------------------------------------
#             HOME PAGE
#------------------------------------------
#button1 -> Register
#button2 -> About
#button3 -> Analytics
#button4 -> Consult
#button5 -> Support
#button6 -> Contact
#button7 -> Nutrition
#button8 -> Mental Health
#button9 -> Sleep
#button10 -> Health & Fitness
#button11 -> Notification
#button12 -> 
#----------------------------------------

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow,self).__init__()
        uic.loadUi("./home_window.ui",self)

           
        self.button1 = self.findChild(QPushButton, "Register_Button")
        self.button1.clicked.connect(self.register_call)

        self.button2 = self.findChild(QPushButton, "About_button")
        self.button2.clicked.connect(self.about_call)

        self.button4 = self.findChild(QPushButton, "Consult_button")
        self.button4.clicked.connect(self.consult_call)
        
        self.button7 = self.findChild(QPushButton,"Nutrition_button")
        self.button7.clicked.connect(self.nutrition_call)

        self.button6 = self.findChild(QPushButton,"Contact_button")
        self.button6.clicked.connect(self.contact_call)

        self.button8 = self.findChild(QPushButton,"Mental_health_button")
        self.button8.clicked.connect(self.mental_health_call)
    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def consult_call(self):
        screen9 = ConsultWindow()
        widget.addWidget(screen9)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def nutrition_call(self):
        screen5 = NutritionWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def mental_health_call(self):
        screen8 = Mental_health_window()
        widget.addWidget(screen8)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def contact_call(self):
        screen7 = ContactWindow()
        widget.addWidget(screen7)
        widget.setCurrentIndex(widget.currentIndex()+1)

#----------------------------------------
#             ABOUT PAGE
#----------------------------------------
#button13 -> Home
#button14  -> Analytics
#button15 -> Consult
#button16 -> Support
#button17 -> Contact
#button18 -> Login
#button19 -> Notification
#----------------------------------------
class AboutWindow(QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        uic.loadUi("./About_page.ui",self)

        self.button13 = self.findChild(QPushButton, "Home_button")
        self.button13.clicked.connect(self.home_call)

        self.button17 = self.findChild(QPushButton,"Contact_button")
        self.button17.clicked.connect(self.contact_call)

        self.button18 = self.findChild(QPushButton, "Login_Button")
        self.button18.clicked.connect(self.login_call)

        
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

#---------------------------------------------
#               REGISTER WINDOW
#---------------------------------------------
#button21 -> home
#button22 -> about
#button23 -> analytics
#button24 -> consult
#button25 -> support
#button26 -> contact
#button27 -> register-button
#button28 -> login
#button29 -> notification
#---------------------------------------------
class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        uic.loadUi("./register_window.ui", self)

        self.button21 = self.findChild(QPushButton,"Home_button")
        self.button21.clicked.connect(self.home_call)

        self.button22 = self.findChild(QPushButton, "About_button")
        self.button22.clicked.connect(self.about_call)

        self.button26 = self.findChild(QPushButton,"Contact_button")
        self.button26.clicked.connect(self.contact_call)

        self.button27 = self.findChild(QPushButton, "Register_Submit_Button")
        self.button27.clicked.connect(self.register_submit_action)

        self.button28 = self.findChild(QPushButton, "login_window_button")
        self.button28.clicked.connect(self.login_call)



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

    def login_call(self):
        screen4 = LoginWindow()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def patient_id_generator(self):
        file = open("id_file.txt", "r")
        old_id = int(file.readline())
        file.close()

        new_id = old_id+1
        file = open("id_file.txt","w")
        file.write(str(new_id))
        file.close()
        return new_id


    def register_submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        email = self.findChild(QLineEdit,"email_entry").text()
        password = self.findChild(QLineEdit,"password_entry").text()         
        mobile = self.findChild(QLineEdit,"mobile_number_entry").text()
        patient_id = self.patient_id_generator()        
        query = "INSERT INTO PATIENT_DATA(patient_id,email,mobile,password) values(%s,%s,%s,%s)"
        value = (patient_id,email,mobile,password)
        mycursor.execute(query, value)
        mydb.commit()
        QMessageBox.about(self,"Sucess!","Data Inserted")
        self.login_call() 
        

#---------------------------------------------
#               LOGIN WINDOW
#---------------------------------------------
#button31 -> home
#button32 -> about
#button33 -> analytics
#button34 -> consult
#button35 -> support
#button36 -> contact
#button37 -> login-submit-button
#button38 -> register
#button39 -> notification
#----------------------------------------------
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

        self.button18 = self.findChild(QPushButton,"Login_submit_button")
        self.button18.clicked.connect(self.login_submit_action)

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

    def patient_info_display_call(self,mobile,password):
        screen6 = Patient_info_display_Window(mobile,password)
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def login_submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        mobile = self.findChild(QLineEdit,"mobile_entry").text()
        password_entry = self.findChild(QLineEdit,"password_entry").text()
        
        mycursor.execute("SELECT password FROM PATIENT_DATA WHERE MOBILE='%s'" %mobile)
        fetched_password = (mycursor.fetchone())
        fetched_password = ''.join(fetched_password)
        mydb.commit()
        if (fetched_password == password_entry):
            self.patient_info_display_call(mobile,password_entry)
            
        else:
            QMessageBox.about(self,"Error","Wrong Password!")

#---------------------------------------------
#               CONSULT WINDOW
#---------------------------------------------
# button41 -> home_button
# button42 -> about_button
# button43 -> analytics_button
# button44 -> support_button
# button45 -> contact_button
# button46 -> yes_button
# button47 -> no_button
# button48 ->
# button49 ->
#---------------------------------------------
class ConsultWindow(QMainWindow):
    def __init__(self):
        super(ConsultWindow, self).__init__()
        uic.loadUi("./Consult_page.ui", self)

        self.button41 = self.findChild(QPushButton,"Home_Button")
        self.button41.clicked.connect(self.home_call)
        
        self.button42 = self.findChild(QPushButton, "About_Button")
        self.button42.clicked.connect(self.about_call)

        self.button45 = self.findChild(QPushButton, "Contact_Button")
        self.button45.clicked.connect(self.contact_call)

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

#---------------------------------------------
#               NUTRITION WINDOW
#---------------------------------------------
# button51 -> home_button
# button52 -> about_button
# button53 -> analytics_button
# button54 -> support_button
# button55 -> contact_button
# button56 -> yes_button
# button57 -> no_button
# button58 ->
# button59 ->
#---------------------------------------------

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

#---------------------------------------------
#               PATIENT_INFO_DISPLAY WINDOW
#---------------------------------------------
# button61 -> home_button
# button62 -> about_button
# button63 -> analytics_button
# button64 -> support_button
# button65 -> contact_button
# button66 -> edit_button
# button67 -> next_button
# button68 ->
# button69 ->
#---------------------------------------------
class Patient_info_display_Window(QMainWindow):
    def __init__(self,User_Mobile,User_Password):
        super(Patient_info_display_Window, self).__init__()
        uic.loadUi("./Patient_info_display.ui", self)

        self.mobile = User_Mobile
        self.password = User_Password

        self.button61 = self.findChild(QPushButton,"Home_button")
        self.button61.clicked.connect(self.home_call)

        self.button62 = self.findChild(QPushButton, "About_button")
        self.button62.clicked.connect(self.about_call)

        self.button65 = self.findChild(QPushButton, "Contact_button")
        self.button65.clicked.connect(self.contact_call)

        self.button66 = self.findChild(QPushButton, "Edit_button")
        self.button66.clicked.connect(self.patient_info_edit_call)

        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT patient_id FROM PATIENT_DATA WHERE MOBILE='%s'" %self.mobile)
        self.patient_id = (mycursor.fetchone())
        self.patient_id = ''.join(self.patient_id)
        
        mycursor.execute("SELECT name FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_name = (mycursor.fetchone())
        self.fetched_name = ''.join(self.fetched_name)
        
        self.id_display = self.findChild(QLabel, "Patient_id_show")
        self.id_display.setText("   "+self.patient_id)

        self.name_display = self.findChild(QLabel, "Name_show")
        self.name_display.setText("   "+self.fetched_name)

        mycursor.execute("SELECT dob FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_dob_tuple = mycursor.fetchone()
        self.fetched_dob = self.fetched_dob_tuple[0]
        self.day = self.fetched_dob.strftime("%d")
        self.month = self.fetched_dob.strftime("%m")
        self.year = self.fetched_dob.strftime("%Y")
        self.fetched_dob = self.fetched_dob.strftime("%d/%m/%Y")
        

        self.dob_display = self.findChild(QLabel, "DOB_show")
        self.dob_display.setText("   "+self.fetched_dob)

        mycursor.execute("SELECT sex FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_sex = mycursor.fetchone()
        self.fetched_sex = ''.join(self.fetched_sex)
        
        self.sex_display = self.findChild(QLabel, "Sex_show")
        self.sex_display.setText("   "+self.fetched_sex)

        mycursor.execute("SELECT height FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_height = mycursor.fetchone()
        self.fetched_height = ''.join(self.fetched_height)

        self.height_display = self.findChild(QLabel, "Height_show")
        self.height_display.setText("   "+self.fetched_height)


        mycursor.execute("SELECT weight FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_weight = mycursor.fetchone()
        self.fetched_weight = ''.join(self.fetched_weight)

        self.weight_display = self.findChild(QLabel, "Weight_show")
        self.weight_display.setText("   "+self.fetched_weight)

        mycursor.execute("SELECT martial_status FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_martial_status = mycursor.fetchone()
        self.fetched_martial_status = ''.join(self.fetched_martial_status)

        self.martial_status_display = self.findChild(QLabel, "Martial_Status_show")
        self.martial_status_display.setText("   "+self.fetched_martial_status)


        mycursor.execute("SELECT address FROM patient_personal_info WHERE patient_id='%s'" %self.patient_id)
        self.fetched_address = mycursor.fetchone()
        self.fetched_address = ''.join(self.fetched_address)

        self.address_display = self.findChild(QLabel, "Address_show")
        self.address_display.setText("   "+self.fetched_address)

        mydb.commit()

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
    def patient_info_edit_call(self):
        screen10 = Patient_info_edit_Window(self.mobile,self.password)
        widget.addWidget(screen10)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

#---------------------------------------------
#               PATIENT_INFO_EDIT WINDOW
#---------------------------------------------
# button71 -> home_button
# button72 -> about_button
# button73 -> analytics_button
# button74 -> support_button
# button75 -> contact_button
# button76 -> submit_button
# button77 -> reset_button
# button78 -> next_button
# button79 ->
#---------------------------------------------
class Patient_info_edit_Window(QMainWindow):
    def __init__(self,User_Mobile,User_Password):
        super(Patient_info_edit_Window, self).__init__()
        uic.loadUi("./Patient_info_edit.ui",self)
        self.password = User_Password
        self.mobile = User_Mobile

        self.button76 = self.findChild(QPushButton, "Save_button")
        self.button76.clicked.connect(self.submit_action)

        self.button71 = self.findChild(QPushButton, "Home_button")
        self.button71.clicked.connect(self.home_call)

        self.button72 = self.findChild(QPushButton, "About_button")
        self.button72.clicked.connect(self.about_call)


    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        name = self.findChild(QLineEdit, "Name_Entry").text()
        dob = self.findChild(QDateEdit,"DOB_Entry").text()
        sex = self.findChild(QComboBox, "Sex_entry").currentText()
        height = self.findChild(QLineEdit,"Height_Entry").text()
        weight = self.findChild(QLineEdit, "Weight_Entry").text()
        martial_status = self.findChild(QComboBox, "Martial_status_entry").currentText()
        address = self.findChild(QLineEdit, "Address_Entry").text()
        mycursor.execute("SELECT patient_id FROM PATIENT_DATA WHERE MOBILE='%s'" %self.mobile)
        patient_id = (mycursor.fetchone())
        patient_id = ''.join(patient_id)
        query2 = "INSERT INTO PATIENT_PERSONAL_INFO(patient_id,name,dob,sex,height,weight,martial_status,address) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        value2 = (patient_id,name,dob,sex,height,weight,martial_status,address)
        mycursor.execute(query2, value2)
        mydb.commit()
        QMessageBox.about(self,"Sucess!","Data Inserted")



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
        
#button22 ->home
#button23 ->about
#button24 ->analytics
#button25 ->consult
#button26 ->support
#button27 ->Contact
#button28 ->register

class Mental_health_window(QMainWindow):
    def __init__(self):
        super(Mental_health_window, self).__init__()
        uic.loadUi("./Mental_Health.ui", self)

        self.button22 = self.findChild(QPushButton,"Home_Button")
        self.button22.clicked.connect(self.home_call)

        self.button23 = self.findChild(QPushButton,"About_Button")
        self.button23.clicked.connect(self.about_call)

        self.button27 = self.findChild(QPushButton, "Contact_button")
        self.button27.clicked.connect(self.contact_call)

        self.button28 = self.findChild(QPushButton, "Register_button")
        self.button28.clicked.connect(self.register_call)
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
    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

        
app = QApplication(sys.argv)
widget = QStackedWidget()
mainwindow = HomeWindow()
widget.addWidget(mainwindow)
widget.setWindowTitle("restore_health")
widget.setWindowIcon(QtGui.QIcon("./Media/icon.png"))
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting...")