import tkinter as tk 
from client.gui_app import Frame,barra_menu

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
    app.mainloop()

if __name__ == "__main__":
    main()