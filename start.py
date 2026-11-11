from tkinter import *
from tkinter import messagebox
from Views.Common.Fonts import *
from Controllers.CollectionController import CollectionController as Controller
from Views.manage import *

jan = Tk()

jan.geometry('640x360')
jan.title("Language Helper")
#jan.iconbitmap("Views/Common/icon.ico")

contr = Controller()

if contr.con is None:
    messagebox.showerror("Erro", "Houve um erro na conexão à base de dados!")
    jan.destroy()

titulo = Label(jan, text="Language Helper", font=Title, pady='10')
titulo.pack()

f1 = Frame(jan, pady='50')
f1.pack()

btnPraticar = Button(f1, text="Praticar")
btnPraticar.pack()

btnTeste = Button(f1, text="Começar Teste")
btnTeste.pack()

btnGerir = Button(f1, text="Gerir Coleções",command=lambda :manage(jan, contr))
btnGerir.pack()

btnSair = Button(f1, text="Sair", command=jan.destroy, bg="red")
btnSair.pack()

jan.mainloop()
