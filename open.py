from tkinter import *
from tkinter import messagebox
from usermainwin import *
import mysql.connector
def openw():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="starmoversdb"

    )
    my_conn = con.cursor()
    q = "SELECT * FROM bookingdetail "
    ####### end of connection ####
    my_conn.execute(q)

    my_w = Tk()
    my_w.geometry("1450x250")
    my_w.title("Booking Details")
    my_w.config(bg = "#EED5B7")#FFF68F

    canvas = Canvas(
        my_w, scrollregion="0 0 0 10000", width=1430, height=700, bg="#EED5B7")  #
    canvas.grid(row=0, column=0, sticky=NSEW)  # sticky=tk.NSEW

    scroll = Scrollbar(my_w, orient=VERTICAL, command=canvas.yview)
    scroll.grid(row=0, column=1, sticky=NS)  # , sticky=NS
    canvas.config(yscrollcommand=scroll.set)

    frame = Frame(my_w, bg="#EED5B7")

    l1 = Label(frame , text="BOOKING ID",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l2 = Label(frame,text = "DATE ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l3 = Label(frame , text = "USERNAME ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l4 = Label(frame, text="FROM ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l5 = Label(frame, text="TO",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l6 = Label(frame , text = "GOODS DETAILS ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l7 = Label(frame, text="RATE PER KM  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l8 = Label(frame, text="RATE PER KG  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l9 = Label(frame, text="NAME  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l10 = Label(frame, text="MOBILE  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l11 = Label(frame, text="ADDRESS  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l12 = Label(frame, text="CUSTOMER ID  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l13 = Label(frame, text="STATUS  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l14 = Label(frame, text="RATE PER WIDTH  ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    l15 = Label(frame, text="RATE PER HEIGHT ",font=("Comic Sans MS", 9),bg = "#EED5B7")
    t = (l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15)

    p = 0
    for k in t:
        k.grid(row=0, column=p)
        p = p + 1



    i = 1

    for each_record in my_conn:

        for j in range(len(each_record)):
            e = Entry(frame,width=12,bg = "#FFEBCD",font=("Comic Sans MS", 9))#width=10, fg='blue'
            e.grid(row= i , column=j)
            e.insert(END, each_record[j])
        i = i + 1
    item = canvas.create_window((2, 2), anchor=NW, window=frame)  # (2, 2), anchor=NW,

    my_w.mainloop()

