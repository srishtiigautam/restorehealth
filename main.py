import os
import sys
import hashlib
from turtle import Screen
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
# screen10 -> Patient_info_edit1_page
# screen11 -> Patient_info_edit2_page
# screen12 -> Feedback
# screen13 -> Staff_Logged_in_page

#------------------------------------------
#             HOME PAGE
#----------------------------------------------------------------------------------------------------------
#button1 -> Register
#button2 -> About
#button3 -> Feedback
#button4 -> Consult
#button5 -> Support
#button6 -> Contact
#button7 -> Nutrition
#button8 -> Mental Health
#button9 -> Sleep
#button10 -> Health & Fitness
#button11 -> Notification
#button12 -> 
#---------------------------------------------------------------------------------------------------------

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow,self).__init__()
        uic.loadUi("./home_window.ui",self)

           
        self.button1 = self.findChild(QPushButton, "Register_Button")
        self.button1.clicked.connect(self.register_call)

        self.button2 = self.findChild(QPushButton, "About_button")
        self.button2.clicked.connect(self.about_call)

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

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
    
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
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

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

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
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Feedback_Window(QMainWindow):
    def __init__(self):
        super(Feedback_Window, self).__init__()
        uic.loadUi("./Feedback_window.ui",self)

        
        self.button13 = self.findChild(QPushButton, "Home_Button")
        self.button13.clicked.connect(self.home_call)
           
        self.button1 = self.findChild(QPushButton, "Register_button")
        self.button1.clicked.connect(self.register_call)

        self.button2 = self.findChild(QPushButton, "About_Button")
        self.button2.clicked.connect(self.about_call)

        self.button4 = self.findChild(QPushButton, "Consult_Button")
        self.button4.clicked.connect(self.consult_call)
        
        self.button6 = self.findChild(QPushButton,"Contact_button")
        self.button6.clicked.connect(self.contact_call)


    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

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

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

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

    def Patient_info_edit_call(self,mobile,password):
        screen4 = Patient_info_edit_Window(mobile,password)
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
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
        self.Patient_info_edit_call(mobile,password) 
        

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
#button40 -> Login_submit_button3
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

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        self.button9 = self.findChild(QPushButton,"Register_Button")
        self.button9.clicked.connect(self.register_call)

        self.button18 = self.findChild(QPushButton,"Login_submit_button_1")
        self.button18.clicked.connect(self.login_submit_action1)

        self.button19 = self.findChild(QPushButton,"Contact_button")
        self.button19.clicked.connect(self.contact_call)

        self.button40 = self.findChild(QPushButton, "Login_submit_button_2")
        self.button40.clicked.connect(self.login_submit_action2)

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

    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def contact_call(self):
        screen5 = ContactWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def patient_info_display_call(self,mobile,password):
        screen6 = Patient_info_display_Window(mobile,password)
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def staff_logged_in_page_call(self):
        screen13 = Staff_Logged_in_page()
        widget.addWidget(screen13)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def login_submit_action1(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        mobile1 = self.findChild(QLineEdit,"mobile_entry_1").text()
        password_entry1 = self.findChild(QLineEdit,"password_entry_1").text()
        
        mycursor.execute("SELECT password FROM PATIENT_DATA WHERE MOBILE='%s'" %mobile1)
        fetched_password1 = (mycursor.fetchone())
        fetched_password1 = ''.join(fetched_password1)
        mydb.commit()
        if (fetched_password1 == password_entry1):
            self.patient_info_display_call(mobile1,password_entry1)            
        else:
            QMessageBox.about(self,"Error","Wrong Password!")
    def login_submit_action2(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        staff_id = self.findChild(QLineEdit, "staff_id_entry").text()
        staff_id = int(staff_id)
        password_entry2 = self.findChild(QLineEdit, "password_entry_2").text()

        mycursor.execute("SELECT password FROM STAFF_DATA WHERE staff_id={0}" .format(staff_id))
        fetched_password2 = (mycursor.fetchone())
        fetched_password2 = ''.join(fetched_password2)
        mydb.commit()
        if (fetched_password2 == password_entry2):
            self.staff_logged_in_page_call()
        else:
            QMessageBox.about(self,"Error","Wrong Password!")
       


#---------------------------------------------
#               STAFF LOGGED IN WINDOW
#---------------------------------------------
#button131 -> home
#button132 -> about
#button133 -> analytics
#button134 -> consult
#button135 -> support
#button136 -> contact
#button137 -> login-submit-button
#button140 -> Login_submit_button3
#button138 -> register
#button139 -> notification
#----------------------------------------------
class Staff_Logged_in_page(QMainWindow):
    def __init__(self):
        super(Staff_Logged_in_page, self).__init__()
        uic.loadUi("./staff_logged_in.ui", self)

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()

        rows = mycursor.execute("SELECT * FROM staff_data")
        data = mycursor.fetchall()

        # for row in data:
        #     self.addTable(MyConverter(row))
        
        mycursor.close()

    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
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

        self.button3 = self.findChild(QPushButton, "Feedback_Button")
        self.button3.clicked.connect(self.feedback_call)
        
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

    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
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

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

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
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
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

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

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
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
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

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        self.button78 = self.findChild(QPushButton, "Next_Button")
        self.button78.clicked.connect(self.next_page_call)

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
    def next_page_call(self):
        screen11 = Patient_info_edit2_Window(self.mobile,self.password)
        widget.addWidget(screen11)
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
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)



#---------------------------------------------
#              CONTACT WINDOW
#---------------------------------------------
# button81 -> home_button
# button82 -> about_button
# button83 -> analytics_button
# button84 -> support_button
# button85 -> contact_button
# button86 -> 
# button87 -> 
# button88 -> 
# button89 ->
#---------------------------------------------
class ContactWindow(QMainWindow):
    def __init__(self):
        super(ContactWindow, self).__init__()
        uic.loadUi("./Contact_window.ui", self)
        
        self.button81 = self.findChild(QPushButton,"Home_Button")
        self.button81.clicked.connect(self.home_call)

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        self.button82 = self.findChild(QPushButton,"About_Button")
        self.button82.clicked.connect(self.about_call)
        
    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
#---------------------------------------------
#              MENTAL_HEALTH WINDOW
#---------------------------------------------
# button91 -> home_button
# button92 -> about_button
# button93 -> analytics_button
# button94 -> support_button
# button95 -> contact_button
# button96 -> 
# button97 -> 
# button98 -> 
# button99 ->
#---------------------------------------------
class Mental_health_window(QMainWindow):
    def __init__(self):
        super(Mental_health_window, self).__init__()
        uic.loadUi("./Mental_Health.ui", self)

        self.button22 = self.findChild(QPushButton,"Home_Button")
        self.button22.clicked.connect(self.home_call)

        self.button23 = self.findChild(QPushButton,"About_Button")
        self.button23.clicked.connect(self.about_call)

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

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
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)

#---------------------------------------------
#               PATEINT_INFO_EDIT2 WINDOW
#---------------------------------------------
# button101 -> home_button
# button102 -> about_button
# button103 -> analytics_button
# button104 -> support_button
# button105 -> contact_button
# button106 -> previous_button
# button107 -> next_button
# button108 -> save_button
# button109 ->
#---------------------------------------------
class Patient_info_edit2_Window(QMainWindow):
    def __init__(self,User_Mobile,User_Password):
        super(Patient_info_edit2_Window, self).__init__()
        uic.loadUi("./Patient_info_edit2.ui",self)
        self.password = User_Password
        self.mobile = User_Mobile

        self.button106 = self.findChild(QPushButton, "Previous_Button")
        self.button106.clicked.connect(self.previous_page_call)

        self.button107 = self.findChild(QPushButton, "Next_Button")
        self.button107.clicked.connect(self.next_page_call)

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        self.button108 = self.findChild(QPushButton, "Save_button")
        self.button108.clicked.connect(self.submit_action)

        self.button101 = self.findChild(QPushButton, "Home_button")
        self.button101.clicked.connect(self.home_call)

        self.button102 = self.findChild(QPushButton, "About_button")
        self.button102.clicked.connect(self.about_call)
    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def next_page_call(self):
        screen11 = Patient_info_edit3_Window(self.mobile,self.password)
        widget.addWidget(screen11)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def previous_page_call(self):
        screen10 = Patient_info_edit_Window(self.mobile,self.password)
        widget.addWidget(screen10)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
    # siip = SIMILAR ILLNESS IN PAST
    # ahoh = ANY HISTORY OF HOSPITALIZATION
    # pm = PREVIOUS MEDICATIONS
    # ahos = ANY HISTORY OF SURGERY
    def submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        siip = self.findChild(QLineEdit, "SIIP_Entry").text()
        ahoh = self.findChild(QLineEdit, "AHOH").text()
        pm = self.findChild(QLineEdit,"previous_medication_Entry").text()
        ahos = self.findChild(QLineEdit, "AHOS_Entry").text()
        
        mycursor.execute("SELECT patient_id FROM PATIENT_DATA WHERE MOBILE='%s'" %self.mobile)
        patient_id = (mycursor.fetchone())
        patient_id = ''.join(patient_id)
        query2 = "UPDATE PATIENT_PERSONAL_INFO SET Similar_illness_in_past = %s, Hospitalization_history = %s, Previous_Medication = %s, Any_history_of_surgery = %s WHERE patient_id = %s"
        value2 = (siip,ahoh,pm,ahos,patient_id)
        mycursor.execute(query2, value2)
        mydb.commit()
        QMessageBox.about(self,"Sucess!","Data Inserted")

#---------------------------------------------
#               PATEINT_INFO_EDIT3 WINDOW
#---------------------------------------------
# button111 -> home_button
# button112 -> about_button
# button113 -> analytics_button
# button114 -> support_button
# button115 -> contact_button
# button116 -> previous_button
# button117 -> next_button
# button118 -> save_button
# button119 ->
#---------------------------------------------
class Patient_info_edit3_Window(QMainWindow):
    def __init__(self,User_Mobile,User_Password):
        super(Patient_info_edit3_Window, self).__init__()
        uic.loadUi("./Patient_info_edit3.ui",self)
        self.password = User_Password
        self.mobile = User_Mobile

        self.button116 = self.findChild(QPushButton, "Previous_Button")
        self.button116.clicked.connect(self.previous_page_call)

        self.button117 = self.findChild(QPushButton, "Next_Button")
        self.button117.clicked.connect(self.next_page_call)

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        self.button118 = self.findChild(QPushButton, "Save_button")
        self.button118.clicked.connect(self.submit_action)

        self.button111 = self.findChild(QPushButton, "Home_button")
        self.button111.clicked.connect(self.home_call)

        self.button112 = self.findChild(QPushButton, "About_button")
        self.button112.clicked.connect(self.about_call)
    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def next_page_call(self):
        screen11 = Patient_info_edit4_Window(self.mobile,self.password)
        widget.addWidget(screen11)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def previous_page_call(self):
        screen10 = Patient_info_edit2_Window(self.mobile,self.password)
        widget.addWidget(screen10)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #hosiif = history of similar illness in family
    #hoacd = history of any chronic disease
    def submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        hosiif = self.findChild(QLineEdit, "HOSIIF").text()
        hoacd = self.findChild(QLineEdit, "HOACD").text()
        
        
        mycursor.execute("SELECT patient_id FROM PATIENT_DATA WHERE MOBILE='%s'" %self.mobile)
        patient_id = (mycursor.fetchone())
        patient_id = ''.join(patient_id)
        query2 = "UPDATE PATIENT_PERSONAL_INFO SET History_of_similar_illness_in_family = %s, Chronic_disease_history = %s WHERE patient_id = %s"
        value2 = (hosiif,hoacd,patient_id)
        mycursor.execute(query2, value2)
        mydb.commit()
        QMessageBox.about(self,"Sucess!","Data Inserted")

#---------------------------------------------
#               PATEINT_INFO_EDIT4 WINDOW
#---------------------------------------------
# button121 -> home_button
# button122 -> about_button
# button123 -> analytics_button
# button124 -> support_button
# button125 -> contact_button
# button126 -> previous_button
# button127 -> next_button
# button128 -> save_button
# button129 ->
#---------------------------------------------
class Patient_info_edit4_Window(QMainWindow):
    def __init__(self,User_Mobile,User_Password):
        super(Patient_info_edit4_Window, self).__init__()
        uic.loadUi("./Patient_info_edit4.ui",self)
        self.password = User_Password
        self.mobile = User_Mobile

        self.button116 = self.findChild(QPushButton, "Previous_Button")
        self.button116.clicked.connect(self.previous_page_call)
        
        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)

        self.button118 = self.findChild(QPushButton, "Save_button")
        self.button118.clicked.connect(self.submit_action)

        self.button117 = self.findChild(QPushButton, "Next_Button")
        self.button117.clicked.connect(self.next_page_call)

        self.button111 = self.findChild(QPushButton, "Home_button")
        self.button111.clicked.connect(self.home_call)

        self.button112 = self.findChild(QPushButton, "About_button")
        self.button112.clicked.connect(self.about_call)
    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def next_page_call(self):
        screen11 = Patient_info_edit5_Window(self.mobile,self.password)
        widget.addWidget(screen11)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def previous_page_call(self):
        screen10 = Patient_info_edit3_Window(self.mobile,self.password)
        widget.addWidget(screen10)
        widget.setCurrentIndex(widget.currentIndex()+1)
    # siip = SIMILAR ILLNESS IN PAST
    # ahoh = ANY HISTORY OF HOSPITALIZATION
    # pm = PREVIOUS MEDICATIONS
    # ahos = ANY HISTORY OF SURGERY
    def submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()
        aam = self.findChild(QLineEdit, "AAM").text()
        ldom = self.findChild(QLineEdit, "LDOM").text()
        cl = self.findChild(QLineEdit,"CL").text()
        aomp = self.findChild(QLineEdit, "AOMP").text()
        
        mycursor.execute("SELECT patient_id FROM PATIENT_DATA WHERE MOBILE='%s'" %self.mobile)
        patient_id = (mycursor.fetchone())
        patient_id = ''.join(patient_id)
        query2 = "UPDATE PATIENT_PERSONAL_INFO SET Menage = %s, Last_Mendate = %s, Cycle_length = %s, MenProblem = %s WHERE patient_id = %s"
        value2 = (aam,ldom,cl,aomp,patient_id)
        mycursor.execute(query2, value2)
        mydb.commit()
        QMessageBox.about(self,"Sucess!","Data Inserted")

class Patient_info_edit5_Window(QMainWindow):
    def __init__(self,User_Mobile,User_Password):
        super(Patient_info_edit5_Window, self).__init__()
        uic.loadUi("./Patient_info_edit5.ui",self)
        self.password = User_Password
        self.mobile = User_Mobile

        self.button116 = self.findChild(QPushButton, "Previous_Button")
        self.button116.clicked.connect(self.previous_page_call)    

        self.button3 = self.findChild(QPushButton, "Feedback_button")
        self.button3.clicked.connect(self.feedback_call)    

        self.button118 = self.findChild(QPushButton, "Save_button")
        self.button118.clicked.connect(self.submit_action)

        self.button111 = self.findChild(QPushButton, "Home_button")
        self.button111.clicked.connect(self.home_call)

        self.button112 = self.findChild(QPushButton, "About_button")
        self.button112.clicked.connect(self.about_call)
    def home_call(self):
        screen1 = HomeWindow()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def about_call(self):
        screen3 = AboutWindow()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    # def next_page_call(self):
    #     screen11 = Patient_info_edit2_Window(self.mobile,self.password)
    #     widget.addWidget(screen11)
    #     widget.setCurrentIndex(widget.currentIndex()+1)
    def previous_page_call(self):
        screen10 = Patient_info_edit4_Window(self.mobile,self.password)
        widget.addWidget(screen10)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def feedback_call(self):
        screen12 = Feedback_Window()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def check_box_texter(self):
        print("yes")
    
    def submit_action(self):
        mydb = mc.connect(host="localhost",user="root",password="",database="restore_health")
        mycursor = mydb.cursor()

        self.tdap_check = self.findChild(QCheckBox, "TDAP")
        if (self.tdap_check.isChecked()):
            tdap = "yes"
        else:
            tdap = "no"

        self.mmr_check = self.findChild(QCheckBox, "MMR")
        if (self.mmr_check.isChecked()):
            mmr = "yes"
        else:
            mmr = "no"

        self.hep_b_check = self.findChild(QCheckBox, "HEP_B")
        if (self.hep_b_check.isChecked()):
            hep_b = "yes"
        else:
            hep_b = "no"

        self.hep_a_check = self.findChild(QCheckBox, "HEP_A")
        if (self.hep_a_check.isChecked()):
            hep_a = "yes"
        else:
            hep_a = "no"

        self.hpv_check = self.findChild(QCheckBox, "HPV")
        if (self.hpv_check.isChecked()):
            hpv = "yes"
        else:
            hpv = "no"
        self.influ_check = self.findChild(QCheckBox, "INFLU")
        if (self.influ_check.isChecked()):
            influ = "yes"
        else:
            influ = "no"
        pr = self.findChild(QLineEdit, "Past_Reports_Entry").text()
                
        mycursor.execute("SELECT patient_id FROM PATIENT_DATA WHERE MOBILE='%s'" %self.mobile)
        patient_id = (mycursor.fetchone())
        patient_id = ''.join(patient_id)
        query2 = "UPDATE PATIENT_PERSONAL_INFO SET TDAP = %s, MMR = %s, HEPATITIS_B = %s, HEPATITIS_A = %s, HPV = %s, INFLUENZA = %s, ANY_PAST_REPORTS = %s WHERE patient_id = %s"
        value2 = (tdap,mmr,hep_b,hep_a,hpv,influ,pr,patient_id)
        mycursor.execute(query2, value2)
        mydb.commit()
        QMessageBox.about(self,"Sucess!","Data Inserted")


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