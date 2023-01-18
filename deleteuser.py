from tkinter import *
from tkinter import messagebox
import mysql.connector
def deleteuserwin():

    def delete():
        dbcon = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"
        )

        if dbcon:

            cur = dbcon.cursor()
            qry = "delete from users where id=%s"
            inpid=en1.get()
            tpval = (inpid,)
            cur.execute(qry, tpval)
            dbcon.commit()
            if cur.rowcount == 1:
                messagebox.showinfo("Done","Data deleted sucesfully")


            else:
                messagebox.showinfo("Note","Failed")

        else:
            print("connection failed")

    du=Tk()
    du.geometry("300x300")
    du.title("Delete User")
    du.resizable(0,0)
    du.config(bg="#FFE4C4")

    heading = Label(du,text="Delete User",font=("Comic Sans MS", 15),bg="#FFE4C4")
    label1=Label(du,text="Id",font=("Comic Sans MS", 10),bg="#FFE4C4")
    label2=Label(du,text="Name",font=("Comic Sans MS", 10),bg="#FFE4C4")
    en1=Entry(du,font=("Comic Sans MS", 10))
    en2=Entry(du,font=("Comic Sans MS", 10))
    btn=Button(du,text="Delete",command=delete,font=("Comic Sans MS", 12),bg="#EED5B7")

    heading.place(x=100,y=30)
    label1.place(x=30,y=90)
    en1.place(x=90,y=90)
    label2.place(x=30,y=130)
    en2.place(x=90,y=130)
    btn.place(x=120,y=180)


    du.mainloop()
