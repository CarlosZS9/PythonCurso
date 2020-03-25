def divide():
	try:

		op1=float((input("Introduce el primer numero")))
		op2=float((input("Introduce el segundo numero")))

		print("La division es:  "+ str(op1/op2))
	except ValueError:
		print("El valor es erroneo")

	except ZeroDivisionError:
		print("No se puede dividir entre 0")


#finally siempre se ejecuta		
	finally:
		print("Calculo finalizado")


#divide()


#Raise: Mandamos errores personalizados 


"""def evaluaEdad(edad):
	if edad<0:
		raise MipropioError("No se permiten edades negativas")


	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "Cuídate..."


print(evaluaEdad(-15))"""

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError ("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero:  ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("programa terminado")
