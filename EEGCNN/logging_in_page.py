from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk 
from tkinter import filedialog

import mysql.connector
from mysql.connector import Error
import time

import Result
project_name = "Evaluation of EEG signal for detecting epilepsy (SEIZURE)"

from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont
image = Image.open('SC.jpg')


########################################################################################    


def LOGIN_PAGE():
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="",
         database="database"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM login_info")
    L = mycursor.fetchall()

    login_page = Tk()
    login_page.geometry("1300x600+30+30")
    login_page.configure(background="#ffff8f")

    def LOGIN():

        def check_login():
            R_name = registration_no.get() #get password from entry
            R_password = psw.get() #get password from entry


            success = 0

            for x in range(0, len(L)):
                if(L[x]==(R_name, R_password) ):
                    success = 1


            if success == 1:
                print('Login Success')
                label2 = Label(login_page, text="Login Success")
                label2.configure(background="#fffff0")
                label2.configure(foreground="#00ff00")
                label2.config(font=("Courier", 15))
                label2.place(x = 750,y=500,height=50, width=500)
                login_page.update()
                time.sleep(2)                
                login_page.destroy()                
                Result.get()    

            else:
                print('Denied')
                label2 = Label(login_page, text="Login Fail")
                label2.configure(background="#fffff0")
                label2.configure(foreground="#ff0000")
                label2.config(font=("Courier", 15))
                label2.place(x = 750,y=500,height=50, width=500)
                login_page.update()
                time.sleep(2)
                login_page.destroy()


        photoimage = ImageTk.PhotoImage(image)
        Label(login_page, image=photoimage).place(x=0,y=0)

        label2 = Label(login_page, text=project_name)
        label2.configure(background="#ffffFf")
        label2.config(font=("Courier", 20))
        label2.place(x = 150,y=20,height=40, width=1000)

        label2 = Label(login_page, text="Login")
        label2.configure(background="#ffffFf")
        label2.config(font=("Courier", 25))
        label2.place(x = 750,y=150,height=40, width=500)

        label3 = Label(login_page, text="User id : ")
        label3.configure(background="#ffffff")
        label3.config(font=("Courier", 15))
        label3.place(x = 700,y=250,height=40, width=300)

        label3 = Label(login_page, text=" Password : ")
        label3.configure(background="#ffffff")
        label3.config(font=("Courier", 15))
        label3.place(x = 700,y=330,height=40, width=300)


        registration_no = StringVar()
        bank1Entry = Entry(login_page, textvariable=registration_no)
        bank1Entry.configure(background="#ffffe0")
        bank1Entry.place(x =1030,y=260,height=20, width=150)


        psw = StringVar()
        bank1Entry = Entry(login_page, textvariable=psw,show="*")
        bank1Entry.configure(background="#ffffe0")
        bank1Entry.place(x =1030,y=340,height=20, width=150)


        B1 = Button(login_page, text = "Login", command = check_login)
        B1.place(x = 930,y = 450 ,height=25, width=150)
        B1.configure(background="#fffff0")

        login_page.mainloop()

    LOGIN()

