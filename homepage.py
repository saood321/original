from tkinter import*
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import matplotlib.pyplot as plt


def homepage1(name):

    win = tk.Tk()  # Create instance 
    win.title("Python GUI")
    win.geometry("1350x700+0+0")
    win.bg_icon = ImageTk.PhotoImage(file="img1.jpg")
    win.camera = ImageTk.PhotoImage(file="camera.png")
    bg_lbl = Label(win, image=win.bg_icon).pack()


    upgrade_frame = Frame(win, bg="white")
    upgrade_frame.place(x=100, y=10)
    btn_upgrade = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="Upgrade Profile", command=camera, bg="black", fg="white").grid(row=0, column=0)

    login_frame = Frame(win, bg="white")
    login_frame.place(x=1100, y=10)
    btn_login = Button(login_frame, text="camera",width=200,height=70, command=camera, image=win.camera, compound=LEFT,
                       font=("times new roman", 20, "bold"), bg="black", fg="white").grid(row=0, column=0)

    win.mainloop()

def camera():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                image = cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                plt.imshow(image)
                plt.show()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

