from tkinter import *
from tkinter import messagebox
import mysql.connector
def addfaredetailwin():
    def Addfaredetail():
        dbcon = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"
        )
        if dbcon:
            # messagebox.showinfo("Done")
            cur = dbcon.cursor(prepared=True)

            transporttype=e1.get()
            chargeperkg = e2.get()
            chargeperkm = e3.get()
            chargeperwidth = e4.get()
            chargeperheight = e5.get()

            tpdata = (transporttype,chargeperkg,chargeperkm,chargeperwidth,chargeperheight)

            qry = "INSERT INTO faredetail(transporttype,chargeperkg,chargeperkm,chargeperwidth,chargeperheight) VALUES(%s,%s,%s,%s,%s)"
            cur.execute(qry, tpdata)
            dbcon.commit()
            if cur.rowcount == 1:
                messagebox.showinfo("Note", "Faredetail Added")

    afd = Tk()
    afd.title("Add Fare Detail")
    afd.geometry("400x400")
    afd.resizable(0,0)
    afd.config(bg = "#FAEBD7")

    heading = Label(afd,text= "Add Fare Detail",font=("Comic Sans MS", 15),bg="#FAEBD7")
    label1 = Label(afd, text="Goods Type",bg="#FAEBD7",font=("Comic Sans MS", 10))
    e1 = Entry(afd,font=("Comic Sans MS", 10))
    label2 = Label(afd, text="Rate Per KG",bg="#FAEBD7",font=("Comic Sans MS", 10))
    e2 = Entry(afd,font=("Comic Sans MS", 10))
    label3 = Label(afd, text="Rate Per KM",bg="#FAEBD7",font=("Comic Sans MS", 10))
    e3 = Entry(afd,font=("Comic Sans MS", 10))
    label4 = Label(afd, text="Rate Per Width",bg="#FAEBD7",font=("Comic Sans MS", 10))
    e4 = Entry(afd,font=("Comic Sans MS", 10))
    label5 = Label(afd, text="Rate Per Height",bg="#FAEBD7",font=("Comic Sans MS", 10))
    e5 = Entry(afd,font=("Comic Sans MS", 10))

    button = Button(afd, text="Add Fare", command=Addfaredetail,font=("Comic Sans MS", 12),bg="#EEDFCC")

    heading.place(x=130 , y = 10)

    label1.place(x=50,y = 50)
    e1.place(x=150, y=50)

    label2.place(x=50,y=100)
    e2.place(x=150, y=100)
    label3.place(x=50,y=150)
    e3.place(x=150,y=150)
    label4.place(x=50,y=200)
    e4.place(x=150,y=200)
    label5.place(x=50,y=250)
    e5.place(x=150,y=250)
    button.place(x=150,y = 300)

    afd.mainloop()
