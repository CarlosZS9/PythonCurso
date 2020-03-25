from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)

#raiz.iconbitmap("gato.ico")   para cambiar el icono

#raiz.geometry("650x350")

raiz.config(bg="green")

raiz.config(bd="45")

raiz.config(relief="groove")

raiz.config(cursor="pirate")


miFrame=Frame()

#miFrame.pack(fill="both", expand="True")
miFrame.pack(side="left", anchor="n")

miFrame.config(bg="white")

miFrame.config(width="650", height="350")

miFrame.config(bd="35")

miFrame.config(relief="sunken")

miFrame.config(cursor="hand2")

raiz.mainloop()

