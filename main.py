from email.mime import image
# from platform import freedesktop_os_release
from tkinter import *
from calculation import simulationCal
import math
import graphSim

win1 = Tk()
win1.title("The Amazing Circus: Projectile Simulation") #title
win1.geometry("1280x720") #ขนาดจอ
# win1.configure(background='#E7E9F5') #bg
win1.resizable(False,False)

#icon
win1.iconbitmap("shooter.ico")

#startPage
#subsample(2,2)=ลดขนาดรูป zoom(2,2)=เพิ่มขนาดรูป
# create bg
canvas = Canvas(win1,width=1280,height=720)
canvas.pack()
bg=PhotoImage(file="background-01.png")
canvas.create_image(640,360,image=bg,anchor=CENTER)

# create purpleFrame
purpleFrame = PhotoImage(file="newinput.png") # set image path
frame = canvas.create_image(1100,220,image=purpleFrame)
# canvas.tag_bind(frame)

# create purpleFrame2
purpleFrame2 = PhotoImage(file="newoutput.png") # set image path
frame2 = canvas.create_image(1100,450,image=purpleFrame2)
# canvas.tag_bind(frame2)

# create goal
goal = PhotoImage(file="goal.png") # set image path
canvas.create_image(1100,600,image=goal)

# create shoot
shoot = PhotoImage(file="shooterGraph2.png")
canvas.create_image(210,530,image=shoot)

# create output
# def button_function(event):
#     print("button pressed")
def open_popup():
    top= Toplevel(win1)
    top.geometry("250x124")
    top.title("Warning!!")
    top.iconbitmap("warning.ico")
    # Label(top,text= "Out Of Range").place(x = 85 , y = 30)
    Label(top,text= "Please Check Your Input Again").place(x = 40 , y = 50)
    top.resizable(False,False)
    box_xaxis.delete(0,END)
    # box_yaxis.delete(0,END)
    box_mass.delete(0,END)
    box_springconst.delete(0,END)
    box_springAmount.delete(0,END)

def nextPage(event):
    win2 = Toplevel(win1)
    win2.title("Member") #title
    win2.geometry("1280x720") #ขนาดจอ
    # win1.configure(background='#E7E9F5') #bg
    win2.resizable(False,False)

    #icon
    win2.iconbitmap("shooter.ico")
    
    canvas = Canvas(win2,width=1280,height=720)
    canvas.pack()
    bgImg=PhotoImage(file="memberPage.png")
    canvas.create_image(640,360,image=bgImg,anchor=CENTER)
    canvas.image = bgImg
    
    def closePage(event):
        win2.destroy()

    #subsample(2,2)=ลดขนาดรูป zoom(2,2)=เพิ่มขนาดรูป
    # create bg
    
    # canvas = Canvas(win2,width=1280,height=720)
    # canvas.pack()
    # bg=PhotoImage(file="background-01.png")
    # # Label(win2, image=bg)
    # # background.grid(row=0,column=1,padx=10,pady=10)
    # canvas.create_image(640,360,anchor=CENTER)
    # canvas.image = bg

    # back = PhotoImage(file="backbutton.png").subsample(2,2) # set image path
    # b = canvas.create_image(150,630,image=back)
    # canvas.tag_bind(b, "<Button-1>", backPage)

    close = PhotoImage(file="closebutton.png").subsample(2,2) # set image path
    c = canvas.create_image(1130,630,image=close)
    canvas.tag_bind(c, "<Button-1>", closePage)
    c.image = close
    
def saveData(event):
    checkInput = False
    try:
        if 0<=float(box_xaxis.get())<=3.26:
            xaxis = float(box_xaxis.get())
            print(xaxis)
        else:
            checkInput=True
        # if float(box_yaxis.get())==0.2:
        #     yaxis = float(box_yaxis.get())
        #     print(yaxis)
        # else:
        #     checkInput=True
        if 0 < float(box_mass.get()) <= 1000:
            mass = float(box_mass.get())
            print(mass)
        else:
            checkInput=True
        if 0<=float(box_springconst.get())<=2500:
            springconst = float(box_springconst.get())
            print(springconst)
        else:
            checkInput=True
        if 0<=int(box_springAmount.get())<=20: 
            springAmount = int(box_springAmount.get())
            print(springAmount)
        else:
            checkInput=False
        if checkInput:
            open_popup()
        
        # if yaxis/xaxis > math.cos(60 * (math.pi/180)):
        #     open_popup()

        distanceX = simulationCal(xaxis,springconst,springAmount,9.81,mass)
        initialVelo = distanceX.projectileCal()
        lenX = distanceX.springCal()
        time = distanceX.timeCal()
        file = open("saveData.txt","w")
    
        file.write("x axis: " + str(xaxis) + " m" + "\n")
        file.write("y axis: " + "0.2" + " m" + "\n")
        file.write("mass: " + str(mass) + " g"+ "\n")
        file.write("spring constant: " + str(springconst) + " N/m" + "\n")
        file.write("spring amount: " + str(springAmount) + "\n")
        file.write("initial velocity: " + str(initialVelo) + " m/s" + "\n")
        file.write("time: " + str(time) + " s" + "\n")
        file.write("spring length: " + str(lenX) + " m" + "\n")
        file.write("------------------------------------------------------" + "\n")
        file.close()

    except ValueError:
        open_popup()
        print("run except")

Save = PhotoImage(file="savebutton.png") # set image path
s = canvas.create_image(180,170,image=Save)
canvas.tag_bind(s, "<Button-1>", saveData)

def button_clear(event):
    box_iniVeloLabel.config(state='normal')
    box_timeLabel.config(state='normal')
    box_springLenLabel.config(state='normal')
    box_xaxis.delete(0,END)
    # box_yaxis.delete(0,END)
    box_mass.delete(0,END)
    box_springconst.delete(0,END)
    box_springAmount.delete(0,END)
    box_iniVeloLabel.delete(0,END)
    box_timeLabel.delete(0,END)
    box_springLenLabel.delete(0,END)
    box_iniVeloLabel.config(state='disabled')
    box_timeLabel.config(state='disabled')
    box_springLenLabel.config(state='disabled')

def calClick(event): #check range
    checkInput = False
    try:
        if 0<=float(box_xaxis.get())<=10:
            xaxis = float(box_xaxis.get())
            print(xaxis)
        else:
            checkInput=True
        # if 0<=float(box_yaxis.get())<=10:
        #     yaxis = float(box_yaxis.get())
        #     print(yaxis)
        # else:
        #     checkInput=True
        if 0 < float(box_mass.get()) <= 1000:
            mass = float(box_mass.get())
            print(mass)
        else:
            checkInput=True
        if 0<=float(box_springconst.get())<=2500:
            springconst = float(box_springconst.get())
            print(springconst)
        else:
            checkInput=True
        if 0<=int(box_springAmount.get())<=20: 
            springAmount = int(box_springAmount.get())
            print(springAmount)
        else:
            checkInput=True
        # if checkInput or yaxis/xaxis > math.cos(60 * (math.pi/180)):
        #     open_popup()
        if checkInput:
            open_popup()

        distanceX = simulationCal(xaxis,springconst,springAmount,9.81,mass)
        initialVelo = distanceX.projectileCal()
        lenX = distanceX.springCal()
        time = distanceX.timeCal()
        box_iniVeloLabel.config(state='normal')
        box_iniVeloLabel.insert(0, str(initialVelo))
        box_iniVeloLabel.config(state='disabled')
        box_timeLabel.config(state='normal')
        box_timeLabel.insert(0, str(time))
        box_timeLabel.config(state='disabled')
        box_springLenLabel.config(state='normal')
        box_springLenLabel.insert(0, str(lenX))
        box_springLenLabel.config(state='disabled')
        # iniVeloLabel = Label(win1, text = str(initialVelo)).place(x = 1118, y = 416)
        # springLenLabel = Label(win1, text = str(lenX)).place(x = 1118, y = 462)
        # timeLabel = Label(win1, text = str(time)).place(x = 1118, y = 440)
    except ValueError:
        open_popup()
        print("run except")

def showGraph(event):
    checkInput = False
    try:
        if 0<=float(box_xaxis.get())<=10:
            xaxis = float(box_xaxis.get())
            print(xaxis)
        else:
            checkInput=True
        # if 0<=float(box_yaxis.get())<=10:
        #     yaxis = float(box_yaxis.get())
        #     print(yaxis)
        # else:
        #     checkInput=True
        if 0 < float(box_mass.get()) <= 1000:
            mass = float(box_mass.get())
            print(mass)
        else:
            checkInput=True
        if 0<=float(box_springconst.get())<=2500:
            springconst = float(box_springconst.get())
            print(springconst)
        else:
            checkInput=True
        if 0<=int(box_springAmount.get())<=20: 
            springAmount = int(box_springAmount.get())
            print(springAmount)
        else:
            checkInput=True
        # if checkInput or yaxis/xaxis > math.cos(60 * (math.pi/180)):
        #     open_popup()
        if checkInput:
            open_popup()

        distanceX = simulationCal(xaxis,springconst,springAmount,9.81,mass)
        initialVelo = float(distanceX.projectileCal())
        graphSim.showGraph(initialVelo, 0.2)
        
    except ValueError:
        open_popup()
        print("run except")

# Use CTkButton instead of tkinter Button
output = PhotoImage(file="output.png") # set image path
op = canvas.create_image(1100,405,image=output)
# canvas.tag_bind(button, "<Button-1>", button_function)

# create input
input = PhotoImage(file="input.png") # set image path
ip = canvas.create_image(1100,50,image=input)

freepik = PhotoImage(file="freepoklogo.png").subsample(4,4) # set image path
fp = canvas.create_image(640,682,image=freepik)

# create Calculate
# Use CTkButton instead of tkinter Button
calculate = PhotoImage(file="Calculate Button.png").subsample(3,3) # set image path
ccl = canvas.create_image(1080,370,image=calculate)
canvas.tag_bind(ccl, "<Button-1>", calClick)

# create Clear
clear = PhotoImage(file="ClearButton.png") # set image path
cl = canvas.create_image(1130,370,image=clear)
canvas.tag_bind(cl, "<Button-1>", button_clear)

# showGraph = graphSim.showGraph(initialVelo, xaxis, yaxis)
Graph = PhotoImage(file="graphbutton.png").subsample(2,2) # set image path
g = canvas.create_image(1100,530,image=Graph)
canvas.tag_bind(g, "<Button-1>", showGraph)

member = PhotoImage(file="memberbutton.png") # set image path
m = canvas.create_image(180,100,image=member)
canvas.tag_bind(m, "<Button-1>", nextPage)

box_xaxis = Entry(win1)
box_xaxis.place(x = 1092,y = 92,width=45,height=20)

# box_yaxis = Entry(win1)
# box_yaxis.place(x = 1092,y = 120,width=45,height=20)

box_mass = Entry(win1)
box_mass.place(x = 1092,y = 168,width=45,height=20)

box_springconst = Entry(win1)
box_springconst.place(x = 1092,y = 292,width=45,height=20)

box_springAmount = Entry(win1)
box_springAmount.place(x = 1092,y = 327,width=45,height=20)

box_iniVeloLabel = Entry(win1)
box_iniVeloLabel.place(x = 1111,y = 417,width=45,height=20)

box_iniVeloLabel.config(state='disabled')

box_timeLabel = Entry(win1)
box_timeLabel.place(x = 1111,y = 441,width=45,height=20)

box_timeLabel.config(state='disabled')

box_springLenLabel = Entry(win1)
box_springLenLabel.place(x = 1111,y = 464,width=45,height=20)

box_springLenLabel.config(state='disabled')

# def open_popup():
#    top= Toplevel(win1)
#    top.geometry("750x250")
#    top.title("Child Window")
#    Label(top, text= "Out Of Range").place(x=150,y=80)
# canvas.tag_bind(ccl, "<Button-1>", open_popup)

# if (ccl, "<Button-1>"):
#     if int(box_angle.get()) is int:
#         if box_angle.get() in range(0,90):
#             angle=box_angle.get()
#         else:
#             open_popup

win1.mainloop()