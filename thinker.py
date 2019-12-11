from tkinter import*
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
class login_system:
    def __init__(self,root):
        #----Images-----
        self.root= root
        self.root.title("EBMP")
        self.root.geometry("1350x700+0+0")
        self.bg_icon = ImageTk.PhotoImage(file="img1.jpg")
        self.user_icon = ImageTk.PhotoImage(file="img2.png")
        self.password_icon = ImageTk.PhotoImage(file="img3.png")
        self.login_icon = ImageTk.PhotoImage(file="login.png")

        #----Variables----
        self.username=StringVar()
        self.password=StringVar()


        bg_lbl =Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login",font=("times new roman",40,"bold"),bg="black",fg="white",bd=20,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=400,y=150)
        logolbl= Label(login_frame,image=self.login_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(login_frame,text="Username",imag=self.user_icon,compound=LEFT,font=("times new roman",30,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(login_frame,textvariable=self.username,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lbluser = Label(login_frame, text="Password", imag=self.password_icon, compound=LEFT,font=("times new roman", 30, "bold")).grid(row=2, column=0, padx=20, pady=10)
        txtpassword = Entry(login_frame, bd=5,textvariable=self.password, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        btn_login= Button(login_frame,text="Login",width=20,command=self.login,font=("times new roman",18,"bold"),bg="black",fg="white").grid(row=3,columnspan=2,pady=10)
        create_account = Button(login_frame, text="Create new account", width=20, command=self.login, font=("times new roman", 18, "bold"),bg="black", fg="white").grid(row=4, columnspan=2, pady=10)




    def login(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="",
            passwd="",
            database="bse"
        )
        mycursor = mydb.cursor()

        name = self.username.get()
        password = self.password.get()
        sql = ("""SELECT * FROM customers WHERE name='%s' and address ='%s'""" % (name, password))
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) >= 1:
            print("loggedin")
            messagebox.showinfo("Message", "Logged in")

        else:
            messagebox.showerror("Error","Enter Valid Data")




root=Tk()
obj=login_system(root)
root.mainloop()