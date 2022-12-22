import tkinter as tk
from messenger_d import mensajero
from model.mensaje import Valores_alerta

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

        self.label_intervalo = tk.Label(self,text ="Intervalo: ")
        self.label_intervalo.grid(row = 1,column = 0, padx=10, pady=10)
        self.label_intervalo.config()

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

        self.mi_simbolo = tk.StringVar()
        self.entry_simbolo = tk.Entry(self,textvariable = self.mi_simbolo)
        self.entry_simbolo.grid(row = 0,column = 1, padx=10, pady=10)
        
        self.mi_intervalo = tk.StringVar()
        self.entry_intervalo = tk.Entry(self,textvariable = self.mi_intervalo)
        self.entry_intervalo.grid(row = 0,column = 1, padx=10, pady=10)

        self.mi_valor = tk.StringVar()
        self.entry_valor = tk.Entry(self,textvariable = self.mi_valor)
        self.entry_valor.grid(row = 1,column = 1, padx=10, pady=10)

        self.mi_rsi = tk.StringVar()
        self.entry_rsi = tk.Entry(self,textvariable = self.mi_rsi)
        self.entry_rsi.grid(row = 2,column = 1, padx=10, pady=10)

        self.mi_macd = tk.StringVar()
        self.entry_macd = tk.Entry(self,textvariable = self.mi_macd)
        self.entry_macd.grid(row = 3,column = 1, padx=10, pady=10)

        self.mi_media = tk.StringVar()
        self.mi_media_limite = tk.StringVar()
        self.entry_media = tk.Entry(self,textvariable = self.mi_media)
        self.entry_media.grid(row = 4,column = 1, padx=10, pady=10)
        self.entry_media_limite = tk.Entry(self,textvariable = self.mi_media_limite)
        self.entry_media_limite.grid(row = 4,column = 3, padx=10, pady=10)

        # Boton
    
        self.boton_inicio = tk.Button(self, text = "Iniciar",command = self.enviar_datos)
        self.boton_inicio.config(width = 20)
        self.boton_inicio.grid(row = 6,column = 1, padx=10, pady=10)

 



def enviar_datos(self):
    dato = Valores_alerta(
        self.mi_simbolo.get(),
        self.mi_valor.get(),
        self.mi_rsi.get(),
        self.mi_macd.get(),
        self.mi_media.get(),
        self.mi_media_limite.get()
        )
