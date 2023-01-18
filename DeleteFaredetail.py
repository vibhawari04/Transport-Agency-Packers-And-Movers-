from tkinter import *
from tkinter import messagebox
import mysql.connector


def deletefaredetailwin():


    def deletefare():
        dbcon = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"
        )

        if dbcon:

            cur = dbcon.cursor()
            qry = "delete from faredetail where id=%s and transporttype=%s"
            inpid=en1.get()
            inpname=en2.get()
            tpval = (inpid,inpname)
            cur.execute(qry, tpval)
            dbcon.commit()
            if cur.rowcount == 1:
                messagebox.showinfo("Done","Data deleted")


            else:
                messagebox.showinfo("Note","Failed")



    dfd = Tk()
    dfd.title("Delete Fare Detail")
    dfd.geometry("300x300")
    dfd.config(bg="#FFEFDB")
    dfd.resizable(0,0)
    heading =Label(dfd,text= "Delete Fare Detail ",font=("Comic Sans MS", 15,"bold"),bg = "#FFEFDB")
    label1=Label(dfd,text="Id",font=("Comic Sans MS", 10),bg = "#FFEFDB")
    en1=Entry(dfd,font=("Comic Sans MS", 10))
    label2=Label(dfd,text="Goods Type",font=("Comic Sans MS", 10),bg = "#FFEFDB")
    en2=Entry(dfd,font=("Comic Sans MS", 10))
    btn=Button(dfd,text="Delete",command=deletefare,font=("Comic Sans MS", 12),bg = "#EEDFCC")

    heading.place(x = 100 , y =10)
    label1.place(x=30,y=70)
    en1.place(x=120,y=70)
    label2.place(x=30,y=110)
    en2.place(x=120,y=110)
    btn.place(x=130,y=170)


    dfd.mainloop()
