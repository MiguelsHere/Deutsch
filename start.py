from tkinter import *
from tkinter import messagebox
from Views.Common.Fonts import *
from Controllers.CollectionController import CollectionController as Controller


jan = Tk()
jan.geometry('640x360')
jan.title("Language Helper")
#jan.iconbitmap("Views/Common/jul.ico")


title = Label(jan, text="Language Helper", font=Title, pady='10')
title.pack()

f1 = Frame(jan, pady='50')
f1.pack()

btnPraticar = Button(f1, text="Praticar")
btnPraticar.pack()

btnTeste = Button(f1, text="Começar Teste")
btnTeste.pack()

btnGerir = Button(f1, text="Gerir Coleções")
btnGerir.pack()

btnSair = Button(f1, text="Sair", command=jan.destroy, bg="red", pady=)
btnSair.pack()

contr = Controller()


if contr.con is None:
    messagebox.showerror("ERRO", "Houve na conexão de base de dados!")


jan.mainloop()
