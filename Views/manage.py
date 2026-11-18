from tkinter import *
from tkinter import messagebox
from Views.Common.Fonts import *


def back(principal, jan):
    principal.deiconify()
    jan.destroy()

def try_fetch_all_collection(collection):
    if not collection.fetch_all_collections():
        messagebox.showerror("Erro", "Não foi buscar as coleções!")

def try_create_collection(collection, name,language , description = "", category = ""):
    if collection.create_collection(name, language, description, category):
        messagebox.showinfo("Succeso", "Coleção criada com sucesso!")
    else:
        messagebox.showerror("Erro", "Não foi possivel criar a coleção!")
        

def manage(principal, collection):

    principal.withdraw()

    jan = Toplevel()
    
    jan.geometry('800x360')
    jan.title("Language Helper: Gerir Coleções")
    jan.iconbitmap("Views/Common/icon.ico")

    titulo = Label(jan, text="Gerir Coleções", font=Title, pady='10')
    titulo.pack()


    insert = Frame(jan)
    insert.pack()

    options = Frame(jan)
    options.pack()

    
    LabelNome = Label(insert, text="Nome:")
    LabelNome.grid(row=3, column=0)

    EntryNome = Entry(insert)
    EntryNome.grid(row = 3, column=1)


    LabelDescricao = Label(insert, text="Descrição:")
    LabelDescricao.grid(row=3, column=2)

    EntryDescricao = Entry(insert)
    EntryDescricao.grid(row = 3, column=3)


    LabelLingua = Label(insert, text="Lingua:")
    LabelLingua.grid(row=3, column=4)

    EntryLingua = Entry(insert)
    EntryLingua.grid(row = 3, column=5)


    LabelCategoria = Label(insert, text="Categoria:")
    LabelCategoria.grid(row=3, column=6)

    EntryCategoria = Entry(insert)
    EntryCategoria.grid(row = 3 , column=7)



    btnCriar = Button(options, text="Criar", command=lambda :try_create_collection(collection, EntryNome.get().strip(), EntryLingua.get().strip(), EntryDescricao.get().strip(), EntryCategoria.get().upper().strip()))
    btnCriar.grid(row = 0, column=0)

    btnApagar = Button(options, text="Apagar", bg="red")
    btnApagar.grid(row=0, column=1)

    btnVoltar = Button(options, text="Voltar", command=lambda :back(principal, jan))
    btnVoltar.grid(row = 0, column=2)

    jan.mainloop()
