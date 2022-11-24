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

        self.label_rsi = tk.Label(self,text ="RSI: ")
        self.label_rsi.grid(row = 2,column = 0, padx=10, pady=10)
        self.label_rsi.config()

        self.label_macd = tk.Label(self,text ="MACD: ")
        self.label_macd.grid(row = 3,column = 0, padx=10, pady=10)
        self.label_macd.config()

        self.label_media = tk.Label(self,text ="Media: ")
        self.label_media.grid(row = 4,column = 0, padx=10, pady=10)
        self.label_media.config()


        self.entry_simbolo = tk.Entry(self)
        self.entry_simbolo.grid(row = 0,column = 1, padx=10, pady=10)

        self.entry_valor = tk.Entry(self)
        self.entry_valor.grid(row = 1,column = 1, padx=10, pady=10)

        self.entry_rsi = tk.Entry(self)
        self.entry_rsi.grid(row = 2,column = 1, padx=10, pady=10)

        self.entry_macd = tk.Entry(self)
        self.entry_macd.grid(row = 3,column = 1, padx=10, pady=10)

        self.entry_media = tk.Entry(self)
        self.entry_media.grid(row = 4,column = 1, padx=10, pady=10)
        self.entry_media_limite = tk.Entry(self)
        self.entry_media_limite.grid(row = 4,column = 3, padx=10, pady=10)

        # Botones
        self.boton_inicio = tk.Button(self, text = "Iniciar")
        self.boton_inicio.config(width = 20)
        self.boton_inicio.grid(row = 6,column = 1, padx=10, pady=10)