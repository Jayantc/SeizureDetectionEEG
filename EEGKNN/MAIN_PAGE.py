from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk 
from tkinter import filedialog

import mysql.connector
from mysql.connector import Error
import time

project_name = "Evaluation of EEG signal for detecting epilepsy (SEIZURE)"

from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont
image = Image.open('SC.jpg')

import logging_in_page
import registration_page
######################################################################################## 
   
def LOGIN_PAGE():
    login_page = Tk()
    login_page.geometry("1300x600+30+30")
    login_page.configure(background="#ffff8f")

    def LOGIN():

        def login_button():
            print("Login button")
            login_page.destroy()                
            logging_in_page.LOGIN_PAGE()    



        def registration_button():
            print("registration_button")
            login_page.destroy()                
            registration_page.registration()    

        def exit():
            global off
            off = 1
            login_page.destroy()
            
        photoimage = ImageTk.PhotoImage(image)
        Label(login_page, image=photoimage).place(x=0,y=0)

        label2 = Label(login_page, text=project_name)
        label2.configure(background="#ffffFf")
        label2.config(font=("Courier", 20))
        label2.place(x = 150,y=20,height=40, width=1000)


        B1 = Button(login_page, text = "Login", command = login_button)
        B1.place(x = 900,y = 210 ,height=40, width=200)
        B1.config(font=("Courier", 17))
        B1.configure(background="#fffff0")

        B1 = Button(login_page, text = "Registration", command = registration_button)
        B1.place(x = 900,y = 310 ,height=40, width=200)
        B1.config(font=("Courier", 17))
        B1.configure(background="#fffff0")

        B1 = Button(login_page, text = "Exit", command = exit)
        B1.place(x = 1150,y = 550 ,height=40, width=100)
        B1.config(font=("Courier", 17))
        B1.configure(background="#fffff0")

        login_page.mainloop()

    LOGIN()

global off
off = 0

while True:
    LOGIN_PAGE()
    if(off==1):
        break

