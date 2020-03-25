import re

#funcion match() busca al principio de una cadena 
#funcion search() busca en toda la cadena



'''nombre1="Sandra Lopéz"
nombre2="Antonio Gómez"
nombre3="sandra López"'''

'''if re.match("Sandra",nombre1):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")'''


'''if re.match("Sandra",nombre3, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")'''


'''nombre1="Jara Lopéz"
nombre2="Antonio Gómez"
nombre3="Lara López"

if re.match(".ara",nombre3, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")'''

'''cadena1="Jara Lopéz"
cadena2="5454645454"
cadena3="a54565454"

if re.match("\d",cadena3):
	print("Hemos encontrado el numero")
else:
	print("No hemos encontrado el numero")'''



'''nombre1="Jara López"
nombre2="Antonio Gómez"
nombre3="Lara López"

if re.search("López",nombre3):
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado el nombre")'''

codigo1="sfdsfsgvdfgfdgdfgdfvdfvdfvv71fvdfvdsfvdfvdf"
codigo2="dfvdfvdfvdbdfbdfd71dfbdfbdfbdbdfbdfbdbdb"
codigo3="bdfbdfbdfbdb  ggdgdgdfgdfgdfgg"

if re.search("71",codigo3):
	print("Hemos encontrado el numero")
else:
	print("No hemos encontrado el numero")