
bucle = True
while bucle:
	print("1.-imprimir valor de i menor a 10")
	print("2.-Programa de calculo de raiz cuadrada")
	print("3.-Salir")

	op=int(input("Ingresa la opcion: "))

	if op==1:
		i=1
		while i<=10:
			print(f"se cumple el valor, i vale: {i}")
			i=i+1
		print("Terminó la ejecución")

	if op==2:
		import math
		numero=int(input("Ingresa un numero"))
		intentos=0

		while numero<0:
			print("No se puede hallar la raiz de un numero negativo")
			if intentos==2:
				print("Has consumido demasiados intentos. El Programa ha finalizado")
				break;
			numero=int(input("Introduce un numero "))
			if numero<0:
				intentos=intentos+1

		if intentos<2:
			solucion=math.sqrt(numero)
			print("La raiz cuadrada de " + str(numero)+ " es: " + str(solucion))

	if op==3:
		print("Saliendo")
		bucle=False
		
		