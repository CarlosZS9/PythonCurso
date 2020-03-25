#la i toma el valor de la lista por ejemplo
"""for i in ["primavera","verano","otoño","invierno"]:
		#print("Hola", end=" ")
		
#en una cadena se imprime el numero de caracteres
		print("Hola", end=" ")"""

#es un rango, se imprime el valor en cada rango se toman 3 valores en range el tercero muestra de cuanto sube cada uno
"""for i in range(5,50,3): 
		print(f"valor de la variable {i}")"""


#f es una notacion especial, funcion tipo f. regresa el numero de caracteres de un string
#print(len("juan")) 


#verificacion si email tiene @
valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
	if email[i]=="@":
		valido=True
if valido:
	print("Email correcto")
else:
	print("Email incorrecto")