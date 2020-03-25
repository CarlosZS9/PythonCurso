class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")


#polimorfismo ayuda a ahorrar codigo 

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Coche()

desplazamientoVehiculo(miVehiculo)