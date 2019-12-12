import homepage
import signin
from tkinter import*
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
    root.email_icon = ImageTk.PhotoImage(file="email.jpg")

    #----Variables----
    username=StringVar()
    password=StringVar()
    email=StringVar()


    bg_lbl =Label(root,image=root.bg_icon).pack()

    title=Label(root,text="Signup",font=("times new roman",40,"bold"),bg="black",fg="white",bd=20,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)

    login_frame=Frame(root,bg="white")
    login_frame.place(x=400,y=130)
    logolbl= Label(login_frame,image=root.login_icon,bd=0).grid(row=0,columnspan=2,pady=15)

    lbluser=Label(login_frame,text="Username",imag=root.user_icon,compound=LEFT,font=("times new roman",30,"bold")).grid(row=1,column=0,padx=20,pady=10)
    txtuser=Entry(login_frame,textvariable=username,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

    lblemail = Label(login_frame, text=" Email       ", imag=root.email_icon, compound=LEFT,font=("times new roman", 30, "bold")).grid(row=2, column=0, padx=20, pady=10)
    txtemail = Entry(login_frame, bd=5, textvariable=email, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

    lbluser = Label(login_frame, text="Password", imag=root.password_icon, compound=LEFT,font=("times new roman", 30, "bold")).grid(row=3, column=0, padx=20, pady=10)
    txtpassword = Entry(login_frame,show="*", bd=5,textvariable=password, relief=GROOVE, font=("", 15)).grid(row=3, column=1, padx=20)


    btn_login= Button(login_frame,text="Signup",width=20,command=lambda: login(root, username, password,email),font=("times new roman",18,"bold"),bg="black",fg="white").grid(row=4,columnspan=2,pady=10)
    create_account = Button(login_frame, text="Already have an account?", width=20, command=lambda: change(root), font=("times new roman", 18, "bold"),bg="black", fg="white").grid(row=5, columnspan=2, pady=10)



def change(root):
    root.destroy()
    signin.call()

def login(root, username, password,email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        passwd="",
        database="ebmp"
    )
    mycursor = mydb.cursor()

    name = username.get()
    password = password.get()
    email=email.get()

    if password == "" or name == "" or email == "":
        messagebox.showerror("Error","Enter Valid Data")
    else:
        sql = ("""SELECT * FROM user WHERE Username='%s'""" % name)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if len(myresult) >=1:
            messagebox.showerror("Error","Username is already taken")
        else:
            sql = "INSERT INTO user (Username, Password,Email) VALUES (%s, %s,%s)"
            val = (name, password,email)
            mycursor.execute(sql, val)
            mydb.commit()
            var=mycursor.rowcount
            if var >= 1:

                root.destroy()
                homepage.homepage1(name)

            else:
                messagebox.showerror("Error","Enter Valid Data")



def call():
    root=Tk()
    start(root)
    root.mainloop()