from email.mime import image
from tkinter import *
import main
# from tkinter import ttk
# import tkinter as tk

win2 = Frame()
win2.title("Simulation") #title
win2.geometry("1280x720") #ขนาดจอ
# win1.configure(background='#E7E9F5') #bg
win2.resizable(False,False)

#icon
win2.iconbitmap("shooter.ico")

def backPage(event):
    win2.withdraw()
    main.win1.deiconify()
    

def closePage(event):
    win2.destroy()

#subsample(2,2)=ลดขนาดรูป zoom(2,2)=เพิ่มขนาดรูป
# create bg
canvas = Canvas(win2,width=1280,height=720)
canvas.pack()
bg=PhotoImage(file="memberPage.gif")
canvas.create_image(640,360,image=bg,anchor=CENTER)

back = PhotoImage(file="backbutton.png").subsample(2,2) # set image path
b = canvas.create_image(150,630,image=back)
canvas.tag_bind(b, "<Button-1>", backPage)

close = PhotoImage(file="closebutton.png").subsample(2,2) # set image path
c = canvas.create_image(1130,630,image=close)
canvas.tag_bind(c, "<Button-1>", closePage)

win2.withdraw()