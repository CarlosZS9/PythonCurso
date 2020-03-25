import re


'''cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#print(re.search("aprender",cadena))

textoBuscar="Python"'''


'''if re.search(textoBuscar,cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")'''

'''textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())'''

#print(len(re.findall(textoBuscar,cadena)))

'''lista_nombres=['http://pildorasinformaticas.es',
				'ftp://pildorasinformaticas.es',
				'http://pildorasinformaticas.com',
				'ftp://pildorasinformaticas.com'
				]'''


'''lista_nombres=['http://informaticaenespaña.es',
				'http://pildorasinformaticas.es',
				'http://pildorasinformaticas.com'
				]'''



'''lista_nombres=['hombres',
				'mujeres',
				'mascotas',
				'camión',
				'camion']'''

'''lista_nombres=['Ana',
				'Pedro',
				'María',
				'Rosa',
				'Sandra',
				'Celia']'''

lista_nombres=['Ma.1',
				'Se1',
				'Ma2',
				'Ba1',
				'Ma:3',
				'Val1',
				'Val2',
				'Ma4',
				'Ma.5',
				'MaA',
				'MaB',
				'Ma:C']



'''for elemento in lista_nombres:
	if re.findall('^Sandra',elemento):
		print(elemento)'''

'''for elemento in lista_nombres:
	if re.findall('Martín$',elemento):
		print(elemento)'''


'''for elemento in lista_nombres:
	if re.findall('niñ[oa]s',elemento):
		print(elemento)'''

'''for elemento in lista_nombres:
	if re.findall('cami[oó]n',elemento):
		print(elemento)'''

'''for elemento in lista_nombres:
	if re.findall('[o-t]$',elemento):
		print(elemento)'''

'''for elemento in lista_nombres:
	if re.findall('Ma[0-3]',elemento):
		print(elemento)'''

'''for elemento in lista_nombres:
	if re.findall('Ma[^0-3]',elemento):
		print(elemento)'''

'''for elemento in lista_nombres:
	if re.findall('Ma[0-3A-B]',elemento):
		print(elemento)'''

for elemento in lista_nombres:
	if re.findall('Ma[.:]',elemento):
		print(elemento)