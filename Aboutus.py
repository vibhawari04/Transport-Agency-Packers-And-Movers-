from tkinter import *

def aboutuswin():

    au=Tk()
    au.title("About us")
    au.geometry("600x700")
    au.resizable(False,False)
    sbackground = PhotoImage(file="images/ABus.png", master=au)
    Label(au, image=sbackground).place(x=-2, y=0)

    au.mainloop()
