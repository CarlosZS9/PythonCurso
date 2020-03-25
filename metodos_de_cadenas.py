edad=input("Ingresa tu edad: ")


while(edad.isdigit()==False):
	print("Ingresa un valor numerico")

	edad=input("Ingresa tu edad: ")


if (int(edad)<18):
	print("No puedes pasar")
else:
	print("Puedes pasar")

