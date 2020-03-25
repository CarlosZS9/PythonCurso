#continue salta la vuelta del bucle en el que se encuentra
for letra in "Python":
	if letra=="h":
		continue
	print("Viendo la letra: "+letra)


#len(variable) dice el numero de caracteres en un str
nombre="Pildoras informaticas"

contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1
print(contador)

#pass devuelve un null en el bucle. Con ctrl + c se sale del bucle infinito
class MiClase:
	pass #Para implementar mas adelante

#else sirve como en el condicional
email=input("Introduce tu email: ")
for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False
print(arroba)

