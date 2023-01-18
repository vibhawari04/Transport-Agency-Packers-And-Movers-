from tkinter import*
from tkinter import messagebox
import mysql.connector
from usermainwin import *
global  i , j
def updatewin():


    def newWinForUpdate():

        def editC():


            con = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",  # type here your password
                db="starmoversdb"
            )

            if con != None:
                print("connection done")
                cur = con.cursor()


                sql = " UPDATE `bookingdetail` SET  bookingdate =%s ,`From` = %s, `to` = %s , goodsdetail=%s , ratebyperkm = %s , ratebyperkg = %s , customername = %s,customermob = %s , customeraddress = %s , customerid = %s , status = %s,bookingchargewidth = %s , bookingchargeheight=%s WHERE (bookingid = %s and username =%s )";

                #execute()#receive data always in the form of tuple
                bookingdate = E2.get()
                username = j
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
                bookingchargeheight = E15.get()
                bookingid = i


                data = (bookingdate,From,to,goodsdetail,ratebyperkm,ratebyperkg,customername,customermob,customeraddress, customerid,status,bookingchargewidth,bookingchargeheight,bookingid ,username)
                cur.execute(sql, data)
                con.commit()
                if cur.rowcount == 1:
                    print("Updated Successfully")
                    messagebox.showinfo("info", "Updated Successfully")
                else:
                    print("failed to update ")
                    messagebox.showinfo("info", "failed to update ")

        up = Tk()
        up.geometry("600x600")
        up.title("update")
        up.config(bg="#FAEBD7")
        up.resizable(0, 0)
        heading = Label(up,text = "UPDATE DETAILS",font=("Comic Sans MS",20,"bold"),bg="#FAEBD7")
        l2 = Label(up, text="BOOKING DATE ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E2 = Entry(up,font=("Comic Sans MS", 10))

        l4 = Label(up, text="FROM ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E4 = Entry(up,font=("Comic Sans MS", 10))

        l5 = Label(up, text="TO ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E5 = Entry(up,font=("Comic Sans MS", 10))

        l6 = Label(up, text="GOODS DETAILS ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E6 = Entry(up,font=("Comic Sans MS", 10))

        l7 = Label(up, text="RATE BY PER KM ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E7 = Entry(up,font=("Comic Sans MS", 10))

        l8 = Label(up, text="RATE BY PER KG ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E8 = Entry(up,font=("Comic Sans MS", 10))

        l9 = Label(up, text="CUSTOMER NAME ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E9 = Entry(up,font=("Comic Sans MS", 10))

        l10 = Label(up, text="CONTACT NO. ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E10 = Entry(up,font=("Comic Sans MS", 10))

        l11 = Label(up, text="ADDRESS ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E11 = Entry(up,font=("Comic Sans MS", 10))

        l12 = Label(up, text="CUSTOMER ID ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E12 = Entry(up,font=("Comic Sans MS", 10))

        l13 = Label(up, text="STATUS ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E13 = Entry(up,font=("Comic Sans MS", 10))

        l14 = Label(up, text="BOOKING CHARGE WIDTH ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E14 = Entry(up,font=("Comic Sans MS", 10))

        l15 = Label(up, text="BOOKING CHARGE HEIGHT ",font=("Comic Sans MS",10),bg="#FAEBD7")
        E15 = Entry(up,font=("Comic Sans MS", 10))

        submitBtn = Button(up, text="Update", command=editC,font=("Comic Sans MS",12),bg="#EED5B7")

        heading.place(x=200, y=50)

        l2.place(x=100, y=130)
        E2.place(x=300, y=130)

        l4.place(x=100, y=160)
        E4.place(x=300, y=160)

        l5.place(x=100, y=190)
        E5.place(x=300, y=190)

        l6.place(x=100, y=220)
        E6.place(x=300, y=220)

        l7.place(x=100, y=250)
        E7.place(x=300, y=250)

        l8.place(x=100, y=280)
        E8.place(x=300, y=280)

        l9.place(x=100, y=310)
        E9.place(x=300, y=310)

        l10.place(x=100, y=340)
        E10.place(x=300, y=340)

        l11.place(x=100, y=370)
        E11.place(x=300, y=370)

        l12.place(x=100, y=400)
        E12.place(x=300, y=400)

        l13.place(x=100, y=430)
        E13.place(x=300, y=430)

        l14.place(x=100, y=460)
        E14.place(x=300, y=460)

        l15.place(x=100, y=490)
        E15.place(x=300, y=490)

        submitBtn.place(x=250, y=540)

        up.mainloop()

    def check():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"

        )
        if con:
            messagebox.showinfo("Success", "Connection Done")
            # input
            bookingid  = BidE.get()
            username = userE.get()
            global i , j
            i = bookingid
            j = username


            # database(fetch)
            qry = "SELECT * FROM bookingdetail where bookingid=%s and username=%s"

            tpdata = (bookingid, username)

            cur = con.cursor()
            cur.execute(qry, tpdata)
            data = cur.fetchone()
            if data != None:
                edit.wm_withdraw()
                newWinForUpdate()

            else:
                messagebox.showinfo("info", "Incorrect Input")

        else:
            messagebox.showinfo("Success", "NO Done")



    edit = Tk()
    edit.geometry("400x300+20+20")
    edit.resizable(0,0)
    edit.title("EDIT DETAILS")
    edit.config(bg ="#FAEBD7")

    heading = Label(edit,text = "Update Booking Detail",font=("Comic Sans MS", 12),bg= "#FAEBD7")
    BidL = Label(edit, text="Booking Id ",font=("Comic Sans MS",12),bg ="#FAEBD7")
    userL = Label(edit, text="Username ",font=("Comic Sans MS",12),bg=	"#FAEBD7")

    BidE= Entry(edit,font=("Comic Sans MS", 10))
    userE = Entry(edit,font=("Comic Sans MS", 10))



    okB = Button(edit,text = "CLICK HERE", command = check,font=("Comic Sans MS", 12),bg="#EED5B7")
    heading.place(x=100,y=10)
    BidL.place(x=60, y=80)
    BidE.place(x=150, y=85)
    userL.place(x= 60 ,y = 120 )
    userE.place(x=150 , y = 125)

    okB . place(x =120 , y = 170)



    edit.mainloop()

