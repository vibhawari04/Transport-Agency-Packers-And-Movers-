from tkinter import *
import time
from threading import *


def aboutprojectwin():


        ap = Tk()
        ap.title("About Project")
        ap.geometry("600x700+200+20")
        ap.resizable(False,False)
        ap.config(bg="brown")
        lb = Label(ap, text="Project Name", bg="red", fg="white", font=("Comic Sans MS", 25))
        lb1 = Label(ap, text="Transport Agency(Packers And Movers)", bg="orange", fg="white", font=("Comic Sans MS", 15))
        lb2 = Label(ap, text="It is a Desktop GUI Application", bg="red", fg="white", font=("Comic Sans MS", 15))
        lb3 = Label(ap, text="  It has Two Module :- ", bg="orange", fg="white", font=("Comic Sans MS", 15))
        lb4 = Label(ap, text="Admin Module And User Module. ", bg="red", fg="white", font=("Comic Sans MS", 15))
        lab5 = Label(ap, text="Both Modules have their own functionalities. ", bg="orange", fg="white", font=("Comic Sans MS", 15))
        lab6 = Label(ap, text="We use Tkinter library for GUI", bg="red", fg="white", font=("Comic Sans MS", 15))
        And = Label(ap,text = "And",bg = "orange",fg="white",font=("Comic Sans MS", 15))
        lab7 = Label(ap, text="MYSQL as a database.", bg="red", fg="white", font=("Comic Sans MS", 15))

        def threading():
            t1 = Thread(target=work)
            t1.start()

        def work():
            lb.place(x=200, y=10)
            time.sleep(.5)

            lb1.place(x=120, y=90)

            time.sleep(.5)

            lb2.place(x=120, y=150)
            time.sleep(.5)

            lb3.place(x=120, y=210)
            time.sleep(.5)

            lb4.place(x=120, y=270)
            time.sleep(.5)

            lab5.place(x=120, y=330)
            time.sleep(.5)

            lab6.place(x=120, y=390)
            time.sleep(.5)

            And.place(x=120,y=440)
            time.sleep(.5)

            lab7.place(x=120,y=500)
            time.sleep(.5)
        threading()

        ap.mainloop()

