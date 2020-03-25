import pickle

#volcar lista en binario

"""lista_nombres=["Pedro","Ana","Maria","Isabel"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)"""

#cargar una lista en binario
fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)