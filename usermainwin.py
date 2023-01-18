from tkinter import*
from tkinter import messagebox
import mysql.connector
from Bookingwin import *
from updatewinUser import *
from deletewin import *
from open import *
from searchFare import *
from showFare import *
from calculatefare import *
from PIL import ImageTk, Image



def userstartwin():
    smw1 = Tk()
    smw1.geometry("600x700")
    smw1.resizable(0, 0)
    smw1.title("User Window")
    smw1.config(bg="#FFEFDB")

    text = Label(smw1,text= "STAR MOVERS ",font=("Comic Sans MS", 24),bg = "#FAEBD7")
    text.place(x=500, y=100)





    def Booking():
        Bookingwin()

    def updateD():
        updatewin()

    def cancel():
        delete()

    def showW():
        openw()

    def searchfare():
        searchF()

    def show():
        showFare()

    def fareCal():
        calci()


    menubar = Menu(smw1)
    # file menu code
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Booking" ,command = Booking)
    filemenu.add_command(label="open",command = showW)
    filemenu.add_command(label="update",command = updateD)
    filemenu.add_command(label="cancel",command = cancel)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=smw1.quit)

    menubar.add_cascade(label="Bookings", menu=filemenu)


    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_separator()

    editmenu.add_command(label="Search",command = searchfare)
    editmenu.add_command(label="show fare",command = show)
    editmenu.add_command(label="calculate",command = fareCal)

    menubar.add_cascade(label="Calculate Fare", menu=editmenu)
    smw1.config(menu=menubar)

    # run menu code

    sbackground = PhotoImage(file="images/PACKERS AND MOVERS2.png",master=smw1)
    Label(smw1, image=sbackground).place(x=-2, y=-5)




    smw1.mainloop()
