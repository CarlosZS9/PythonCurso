from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

#label y cuadro nombre
minombre=StringVar()

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="w", padx=10,pady=10)

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="blue",justify="left")

#label y cuadro contraseña
Label2=Label(miFrame,text="Contraseña:")
Label2.grid(row=1,column=0,sticky="w",padx=10,pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

#label y cuadro apellido
Label3=Label(miFrame,text="Apellido:")
Label3.grid(row=2,column=0, sticky="w",padx=10,pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)

#label y cuadro direccion
Label4=Label(miFrame,text="Dirección:")
Label4.grid(row=3,column=0,sticky="w",padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

#label comentario y texto
Label5=Label(miFrame,text="Comentario:")
Label5.grid(row=4,column=0,sticky="w",padx=10,pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsw")
textoComentario.config(yscrollcommand=scrollVert.set)


#botones
def codigoBoton():
	minombre.set("Carlos")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()