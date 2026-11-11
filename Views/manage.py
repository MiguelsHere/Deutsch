from tkinter import *
from tkinter import messagebox
from Views.Common.Fonts import *


def manage(principal, contr):

    principal.destroy()

    jan = Tk()
    
    jan.geometry('640x360')
    jan.title("Language Helper: Gerir Coleções")
    #jan.iconbitmap("Views/Common/icon.ico")

    title = Label(jan, text="Language Helper", font=Title, pady='10')
    title.pack()

    f1 = Frame(jan, pady='50')
    f1.pack()

    jan.mainloop()

        
