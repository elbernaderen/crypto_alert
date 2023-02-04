import tkinter as tk 
from tkinter import messagebox
from client.gui_app import Frame,barra_menu

from model.mensaje import detener

def main():
    #here we create the interface

    root = tk.Tk()
    root.title("Crypto Alert")
    root.resizable(0,0)
    #change ico

    root.iconbitmap("ico/cp_logo.ico")
    # container
    
    # change the background color
    barra_menu(root)

    app = Frame(root = root)
    
    

    def on_closing(): 
        if messagebox.askokcancel("Salir", "¿Desea salir?"):
            detener()
            root.destroy()

    root.protocol("WM_DELETE_WINDOW",on_closing )

    app.mainloop()

if __name__ == "__main__":
    main()