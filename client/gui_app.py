import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

    menu_inicio.add_command(label = "Sesion Telegram")
    menu_inicio.add_command(label = "Sesion Binance")
    
class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root,width=360,height=450)
        self.root = root
        self.pack()
        self.label_varios()
        

    def label_varios(self):
        self.label_simbolo = tk.Label(self,text ="Nombre Simbolo: ")
        self.label_simbolo.grid(row = 0,column = 0, padx=10, pady=10)
        self.label_simbolo.config()

        self.label_valor = tk.Label(self,text ="Valor: ")
        self.label_valor.grid(row = 1,column = 0, padx=10, pady=10)
        self.label_valor.config()

        self.entry_simbolo = tk.Entry(self)
        self.entry_simbolo.grid(row = 0,column = 1, padx=10, pady=10)

        self.entry_valor = tk.Entry(self)
        self.entry_valor.grid(row = 1,column = 1, padx=10, pady=10)