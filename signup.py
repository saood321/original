import homepage
import signup
import thinker
from tkinter import*
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

def start(root):
    #----Images-----
    root.title("EBMP")
    root.geometry("1350x700+0+0")
    root.bg_icon = ImageTk.PhotoImage(file="img1.jpg")
    root.user_icon = ImageTk.PhotoImage(file="img2.png")
    root.password_icon = ImageTk.PhotoImage(file="img3.png")
    root.login_icon = ImageTk.PhotoImage(file="login.png")

    #----Variables----
    username=StringVar()
    password=StringVar()


    bg_lbl =Label(root,image=root.bg_icon).pack()

    title=Label(root,text="Signup",font=("times new roman",40,"bold"),bg="black",fg="white",bd=20,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)

    login_frame=Frame(root,bg="white")
    login_frame.place(x=400,y=150)
    logolbl= Label(login_frame,image=root.login_icon,bd=0).grid(row=0,columnspan=2,pady=20)

    lbluser=Label(login_frame,text="Username",imag=root.user_icon,compound=LEFT,font=("times new roman",30,"bold")).grid(row=1,column=0,padx=20,pady=10)
    txtuser=Entry(login_frame,textvariable=username,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

    lbluser = Label(login_frame, text="Password", imag=root.password_icon, compound=LEFT,font=("times new roman", 30, "bold")).grid(row=2, column=0, padx=20, pady=10)
    txtpassword = Entry(login_frame, bd=5,textvariable=password, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

    btn_login= Button(login_frame,text="Signup",width=20,command=lambda: login(root, username, password),font=("times new roman",18,"bold"),bg="black",fg="white").grid(row=3,columnspan=2,pady=10)
    create_account = Button(login_frame, text="Already have an account?", width=20, command=lambda: change(root), font=("times new roman", 18, "bold"),bg="black", fg="white").grid(row=4, columnspan=2, pady=10)



def change(root):
    root.destroy()
    thinker.call()

def login(root, username, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        passwd="",
        database="bse"
    )
    mycursor = mydb.cursor()

    name = username.get()
    password = password.get()
    sql = ("""SELECT * FROM customers WHERE name='%s' and address ='%s'""" % (name, password))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) >= 1:


        root.destroy()

        homepage.homepage1()

    else:
        messagebox.showerror("Error","Enter Valid Data")



def call():
    root=Tk()
    start(root)
    root.mainloop()