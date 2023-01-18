from tkinter import*

from tkinter import messagebox
import mysql.connector
from Adminchangepswd import*
from createnewuser import*
from userchanngepswd import*
from deleteuser import*
from AddFaredetail import*
from SearchFaredetail import *
from UpdateFaredetail import*
from DeleteFaredetail import *
from Aboutus import *
from Aboutproject import*

def adminstartwin():

    smw=Tk()
    smw.geometry("600x700+500+20")
    smw.resizable(False,False)
    smw.title("Main Window")
    smw.configure(bg="sky blue")
    menubar = Menu(smw)

    # file menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Admin Change Password",command=adminchngepswdwin)
    filemenu.add_command(label="Create New User",command=createnewuserwin)
    filemenu.add_command(label="User Change Password",command=userchngepswdwin)
    filemenu.add_command(label="Delete",command=deleteuserwin)
    filemenu.add_separator()
    filemenu.add_command(label="Exit")

    menubar.add_cascade(label="Admin", menu=filemenu)
    # edit menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Add FareDetail",command=addfaredetailwin)
    editmenu.add_command(label="Search FareDetail",command=searchfaredetailwin)
    editmenu.add_separator()
    editmenu.add_command(label="Update FareDetail",command=updatefaredetailwin)
    editmenu.add_command(label="Delete FareDetail",command=deletefaredetailwin)

    menubar.add_cascade(label="Fare menu", menu=editmenu)
    # runmenu
    runmenu = Menu(menubar, tearoff=0)
    runmenu.add_command(label="About us",command=aboutuswin)
    runmenu.add_command(label="About Project",command=aboutprojectwin)
    menubar.add_cascade(label="Help", menu=runmenu)


    smw.config(menu=menubar)

    #Addding image to the admin window




    # Position image

    sbackground = PhotoImage(file="images/PACKERS AND MOVERS2.png", master=smw)
    Label(smw, image=sbackground).place(x=-2, y=-5)





     #conBtn=Button(smw,text="Next")
    #conBtn.pack()
    smw.mainloop()

