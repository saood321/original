import homepage
import signup
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

def start(root,name):
    #----Images-----
    root.title("EBMP")
    root.geometry("1350x700+0+0")
    root.bg_icon = ImageTk.PhotoImage(file="img1.jpg")
    root.user_icon = ImageTk.PhotoImage(file="img2.png")
    root.password_icon = ImageTk.PhotoImage(file="img3.png")
    root.email_icon = ImageTk.PhotoImage(file="email.jpg")

    bg_lbl =Label(root,image=root.bg_icon).pack()
    newPassword=StringVar()
    oldPassword=StringVar()
    title=Label(root,text="Upgrade Password",font=("times new roman",40,"bold"),bg="black",fg="white",bd=20,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)

    login_frame=Frame(root,bg="white")
    login_frame.place(x=400,y=150)


    passlbl = Label(login_frame, text="New Password",imag=root.password_icon,compound=LEFT,font=("times new roman", 30, "bold")).grid(row=1, column=1, padx=20, pady=10)
    passtxt = Entry(login_frame, bd=5,show="*",textvariable=newPassword, relief=GROOVE, font=("", 15)).grid(row=1, column=2, padx=20)

    oldPasslbl = Label(login_frame, text="Old Password",imag=root.password_icon,compound=LEFT, font=("times new roman", 30, "bold")).grid(row=2, column=1, padx=20,pady=10)
    oldPasstxt = Entry(login_frame, bd=5, show="*", textvariable=oldPassword, relief=GROOVE, font=("", 15)).grid(row=2,column=2,padx=20)

    btn_upgrade= Button(login_frame,text="Upgrade",width=20,command=lambda :upgradefun(root,name,newPassword,oldPassword),font=("times new roman",18,"bold"),bg="black",fg="white").grid(row=3,columnspan=2,pady=10)
    create_account = Button(login_frame, text="Back", width=20, command=lambda: change(root,name), font=("times new roman", 18, "bold"),bg="black", fg="white").grid(row=4, columnspan=2, pady=10)



def change(root,name):
    root.destroy()
    homepage.homepage1(name)

def upgradefun(root,name, newPassword,oldPassword):
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        passwd="",
        database="ebmp"
    )
    new = newPassword.get()
    old = oldPassword.get()
    mycursor = mydb.cursor()

    sql = "UPDATE user SET Password = %s WHERE Password= %s AND Username=%s"
    val = (new, old,name)

    mycursor.execute(sql, val)

    mydb.commit()
    var = mycursor.rowcount
    if var >= 1:
        messagebox.showinfo("Success","Upgraded Successfully")
    else:
        messagebox.showerror("Error","Failed")



def callme(name):
    root=Tk()
    start(root,name)
    root.mainloop()