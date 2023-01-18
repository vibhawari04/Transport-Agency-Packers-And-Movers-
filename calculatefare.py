from tkinter import *
from tkinter import messagebox
import mysql.connector
from usermainwin import *
""" formula amt =  e1*chargeperkg + e2*chargeperkm + e3 * chargeperwidth + e4 * chargeperhight """
def calci():

    def calculation():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"
        )

        conn = con.cursor()
        q = "SELECT * FROM faredetail  WHERE transporttype = %s "
        transporttype = transportTypeE.get()
        kg = int(E1.get())
        km = int(E2.get())
        width = int(E3.get())
        height =int(E4.get())

        tpdata = (transporttype,)
        conn.execute(q,tpdata)
        data = conn.fetchone()

        if conn.rowcount == 1:

            total_amt =( (data[2] * kg) + (data[3]* km) + (data[4] * width) + (data[5] * height) )
            print(total_amt)
            totalE.insert(0,str(total_amt))#,font=("Comic Sans MS", 10)
        else:
            messagebox.showinfo("failed","No Such Record")





    calwin = Tk()
    calwin.geometry("400x400")
    calwin.title("calculator window")
    calwin.resizable(0,0)
    calwin.config(bg = "#FFE4E1")

    heading = Label(calwin,text = "CALCULATION",font=("Comic Sans MS", 12,"bold"),bg = "#FFE4E1")
    transportType = Label(calwin, text = "Goods Type",font=("Comic Sans MS", 10),bg = "#FFE4E1")
    transportTypeE = Entry(calwin,font=("Comic Sans MS", 10))
    l1 = Label(calwin,text="Weight (KG)",font=("Comic Sans MS", 10),bg = "#FFE4E1")
    E1 = Entry(calwin,font=("Comic Sans MS", 10))

    l2 = Label(calwin,text="Distance(KM)",font=("Comic Sans MS", 10),bg = "#FFE4E1")
    E2 = Entry(calwin,font=("Comic Sans MS", 10))

    l3 = Label(calwin,text="Height (Feet)",font=("Comic Sans MS", 10),bg = "#FFE4E1")
    E3 = Entry(calwin,font=("Comic Sans MS", 10))

    l4 = Label(calwin,text="Width (Feet)",font=("Comic Sans MS", 10),bg = "#FFE4E1")
    E4 = Entry(calwin,font=("Comic Sans MS", 10))

    btn = Button(calwin , text = " CALCULATE",command = calculation,font=("Comic Sans MS", 10),bg = "#CDB38B")
    totalL = Label(calwin, text ="Total Amount",font=("Comic Sans MS", 10),bg = "#FFE4E1")
    totalE = Entry(calwin,font=("Comic Sans MS", 10))

    heading.place(x=150,y = 20)
    transportType.place(x = 30 , y =60)
    transportTypeE.place(x = 150 , y =60)
    l1.place(x = 30 , y = 90)
    E1.place(x =150 , y =90)
    l2.place(x=30 , y = 120)
    E2.place(x =150 , y = 120)
    l3.place(x =30 , y =150)
    E3.place(x = 150 ,y =150)
    l4.place(x = 30 , y =180)
    E4.place(x=150 , y = 180)
    btn.place(x = 140 , y =230)
    totalL.place(x =30,y=290)
    totalE.place(x=150,y = 290)


    calwin.mainloop()
