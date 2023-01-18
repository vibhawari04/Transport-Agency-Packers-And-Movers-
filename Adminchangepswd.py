from tkinter import *
from tkinter import messagebox
import mysql.connector
def adminchngepswdwin():

        def changed():
            dbcon=mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="starmoversdb"
            )
            if dbcon:
                cur=dbcon.cursor()
                inpid=enid.get()
                inpusertype=enusertype.get()
                inppaswrd=enpassw.get()
                tpdata = (inppaswrd, inpid, inpusertype)
                qry="UPDATE users set password=%s WHERE id=%s and usertype=%s"

                cur.execute(qry,tpdata)
                dbcon.commit()
                if cur.rowcount==1:
                    messagebox.showinfo("Sucess","Password changed")



        acp=Tk()
        acp.geometry("400x400")
        acp.title("Admin change password")
        acp.resizable(0,0)
        acp.config(bg= "#FAEBD7")

        heading = Label(acp,text = "Admin Change Password",font=("Comic Sans MS", 15),bg="#FAEBD7")
        label1=Label(acp,text="Id",font=("Comic Sans MS", 10),bg="#FAEBD7")
        label2=Label(acp,text="Usertype",font=("Comic Sans MS", 10),bg="#FAEBD7")
        label3=Label(acp,text=" New Password",font=("Comic Sans MS", 10),bg="#FAEBD7")
        enid=Entry(acp,font=("Comic Sans MS", 10))
        enusertype=Entry(acp,font=("Comic Sans MS", 10))
        enpassw=Entry(acp,font=("Comic Sans MS", 10))
        btn=Button(acp,text="Change password",command=changed,font=("Comic Sans MS", 12),bg="#EEDFCC")


        heading.place(x =100 ,y = 30)
        label1.place(x = 30 , y = 90)
        enid.place(x = 150 , y = 90)
        label2.place(x=30 , y = 120)
        enusertype.place(x=150 , y = 120)
        label3.place(x = 30 , y = 150)
        enpassw.place(x = 150 , y = 150)
        btn.place(x = 130 , y = 230)


        acp.mainloop()
