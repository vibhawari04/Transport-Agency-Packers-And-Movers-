from tkinter import *
from tkinter import messagebox
import mysql.connector

def updatefaredetailwin():

    def updatefaredetail():
        dbcon = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"
        )
        if dbcon:
            # messagebox.showinfo("Done")
            cur = dbcon.cursor()
            inpid = enid.get()
            inptype = entype.get()
            inpchargekg = enpkg.get()
            inpchargekm = enpkm.get()
            inpwidth = enpwidth.get()
            inpheight = enpheight.get()

            tpdata = (inpchargekg, inpchargekm, inpwidth, inpheight, inpid,inptype)

            qry = "UPDATE faredetail SET chargeperkg=%s, chargeperkm=%s, chargeperwidth=%s, chargeperheight=%s WHERE id=%s and transporttype=%s "
            cur.execute(qry, tpdata)
            dbcon.commit()
            if cur.rowcount == 1:
                messagebox.showinfo("Note", "Faredetail updated")
            else:
                messagebox.showinfo("Note","Failed updated")

    ufd = Tk()
    ufd.title("Update Fare Detail")
    ufd.geometry("400x400")
    ufd.resizable(0,0)
    ufd.config(bg="#FAEBD7")
    heading = Label(ufd , text = "Update Fare Detail",font=("Comic Sans MS", 15,"bold"),bg="#FAEBD7")
    label1 = Label(ufd, text="ID",font=("Comic Sans MS", 10),bg="#FAEBD7")
    label2 = Label(ufd, text="Goods Type",font=("Comic Sans MS", 10),bg="#FAEBD7")
    label3 = Label(ufd, text="Rate Per KG",font=("Comic Sans MS", 10),bg="#FAEBD7")
    label4 = Label(ufd, text="Rate Per KM",font=("Comic Sans MS", 10),bg="#FAEBD7")
    label5 = Label(ufd, text="Charge Per Width",font=("Comic Sans MS", 10),bg="#FAEBD7")
    label6 = Label(ufd, text="Charge Per Height",font=("Comic Sans MS", 10),bg="#FAEBD7")



    enid = Entry(ufd,font=("Comic Sans MS", 10))
    entype = Entry(ufd,font=("Comic Sans MS", 10))
    enpkg = Entry(ufd,font=("Comic Sans MS", 10))
    enpkm = Entry(ufd,font=("Comic Sans MS", 10))
    enpwidth = Entry(ufd,font=("Comic Sans MS", 10))
    enpheight = Entry(ufd,font=("Comic Sans MS", 10))

    button = Button(ufd, text="Update", command=updatefaredetail,font=("Comic Sans MS", 12),bg="#EED5B7")

    heading.place(x=100 , y = 10)

    label1.place(x = 40 , y = 70)
    enid.place(x=170,y=70)

    label2.place(x=40,y=110)
    entype.place(x=170,y=110)

    label3.place(x=40,y = 150)
    enpkg.place(x =170 , y =150)

    label4.place(x=40 , y =190)
    enpkm.place(x=170,y=190)

    label5.place(x=40,y=230)
    enpwidth.place(x=170,y=230)

    label6.place(x=40,y=270)
    enpheight.place(x=170,y=270)

    button.place(x= 150 , y = 320)


    ufd.mainloop()
