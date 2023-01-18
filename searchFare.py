from tkinter import*
from tkinter import messagebox
import mysql.connector
from usermainwin import *
def searchF():

   def find():
      find = Tk()
      find.geometry("400x400")
      find.config(bg="#FFC1C1")
      find.resizable(0,0)

      con = mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="1234",
         db="starmoversdb"
      )

      if con != None:
         cur = con.cursor()
         q = " SELECT * FROM faredetail where transporttype = %s "
         transporttype = E1.get()
         tpdata = (transporttype,)

         cur.execute( q ,tpdata)
         print("type ",type(cur))
         data = cur.fetchone()
         heading = Label(find,text = "FARE DETAILS",bg = "#FFC1C1",font=("Comic Sans MS", 15,"bold"))
         heading.place(x=120,y=20)
         l1 = Label(find, text="Id",font=("Comic Sans MS", 9),bg = "#FFC1C1")
         l2 = Label(find, text="Goods Type",font=("Comic Sans MS", 9),bg = "#FFC1C1")
         l3 = Label(find, text="Rate Per KG",font=("Comic Sans MS", 9),bg = "#FFC1C1")
         l4 = Label(find, text="Rate Per KM",font=("Comic Sans MS", 9),bg = "#FFC1C1")
         l5 = Label(find, text="Rate Per Width",font=("Comic Sans MS", 9),bg = "#FFC1C1")
         l6 = Label(find, text="Rate Per Height",font=("Comic Sans MS", 9),bg = "#FFC1C1")
         t = (l1, l2, l3, l4, l5, l6)

         p = 90
         for k in t:
            k.place(x=30, y =p)
           # k.grid(row=5, column=p)
            p = p + 40

         if cur.rowcount == 1:
            j = 90
            for i in data:
               e = Entry(find, width=10,font=("Comic Sans MS", 9))
               #e.grid(row = 6 , column = j)
               e.place(x = 150,y = j)
               e.insert(END, i)
               j=j+40
         else:
            messagebox.showinfo("info", "No Record Found")
      else:
         messagebox.showinfo("info","not found")

      find.mainloop()

   def check():
      con = mysql.connector.connect(
         host="localhost",
         user="root",
         password="1234",
         database="starmoversdb"

      )
      if con:

         transporttype = E1.get()


         qry = "SELECT * FROM faredetail where transporttype=%s"

         tpdata = (transporttype,)

         cur = con.cursor()
         cur.execute(qry, tpdata)
         data = cur.fetchone()
         if data != None:
            #search.wm_withdraw()
            find()

         else:
            messagebox.showinfo("info", "Incorrect Input")

      else:
         messagebox.showinfo("Success", "NO Done")




   search = Tk()
   search.geometry("300x300")
   search.title("search fare")
   search.resizable(0,0)
   search.config(bg="#FAEBD7")


   heading = Label(search, text = "Search Fare ",font=("Comic Sans MS", 15,"bold"),bg="#FAEBD7")
   L1 = Label(search,text= "Goods Type",font=("Comic Sans MS", 12),bg = "#FAEBD7")
   E1 = Entry(search,font=("Comic Sans MS", 10))

   Btn = Button(search,text = " Search" ,command = check,font=("Comic Sans MS", 12),bg= "#DEB887")

   heading.place(x=20 , y = 10)
   L1.place(x = 20 , y = 90)
   E1.place(x = 120 , y= 95)
   Btn.place(x = 110 , y = 160)


   search.mainloop()
