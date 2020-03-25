from tkinter import *

root=Tk()

miFrame=Frame(root,width=500,height=400)

miFrame.pack()

#imagen label

#miImagen=PhotoImage(file="mouse.gif")

#Label(miFrame, image=miImagen).place(x=100,y=200)
Label(miFrame, text="Hola alumnos de Python", fg="red",font=("Comics Sans MS",18)).place(x=100,y=200)


root.mainloop()