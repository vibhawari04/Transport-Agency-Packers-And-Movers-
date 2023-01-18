from tkinter import *
from tkinter import messagebox
from usermainwin import *
import mysql.connector
def delete():
    def cancel():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",  # type here your password
            db="starmoversdb"
        )
        if con != None:
            print("connection done")
            sql = "DELETE FROM bookingdetail WHERE customerid = %s";
            cur = con.cursor(prepared=True)
            customerid = E1.get()
            tpdata = (customerid ,)
            cur.execute(sql, tpdata)
            con.commit()
            if cur.rowcount == 1:
                print("Deleted Successfully")
                messagebox.showinfo("info", "Canceled Booking")
            else:
                print("No detail present ")
                messagebox.showinfo("info", "Booking Not Present ")

    dele = Tk()
    dele.title("delete window")
    dele.geometry("300x200")
    dele.config(bg="#FFDAB9")
    dele.resizable(0,0)
    heading = Label(dele , text ="Delete Booking Detail",font=("Comic Sans MS", 12),bg= "#FFDAB9")
    l1 = Label(dele,text ="Customer Id",font=("Comic Sans MS", 10),bg= "#FFDAB9")
    E1 = Entry(dele,font=("Comic Sans MS", 10))
    okBtn = Button(dele,text = "Delete",command = cancel,font = ("Comic Sans MS",12),bg ="#FFEFD5")

    heading.pack()
    l1.place(x=40 , y = 50)
    E1.place(x=130 , y=50)
    okBtn.place(x=120,y=100)

    dele.mainloop()

