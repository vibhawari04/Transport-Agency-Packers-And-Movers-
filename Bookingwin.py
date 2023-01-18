from usermainwin import *
from tkinter import*
from tkinter import messagebox
import mysql.connector

def Bookingwin():

    def create_fun():
    # insert query
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            db="starmoversdb"
            )
        if con != None:
            print("connection done")
            cur = con.cursor()
            sql = " INSERT INTO `bookingdetail` (`bookingdate`, `username`, `from`, `to`, `goodsdetail`, `ratebyperkm`, `ratebyperkg`, `customername`, `customermob`, `customeraddress`, `customerid`, `status`, `bookingchargewidth`, `bookingchargeheight`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";

            # bookingid= E1.get()
            bookingdate= E2.get()
            username= E3.get()
            From = E4.get()
            to = E5.get()
            goodsdetail = E6.get()
            ratebyperkm = E7.get()
            ratebyperkg = E8.get()
            customername = E9.get()
            customermob = E10.get()
            customeraddress = E11.get()
            customerid = E12.get()
            status = E13.get()
            bookingchargewidth = E14.get()
            bookingchargeheight =E15.get()

            if ( bookingdate and username and From and to and goodsdetail and ratebyperkm and ratebyperkg and customername and customermob and customeraddress and customerid and status and bookingchargewidth and bookingchargeheight)!=" ":
                tpdata = ( bookingdate,username,From,to,goodsdetail,ratebyperkm,ratebyperkg,customername,customermob,customeraddress,customerid,status,bookingchargewidth,bookingchargeheight)
                cur.execute(sql,tpdata)
                con.commit()
                if cur.rowcount == 1:
                     messagebox.showinfo("info", "BOOKED")

                else:
                    messagebox.showinfo("info", "Please Try Later")
                con.close()
            else:
                messagebox.showinfo("info", "please fill the information")

#*****************************************************************************************************************************#
    bw = Tk()
    bw.geometry("500x680")
    bw.title("Booking Window")
    bw.resizable(0,0)
    heading = Label(bw,text = "BOOKING  DETAILS",bg="#FAEBD7",font=("Comic Sans MS", 20,"bold"))# center
    bw.config(bg="#FAEBD7")



    l2 = Label(bw,text="BOOKING DATE ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E2 = Entry(bw,font=("Comic Sans MS", 10))

    l3 = Label(bw,text="USERNAME ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E3 = Entry(bw,font=("Comic Sans MS", 10))

    l4 = Label(bw,text="FROM ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E4 = Entry(bw,font=("Comic Sans MS", 10))

    l5 = Label(bw,text="TO ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E5 = Entry(bw,font=("Comic Sans MS", 10))

    l6 = Label(bw,text="GOODS DETAILS ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E6 = Entry(bw,font=("Comic Sans MS", 10))

    l7 = Label(bw,text="RATE BY PER KM ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E7 = Entry(bw,font=("Comic Sans MS", 10))

    l8 = Label(bw,text="RATE BY PER KG ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E8 = Entry(bw,font=("Comic Sans MS", 10))

    l9 = Label(bw,text="CUSTOMER NAME ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E9 = Entry(bw,font=("Comic Sans MS", 10))

    l10 = Label(bw,text="CONTACT NO. ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E10 = Entry(bw,font=("Comic Sans MS", 10))

    l11 = Label(bw,text="ADDRESS ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E11 = Entry(bw,font=("Comic Sans MS", 10))

    l12 = Label(bw,text="CUSTOMER ID ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E12 = Entry(bw,font=("Comic Sans MS", 10))

    l13 = Label(bw, text="STATUS ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E13 = Entry(bw,font=("Comic Sans MS", 10))

    l14= Label(bw,text="BOOKING CHARGE WIDTH ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E14 = Entry(bw,font=("Comic Sans MS", 10))

    l15 = Label(bw,text="BOOKING CHARGE HEIGHT ",bg="#FAEBD7",font=("Comic Sans MS", 10))
    E15 = Entry(bw,font=("Comic Sans MS", 10))

    submitBtn = Button(bw,text= "Submit",command = create_fun,bg="#EEDFCC",font=("Comic Sans MS", 10),border=2)

    heading.place(x= 100 , y = 50)

    l2.place(x=90, y=130)
    E2.place(x=270, y=130)

    l3.place(x=90, y=160)
    E3.place(x=270, y=160)

    l4.place(x=90, y=190)
    E4.place(x=270, y=190)

    l5.place(x=90, y=220)
    E5.place(x=270, y=220)

    l6.place(x=90, y=250)
    E6.place(x=270, y=250)

    l7.place(x=90, y=280)
    E7.place(x=270, y=280)

    l8.place(x=90, y=320)
    E8.place(x=270, y=320)

    l9.place(x=90, y=350)
    E9.place(x=270, y=350)

    l10.place(x=90, y=380)
    E10.place(x=270, y=380)

    l11.place(x=90, y=420)
    E11.place(x=270, y=420)

    l12.place(x=90, y=450)
    E12.place(x=270, y=450)

    l13.place(x=90, y=480)
    E13.place(x=270, y=480)

    l14.place(x=90, y=520)
    E14.place(x=270, y=520)

    l15.place(x=90, y=550)
    E15.place(x=270, y=550)

    submitBtn.place(x=200,y=600)


    bw.mainloop()
