#estructuras que extraen valores de una funcion y que se pueden recorrer
#funcion normal con lista
#append agrega a lista elementos
"""def generaPares(Limite):
	num=1
	miLista=[]
	while num<Limite:
		miLista.append(num*2)
		num+=1
	return miLista
print(generaPares(10))"""

#funcion con generador
def generaPares(Limite):
	num=1
	
	while num<Limite:
		yield num*2
		num+=1
devuelvePAres=generaPares(10)
#entre llamadas el generador entra en estado de suspension

"""for i in devuelvePAres:
	print(i) un for para que imprima todos los 9 valores"""

print(next(devuelvePAres))
print("Aqui podria ir mas codigo....")
print(next(devuelvePAres))
print("Aqui podria ir mas codigo....")
print(next(devuelvePAres))

#yield from: simplificar el codigo de los genereadores en el caso de utilizar bucles anidados

print("Generadores 2 con Yield from")

#en python si ponemos un asterisco es que va a recibir un numero indeterminado de elementos
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento:
			yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))