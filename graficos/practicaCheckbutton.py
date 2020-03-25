from tkinter import *

root=Tk()
root.title("Ejemplo")



playa=IntVar()
montaña=IntVar()
turismoRural=IntVar()


def opcionesViaje():
	opcioneEscogida=""

	if(playa.get()==1):
		opcioneEscogida+="playa "

	if(montaña.get()==1):
		opcioneEscogida+="montaña "

	if(turismoRural.get()==1):
		opcioneEscogida+="turismoRural "

	textoFinal.config(text=opcioneEscogida)



#foto=PhotoImage(file="avion.jpg")
#Label(root,image=foto).pack()


frame=Frame(root)
frame.pack()

Label(frame,text="Elige destinos",width=50).pack()


Checkbutton(root,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()

Checkbutton(root,text="Montaña",variable=montaña,onvalue=1,offvalue=0,command=opcionesViaje).pack()

Checkbutton(root,text="Turismo Rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()