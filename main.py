import os
from tkinter import *
import MyWeasel as MW

class App:

    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 0
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 0
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 0
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 0
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 10
        self.sextoContainer.pack()

        self.EntradaLabel = Label(self.primeiroContainer,text="Entrada", font=self.fontePadrao)
        self.EntradaLabel.pack(side=LEFT)

        self.Entrada = Entry(self.primeiroContainer)
        self.Entrada["width"] = 30
        self.Entrada["font"] = self.fontePadrao
        self.Entrada.pack(side=LEFT)

        self.CopiasLabel = Label(self.segundoContainer,text="Strings Geradas", font=self.fontePadrao)
        self.CopiasLabel.pack(side=LEFT)

        self.Copias = Entry(self.segundoContainer)
        self.Copias["width"] = 30
        self.Copias["font"] = self.fontePadrao
        self.Copias.pack(side=LEFT)

        self.mutacaoLabel = Label(self.terceiroContainer,text="Taxa de Mutacao", font=self.fontePadrao)
        self.mutacaoLabel.pack(side=LEFT)

        self.mutacao = Entry(self.terceiroContainer)
        self.mutacao["width"] = 30
        self.mutacao["font"] = self.fontePadrao
        self.mutacao.pack(side=LEFT)

        self.targetLabel = Label(self.quartoContainer,text="Target", font=self.fontePadrao)
        self.targetLabel.pack(side=LEFT)

        self.target  = Entry(self.quartoContainer)
        self.target["width"] = 30
        self.target["font"] = self.fontePadrao
        self.target.pack(side=LEFT)

        self.iniciar = Button(self.quintoContainer)
        self.iniciar["text"] = "Iniciar !"
        self.iniciar["width"] = 12
        self.iniciar["command"] = (lambda : resultado(self.Entrada.get(), self.Copias.get(), self.mutacao.get(), self.target.get()))
        self.iniciar.pack()
       
        self.scrollbar = Scrollbar(self.sextoContainer) 
        self.scrollbar.pack( side = RIGHT, fill = Y ) 

        self.mylist = Listbox(self.sextoContainer, yscrollcommand = self.scrollbar.set, ) 
        self.mylist.pack( side = LEFT, fill = BOTH ) 
        self.mylist["width"] = 200
        self.mylist["height"] = 400
        self.scrollbar.config( command = self.mylist.yview )
        
        def resultado(CONST_STR, CONST_SIZE, CONST_PROB, ENTRADA):
            for i in (MW.Weasel(ENTRADA, CONST_SIZE, CONST_PROB, CONST_STR)):
                self.mylist.insert(END, str(i))
                
root = Tk()
root.geometry("600x600")
root.title("Weasel")
App(root)
root.mainloop()
