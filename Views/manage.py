from tkinter import *
from tkinter import messagebox
from Views.Common.Fonts import *


def back(principal, jan):
    principal.deiconify()
    jan.destroy()

def try_fetch_all_collection(collection):
    cont = collection.fetch_all_collections()
    if not cont:
        messagebox.showerror("Erro", "Não à coleções!")
    return cont

def try_create_collection(collection, name,language , description = "", category = ""):
    if collection.create_collection(name, language, description, category):
        messagebox.showinfo("Succeso", "Coleção criada com sucesso!")
    else:
        messagebox.showerror("Erro", "Não foi possivel criar a coleção!")

def try_delete_collection(collection, id, collections):
    for x in collections:
        if x[0] == id:
            nome = x[1]

    if messagebox.askyesno("Confirma",f"Tem acerteza que deseja apagar {nome}?"):
        collection.delete_collection(id)
        
def manage(principal, collection):

    principal.withdraw()

    jan = Toplevel()
    
    jan.geometry('800x360')
    jan.title("Language Helper: Gerir Coleções")
    jan.iconbitmap("Views/Common/icon.ico")

    titulo = Label(jan, text="Gerir Coleções", font=Title, pady='10')
    titulo.pack()

    info = Frame (jan, pady='50')
    info.pack()

    inserir = Frame(jan)
    inserir.pack()

    opcoes = Frame(jan, pady='25')
    opcoes.pack()

    #info
    collections = try_fetch_all_collection(collection)
 
    lbId = Label(info, text="Id")
    lbId.grid(row=0, column=0)

    lbNome = Label(info, text="Nome")
    lbNome.grid(row=0, column=1)

    lbLing = Label(info, text="Lingua")
    lbLing.grid(row=0, column=2)

    lbCat = Label(info, text="Categoria")
    lbCat.grid(row=0, column=3)

    for i in range(len(collections)):
        for j in range(4):
                e = Entry(info, justify=CENTER)
                e.grid(row=i+1, column=j)
                e.insert(END, collections[i][j])
                e.config(state=DISABLED)

    #inserir
    LabelNome = Label(inserir, text="Nome:")
    LabelNome.grid(row=3, column=0)

    EntryNome = Entry(inserir)
    EntryNome.grid(row = 3, column=1)

    LabelLingua = Label(inserir, text="Lingua:")
    LabelLingua.grid(row=3, column=2)

    EntryLingua = Entry(inserir)
    EntryLingua.grid(row = 3, column=3)

    LabelCategoria = Label(inserir, text="Categoria:")
    LabelCategoria.grid(row=3, column=4)

    EntryCategoria = Entry(inserir)
    EntryCategoria.grid(row = 3 , column=5)


    #opcoes
    btnCriar = Button(opcoes, text="Criar", command=lambda: try_create_collection(collection, EntryNome.get().strip(), EntryLingua.get().strip(), EntryCategoria.get().upper().strip()))
    btnCriar.grid(row = 0, column=0)

    btnApagar = Button(opcoes, text="Apagar", bg="red", command=lambda: try_delete_collection(collection, idparaApagar.get()))
    btnApagar.grid(row=0, column=1)

    idparaApagar = Entry(opcoes, width="5", justify="center")
    idparaApagar.grid(row=0,column=2)

    btnVoltar = Button(opcoes, text="Voltar", command=lambda :back(principal, jan))
    btnVoltar.grid(row = 0, column=3)

    jan.mainloop()
