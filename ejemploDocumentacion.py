from modulos import funciones_matematicas
class Areas:
	'''Esta clase calcula las areas de diferentes figuras geometricas'''

	def areaCuadrado(lado):   
		'''Calcula el area de un cuadrado
		elevando al cuadrado el lado pasado por parametro'''
		return "El área del cuadrado es: " + str(lado*lado)



	def areaTriangulo(base,altura):
		'''Calcula el area de un triangulo
		utilizando los parametros base y altura'''
		return "El área del triangulo es: " + str((base*altura)/2)


#print(areaCuadrado(3))
#print(areaCuadrado.__doc__)
#help(areaCuadrado)


#print(areaTriangulo(2,7))
#help(areaTriangulo)

#help(Areas.areaTriangulo)

#help(Areas)
help(funciones_matematicas)