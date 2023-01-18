from tkinter import *
from tkinter import messagebox
import mysql.connector
def createnewuserwin():

        def created():
            dbcon=mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="starmoversdb"
            )
            if dbcon:
                #messagebox.showinfo("Done")
                cur=dbcon.cursor(prepared=True)
                inpname=enname.get()
                inppass=enpass.get()
                inptype=entype.get()
                tpdata=(inpname,inppass,inptype)

                qry="INSERT INTO users(name,password,usertype) VALUES(%s,%s,%s)"
                cur.execute(qry,tpdata)
                dbcon.commit()
                if cur.rowcount==1:
                    messagebox.showinfo("create","new user created")

        unw=Tk()
        unw.geometry("400x400")
        unw.title("Create new user")
        unw.resizable(0,0)
        unw.config(bg ="#FAEBD7")

        heading = Label(unw,text= "CREATE USER",font=("Comic Sans MS", 15,"bold"),bg ="#FAEBD7")
        label1=Label(unw,text="User name",font=("Comic Sans MS", 10),bg ="#FAEBD7")
        label2=Label(unw,text="Password",font=("Comic Sans MS", 10),bg ="#FAEBD7")
        label3=Label(unw,text="User type",font=("Comic Sans MS", 10),bg ="#FAEBD7")
        enname=Entry(unw,font=("Comic Sans MS", 10))
        enpass=Entry(unw,show="*",font=("Comic Sans MS", 10))
        entype=Entry(unw,font=("Comic Sans MS", 10))
        button=Button(unw,text="Create",command=created,font=("Comic Sans MS", 12),bg="#EEDFCC")

        heading.place(x=130, y=30)
        label1.place(x=30, y=90)
        enname.place(x=150, y=90)
        label2.place(x=30, y=120)
        enpass.place(x=150, y=120)
        label3.place(x=30, y=150)
        entype.place(x=150, y=150)
        button.place(x=130, y=230)



        unw.mainloop()
