from io import open 

# r: read, a: append, w: write

archivo_texto=open("archivo.txt","r+") #lectura y escritura

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines()

lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close

"""archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())"""

#seek() desplaza el puntero en el archivo



"""frase="Estupendo dia para estudiar python \n el miércoles"

archivo_texto.write(frase)

archivo_texto.close()"""




"""texto=archivo_texto.read()

archivo_texto.close()

print(texto)"""



#readlines() lee lineas y lo almacena en una lista
"""lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto[1])"""



#agregar linea de texto a un archivo existente

"""archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")
archivo_texto.close()"""