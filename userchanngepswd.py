from tkinter import *
from tkinter import messagebox
import  mysql.connector
def userchngepswdwin():


    def userpchnged():
        dbcon = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"
        )
        if dbcon:
            cur = dbcon.cursor()
            inpid = enid.get()
            inpusertype = enusertype.get()
            inppaswrd = enpassw.get()
            tpdata = (inppaswrd, inpid, inpusertype)
            qry = "UPDATE users set password=%s WHERE id=%s and usertype=%s"

            cur.execute(qry, tpdata)
            dbcon.commit()
            if cur.rowcount == 1:
                messagebox.showinfo("Sucess", "Password changed")


    ucp=Tk()
    ucp.geometry("400x400")
    ucp.title("User changed password")
    ucp.resizable(0,0)
    ucp.config(bg="#FFE4C4")
    heading = Label(ucp,text = "User Change Password",font=("Comic Sans MS", 15),bg="#FFE4C4")
    label1 = Label(ucp, text="Id",font=("Comic Sans MS", 10),bg="#FFE4C4")
    label2 = Label(ucp, text="User Type",font=("Comic Sans MS", 10),bg="#FFE4C4")
    label3 = Label(ucp, text=" New Password",font=("Comic Sans MS", 10),bg="#FFE4C4")
    enid = Entry(ucp,font=("Comic Sans MS", 10))
    enusertype = Entry(ucp,font=("Comic Sans MS", 10))
    enpassw = Entry(ucp,font=("Comic Sans MS", 10))
    btn = Button(ucp, text="Changed password", command=userpchnged,font=("Comic Sans MS", 12),bg="#EEDFCC")

    heading.place(x=100, y=30)
    label1.place(x=30, y=90)
    enid.place(x=150, y=90)
    label2.place(x=30, y=120)
    enusertype.place(x=150, y=120)
    label3.place(x=30, y=150)
    enpassw.place(x=150, y=150)
    btn.place(x=130, y=230)

    ucp.mainloop()
