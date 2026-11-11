from tkinter import *
from tkinter import messagebox
from Views.Common.Fonts import *


def back(principal, jan):
    principal.deiconify()
    jan.destroy()

def try_create_collection(contr, name,language , description = "", category = ""):
    if contr.create_collection(name, language, description, category):
        messagebox.showinfo("Succeso", "Coleção criada com sucesso!")
    else:
        messagebox.showerror("Erro", "Não foi possivel criar a coleção!")

def manage(principal, contr):

    principal.withdraw()

    jan = Toplevel()
    
    jan.geometry('640x360')
    jan.title("Language Helper: Gerir Coleções")
    #jan.iconbitmap("Views/Common/icon.ico")

    title = Label(jan, text="Gerir Coleções", font=Title, pady='10')
    title.pack()

    f1 = Frame(jan, pady='50')
    f1.pack()


    LabelNome = Label(f1, text="Nome:")
    LabelNome.grid(row=0, column=0)

    EntryNome = Entry(f1)
    EntryNome.grid(row = 0 , column=1)


    LabelDescricao = Label(f1, text="Descrição:")
    LabelDescricao.grid(row=1, column=0)

    EntryDescricao = Entry(f1)
    EntryDescricao.grid(row = 1 , column=1)


    LabelLingua = Label(f1, text="Lingua:")
    LabelLingua.grid(row=2, column=0)

    EntryLingua = Entry(f1)
    EntryLingua.grid(row = 2, column=1)


    LabelCategoria = Label(f1, text="Categoria:")
    LabelCategoria.grid(row=3, column=0)

    EntryCategoria = Entry(f1)
    EntryCategoria.grid(row = 3 , column=1)

    btnCriar = Button(f1, text="Criar", command=lambda :try_create_collection(contr, EntryNome.get(), EntryLingua.get(), EntryDescricao.get(), EntryCategoria.get()))
    btnCriar.grid(row = 4, column=0)

    btnVoltar = Button(f1, text="Voltar", command=lambda :back(principal, jan))
    btnVoltar.grid(row = 4, column=2)

    jan.mainloop()

        
