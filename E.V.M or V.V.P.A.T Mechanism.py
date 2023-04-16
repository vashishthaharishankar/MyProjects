# Import Tkinter Module
import tkinter as tk
from tkinter import *
import os
import webbrowser

def rating():
    # Default browser path
    # Change it according to your own
    path2 = '"C://Program Files/Mozilla Firefox/firefox.exe" %s'
    webbrowser.get(path2).open('vashishthahari.weebly.com/feedback')
    #webbrowser.open('vashishthahari.weebly.com/feedback')
def exit1():
    exit()
def globals():
    global i1
    global i2
    global i3
    global i4
    global i5
    global b1
    global r
    global a
    global b2
    global t
    i1, i2, i3, i4, i5 = 0, 0, 0, 0, 0
    b1, r, a, b2, t = 0, 0, 0, 0, 0
def reset1():
    win3.window3.destroy()
    globals()
    win2()

def win2():

    win2.window2 = tk.Tk()
    # Title of the window
    win2.window2.title('Start Voting')
    # Dimwnsion of Window
    win2.window2.geometry('400x265')
    # Stop resizing the window
    win2.window2.resizable(False, False)

    frame1 = tk.Frame(win2.window2, width=400, height=600, bg="#7FFFD4")
    frame1.pack()

    label1 = tk.Label(win2.window2, text="V.V.P.A.T",width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
    label1.config(font=('Arial bold', 25))
    label1.place(x=55, y=5)
    frame2 = tk.Frame(win2.window2, width=400, height=50, bg="#7FFFD4")
    frame2.place(x=0, y=80)
    btn1 = tk.Button(frame2, text="Previous", width=10, relief=RAISED, borderwidth=5, bg="lime green")
    btn1.config(font=('Arial bold', 10))
    btn1.grid(row=0, column=0, padx=17)
    btn2 = tk.Button(frame2, text="Rate Us", width=10, relief=RAISED, borderwidth=5, bg="yellow",command=rating)
    btn2.config(font=('Arial bold', 10))
    btn2.grid(row=0, column=2, padx=20)
    btn3 = tk.Button(frame2, text="Exit(X)", width=10, relief=RAISED, borderwidth=5, bg="red",command=exit1)
    btn3.config(font=('Arial bold', 10))
    btn3.grid(row=0, column=3, padx=20)

    frame3 = tk.Frame(win2.window2, width=400, height=400,relief=FLAT,borderwidth=9, bg="#7FFFD4")
    frame3.place(x=0, y=133)
    btn4 = tk.Button(frame3, text="START\nVOTING", width=18, relief=RAISED, borderwidth=5, bg="#1E90FF",command=win3)
    btn4.config(font=('Arial bold', 20))
    btn4.grid(row=0, column=0, padx=30)

    win2.window2.mainloop()

i1,i2,i3,i4,i5=0,0,0,0,0
b1,r,a,b2,t=0,0,0,0,0
global next
next = True

def next1():
    global next
    next=True

def bjp():
    bjp.voted=True
    rld.voted=False
    aap.voted=False
    bsp.voted=False
    trs.voted=False
    global next
    if next==True:
        global i1
        global b1
        b1 = i1 + 1
        i1 = b1
        next = False

def rld():
    bjp.voted=False
    rld.voted=True
    aap.voted=False
    bsp.voted=False
    trs.voted=False
    global next
    if next==True:
        global i2
        global r
        r = i2 + 1
        i2 = r
        next = False

def aap():
    bjp.voted = False
    rld.voted = False
    aap.voted = True
    bsp.voted = False
    trs.voted = False
    global next
    if next == True:
        global i3
        global a
        a = i3 + 1
        i3 = a
        next = False

def bsp():
    bjp.voted = False
    rld.voted = False
    aap.voted = False
    bsp.voted = True
    trs.voted = False
    global next
    if next == True:
        global i4
        global b2
        b2 = i4 + 1
        i4 = b2
        next = False

def trs():
    bjp.voted = False
    rld.voted = False
    aap.voted = False
    bsp.voted = False
    trs.voted = True
    global next
    if next == True:
        global i5
        global t
        t = i5 + 1
        i5 = t
        next = False

def result():
    win4()

def verifybjp():
    if bjp.voted==True:
        global vote
        vote="You Voted for B.J.P\nThanks! to Vote."
def verifyrld():
    if rld.voted == True:
        global vote
        vote="You Voted for R.L.D\nThanks! to Vote."
def verifyaap():
    if aap.voted == True:
        global vote
        vote="You Voted for A.A.P\nThanks! to Vote."
def verifybsp():
    if bsp.voted == True:
        global vote
        vote="You Voted for B.S.P\nThanks! to Vote."
def verifytrs():
    if trs.voted == True:
        global vote
        vote="You Voted for T.R.S\nThanks! to Vote."

def history():
    f = open('R:/vvpat.txt', 'w')
    f.write("")
    f.close()

    f = open('R:/vvpat.txt', 'a+')
    verifybjp()
    verifyrld()
    verifyaap()
    verifybsp()
    verifytrs()

    global vote
    f.write(vote)
    f.close()
    os.system("R:/vvpat.txt")

def win3():

    win2.window2.destroy()

    win3.window3 = tk.Tk()
    # Title of the window
    win3.window3.title('Voting Window')
    # Dimwnsion of Window
    win3.window3.geometry('400x600')
    # Stop resizing the window
    win3.window3.resizable(False, False)

    frame1 = tk.Frame(win3.window3, width=400, height=600, bg="#7FFFD4")
    frame1.pack()

    label1 = tk.Label(win3.window3, text="V.V.P.A.T",width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
    label1.config(font=('Arial bold', 25))
    label1.place(x=55, y=5)
    frame2 = tk.Frame(win3.window3, width=400, height=50, bg="#7FFFD4")
    frame2.place(x=0, y=60)
    btn1 = tk.Button(frame2, text="Previous", width=10, relief=RAISED, borderwidth=5, bg="lime green",command=reset1)
    btn1.config(font=('Arial bold', 10))
    btn1.grid(row=0, column=0, padx=17)
    btn2 = tk.Button(frame2, text="Rate Us", width=10, relief=RAISED, borderwidth=5, bg="yellow",command=rating)
    btn2.config(font=('Arial bold', 10))
    btn2.grid(row=0, column=2, padx=20)
    btn3 = tk.Button(frame2, text="Exit(X)", width=10, relief=RAISED, borderwidth=5, bg="red",command=exit1)
    btn3.config(font=('Arial bold', 10))
    btn3.grid(row=0, column=3, padx=20)

    frame5 = tk.Frame(win3.window3, width=400, height=400, relief=FLAT, borderwidth=9, bg="#7FFFD4")
    frame5.place(x=32, y=100)

    btn7 = tk.Button(frame5, text="B.J.P", width=20, relief=RAISED, borderwidth=5, bg="#FF4500", command=bjp)
    btn7.config(font=('Arial bold', 17))
    btn7.grid(row=0, column=0, padx=12, pady=2)
    btn8 = tk.Button(frame5, text="R.L.D", width=20, relief=RAISED, borderwidth=5, bg="#00FF00", command=rld)
    btn8.config(font=('Arial bold', 17))
    btn8.grid(row=1, column=0, padx=12, pady=2)
    btn9 = tk.Button(frame5, text="A.A.P", width=20, relief=RAISED, borderwidth=5, bg="white", command=aap)
    btn9.config(font=('Arial bold', 17))
    btn9.grid(row=2, column=0, padx=12, pady=2)
    btn10 = tk.Button(frame5, text="B.S.P", width=20, relief=RAISED, borderwidth=5, bg="blue", command=bsp)
    btn10.config(font=('Arial bold', 17))
    btn10.grid(row=3, column=0, padx=12, pady=2)
    btn11 = tk.Button(frame5, text="T.R.S", width=20, relief=RAISED, borderwidth=5, bg="#FF1493", command=trs)
    btn11.config(font=('Arial bold', 17))
    btn11.grid(row=4, column=0, padx=12, pady=2)

    frame4 = tk.Frame(win3.window3, width=400, height=400,relief=FLAT,borderwidth=9, bg="#7FFFD4")
    frame4.place(x=32, y=400)
    btn4 = tk.Button(frame4, text="NEXT(>>)", width=8, relief=RAISED, borderwidth=5, bg="red",command=next1)
    btn4.config(font=('Arial bold', 15))
    btn4.grid(row=0, column=0, padx=100,pady=5)
    btn5 = tk.Button(frame4, text="RESULT", width=8, relief=RAISED, borderwidth=5, bg="yellow",command=result)
    btn5.config(font=('Arial bold', 15))
    btn5.grid(row=1, column=0, padx=100,pady=5)
    btn6 = tk.Button(frame4, text="V.V.P.A.T", width=8, relief=RAISED, borderwidth=5, bg="lime green",command=history)
    btn6.config(font=('Arial bold', 15))
    btn6.grid(row=2, column=0, padx=100,pady=5)

    win3.window3.mainloop()

def counting():
    f = open('R:/vvpat.txt', 'w')
    f.write("")
    f.close()

    f = open('R:/vvpat.txt', 'a+')
    bjp1 = "Total Votes for B.J.P are:- "+str(b1)+"\n"
    rld1 = "Total Votes for R.L.D are:- " + str(r) + "\n"
    aap1 = "Total Votes for A.A.P are:- " + str(a) + "\n"
    bsp1 = "Total Votes for B.S.P are:- " + str(b2) + "\n"
    trs1 = "Total Votes for T.R.S are:- " + str(t) + "\n\n"

    f.write(bjp1)
    f.write(rld1)
    f.write(aap1)
    f.write(bsp1)
    f.write(trs1)
    f.close()

    os.system("R:/vvpat.txt")

global b1winner
global rwinner
global awinner
global b2winner
global twinner
b1winner = False
rwinner = False
awinner = False
b2winner = False
twinner = False
global temptie
temptie=0
def win4():
    win3.window3.destroy()
    #win2()
    #win2.window2.destroy()
    win4.window4 = tk.Tk()
    # Title of the window
    win4.window4.title('Window3')
    # Dimwnsion of Window
    win4.window4.geometry('400x600')
    # Stop resizing the window
    win4.window4.resizable(False, False)

    frame1 = tk.Frame(win4.window4, width=400, height=600, bg="#7FFFD4")
    frame1.pack()

    label1 = tk.Label(win4.window4, text="V.V.P.A.T",width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
    label1.config(font=('Arial bold', 25))
    label1.place(x=55, y=5)

    a1="B.J.P\n"+str(b1)
    a2="R.L.D\n"+str(r)
    a3="A.A.P\n"+str(a)
    a4="B.S.P\n"+str(b2)
    a5="T.R.S\n"+str(t)
    list1=[b1,r,a,b2,t]
    win4.high=max(list1)
    global temptie
    global tie
    if b1 == win4.high:
        global b1winner
        tie=temptie+1
        temptie=tie
        b1winner = True

    if r == win4.high:
        global rwinner
        tie=temptie+1
        temptie=tie
        rwinner = True
    if a == win4.high:
        global awinner
        tie=temptie+1
        temptie=tie
        awinner = True
    if b2 == win4.high:
        global b2winner
        tie=temptie+1
        temptie=tie
        b2winner = True
    if t == win4.high:
        global twinner
        tie=temptie+1
        temptie=tie
        twinner = True

    frame5 = tk.Frame(win4.window4, width=400, height=400, relief=FLAT, borderwidth=9, bg="#7FFFD4")
    frame5.place(x=28, y=70)

    label7 = tk.Label(frame5, text=a1, width=24, relief=RIDGE, borderwidth=5, bg="#FF4500")
    label7.config(font=('Arial bold', 15))
    label7.grid(row=0, column=0, padx=12, pady=6)
    label8 = tk.Label(frame5, text=a2, width=24, relief=RIDGE, borderwidth=5, bg="#00FF00")
    label8.config(font=('Arial bold', 15))
    label8.grid(row=1, column=0, padx=12, pady=6)
    label9 = tk.Label(frame5, text=a3, width=24, relief=RIDGE, borderwidth=5, bg="white")
    label9.config(font=('Arial bold', 15))
    label9.grid(row=2, column=0, padx=12, pady=6)
    label10 = tk.Label(frame5, text=a4, width=24, relief=RIDGE, borderwidth=5, bg="blue")
    label10.config(font=('Arial bold', 15))
    label10.grid(row=3, column=0, padx=12, pady=6)
    label11 = tk.Label(frame5, text=a5, width=24, relief=RIDGE, borderwidth=5, bg="#FF1493")
    label11.config(font=('Arial bold', 15))
    label11.grid(row=4, column=0, padx=12, pady=6)

    frame4 = tk.Frame(win4.window4, width=400, height=400,relief=FLAT,borderwidth=9, bg="#7FFFD4")
    frame4.place(x=32, y=450)
    btn4 = tk.Button(frame4, text="COUNTING", width=9, relief=RAISED, borderwidth=5, bg="#ADFF2F",command=counting)
    btn4.config(font=('Arial bold', 15))
    btn4.grid(row=0, column=0, padx=100,pady=5)
    btn4 = tk.Button(frame4, text="WINNER", width=9, relief=RAISED, borderwidth=5, bg="#FF1493",command=win5)
    btn4.config(font=('Arial bold', 15))
    btn4.grid(row=1, column=0, padx=100,pady=5)

    win4.window4.mainloop()

def win5():
    win4.window4.destroy()
    window5 = tk.Tk()
    window5.title('Final Result')
    window5.geometry('400x600')
    window5.resizable(False, False)
    global b1winner
    global rwinner
    global awinner
    global b2winner
    global twinner

    frame1 = tk.Frame(window5, width=400, height=600, bg="#7FFFD4")
    frame1.pack()
    global tie
    if tie > 1:
        strtie="TIE B/W "+str(tie)
        label1 = tk.Label(window5, text=strtie, width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
        label1.config(font=('Arial bold', 25))
        label1.place(x=55, y=5)
    else :
        label1 = tk.Label(window5, text="WINNER", width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
        label1.config(font=('Arial bold', 25))
        label1.place(x=55, y=5)

    a1="B.J.P\n"+str(b1)
    a2="R.L.D\n"+str(r)
    a3="A.A.P\n"+str(a)
    a4="B.S.P\n"+str(b2)
    a5="T.R.S\n"+str(t)


    frame5 = tk.Frame(window5, width=400, height=400, relief=FLAT, borderwidth=9, bg="#7FFFD4")
    frame5.place(x=28, y=70)

    if b1winner == True:
        label7 = tk.Label(frame5, text=a1, width=24, relief=RIDGE, borderwidth=5, bg="#FF4500")
        label7.config(font=('Arial bold', 15))
        label7.grid(row=0, column=0, padx=12, pady=6)
    if rwinner == True:
        label8 = tk.Label(frame5, text=a2, width=24, relief=RIDGE, borderwidth=5, bg="#00FF00")
        label8.config(font=('Arial bold', 15))
        label8.grid(row=1, column=0, padx=12, pady=6)
    if awinner == True:
        label9 = tk.Label(frame5, text=a3, width=24, relief=RIDGE, borderwidth=5, bg="white")
        label9.config(font=('Arial bold', 15))
        label9.grid(row=2, column=0, padx=12, pady=6)
    if b2winner == True:
        label10 = tk.Label(frame5, text=a4, width=24, relief=RIDGE, borderwidth=5, bg="blue")
        label10.config(font=('Arial bold', 15))
        label10.grid(row=3, column=0, padx=12, pady=6)
    if twinner == True:
        label11 = tk.Label(frame5, text=a5, width=24, relief=RIDGE, borderwidth=5, bg="#FF1493")
        label11.config(font=('Arial bold', 15))
        label11.grid(row=4, column=0, padx=12, pady=6)

    btn4 = tk.Button(window5, text="COUNTING", width=9, relief=RAISED, borderwidth=5, bg="#ADFF2F",command=counting)
    btn4.config(font=('Arial bold', 15))
    btn4.place(x=132,y=450)
    btn4 = tk.Button(window5, text="EXIT(X)", width=9, relief=RAISED, borderwidth=5, bg="red",command=exit1)
    btn4.config(font=('Arial bold', 15))
    btn4.place(x=132,y=510)

    window5.mainloop()


win2()


