from tkinter import *
from tkinter import messagebox
from usermainwin import *
import mysql.connector
def showFare():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="starmoversdb"

    )
    my_conn = con.cursor()
    q = "SELECT * FROM faredetail "
    my_conn.execute(q)

    show = Tk()
    show.geometry("920x400")
    show.title("Fare Details")
    canvas = Canvas(
        show, scrollregion="0 0 0 10000", width=900, height=400,bg="#EED5B7")  #
    canvas.grid(row=0, column=0,sticky = NSEW)  # sticky=tk.NSEW

    scroll = Scrollbar(show, orient=VERTICAL, command=canvas.yview)
    scroll.grid(row=0, column=1, sticky=NS)  # , sticky=NS
    canvas.config(yscrollcommand=scroll.set)


    frame = Frame(show,bg="#EED5B7")


    l1 = Label(frame , text="Id",font=("Comic Sans MS", 11),bg="#EED5B7")
    l2 = Label(frame,text = "Goods Type",font=("Comic Sans MS", 11),bg="#EED5B7")
    l3 = Label(frame , text = "Rate Per KG",font=("Comic Sans MS", 11),bg="#EED5B7")
    l4 = Label(frame, text="Rate Per KM",font=("Comic Sans MS", 11),bg="#EED5B7")
    l5 = Label(frame, text="Rate Per Width",font=("Comic Sans MS", 11),bg="#EED5B7")
    l6 = Label(frame , text = "Rate Per Height",font=("Comic Sans MS", 11),bg="#EED5B7")
    t = (l1,l2,l3,l4,l5,l6)

    p = 0
    for k in t:
        k.grid(row =  0, column = p)
        p = p+1
    i = 1

    for each_record in my_conn:
        for j in range(len(each_record)):
            e = Entry(frame,width=20,font=("Comic Sans MS", 9),bg = "#FFEBCD")#width=10, fg='blue'
            e.grid(row=i, column=j)
            e.insert(END, each_record[j])
        i = i + 1
    item = canvas.create_window((2, 2), anchor=NW, window=frame)  # (2, 2), anchor=NW,

    show.mainloop()
