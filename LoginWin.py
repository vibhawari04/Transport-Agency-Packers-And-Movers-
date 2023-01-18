from tkinter import*
from tkinter import messagebox
import mysql.connector
from adminmainwin import adminstartwin
from usermainwin import userstartwin

def adminLogin():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="starmoversdb"

    )
    if con:

        inname=enname.get()
        inpass=enpass.get()
        # Database Fetching.
        qry="SELECT *FROM users where name=%s and password=%s and usertype='admin'"
        tpdata=(inname,inpass)
        cur=con.cursor()
        cur.execute(qry,tpdata)
        data=cur.fetchone()
        if data!=None:
            mw.wm_withdraw()
            adminstartwin()

        else:
            messagebox.showinfo("info","login failed")

    else:
        messagebox.showinfo("failed","connection failed")
def userLogin():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="starmoversdb"

    )
    if con:

        #input
        inname=enname.get()
        inpass=enpass.get()
        #database(fetch)
        qry="SELECT *FROM users where name=%s and password=%s and usertype='user'"
        tpdata=(inname,inpass)
        cur=con.cursor()
        cur.execute(qry,tpdata)
        data=cur.fetchone()
        if data!=None:
            mw.wm_withdraw()
            userstartwin()

        else:
            messagebox.showinfo("info","login failed")

    else:
        messagebox.showinfo("failed","connection failed")
mw=Tk()
mw.geometry("400x200+500+250")
mw.minsize(400,200)
mw.maxsize(400,200)
mw.config(bg = "#FAEBD7")
heading = Label(mw,text= "LOGIN",bg="#FAEBD7",font=("Comic Sans MS", 20,"bold"))
lbname=Label(mw,text="Name",bg = "#FAEBD7",font=("Comic Sans MS",10))
lbpass=Label(mw,text="Password",bg = "#FAEBD7",font=("Comic Sans MS", 10))
enname=Entry(mw,font=("Comic Sans MS", 10))
enpass=Entry(mw,show="*",font=("Comic Sans MS", 10))

adminLoginBtn=Button(text="ADMIN",command=adminLogin,fg='black', bg='#EED5B7',border = 2,font=("Comic Sans MS", 10) )
userLoginBtn=Button(text="USER",command=userLogin,fg='black', bg='#EED5B7',border = 2,font=("Comic Sans MS", 10))

heading.place(x = 150, y =10)
lbname.place(x=85,y=70)

enname.place(x = 180 ,y=70)
lbpass.place(x=85,y=105)

enpass.place(x = 180,y =105)
adminLoginBtn.place(x=70,y=150)
userLoginBtn.place(x = 250,y=150)

mw.mainloop()