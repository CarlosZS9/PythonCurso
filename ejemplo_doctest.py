def compruebaMail(mailUsuario):

	"""
	La funcion compruebaMail evalua un mail recibido
	en busca de la @. Si tiene una @ es correcto,
	si tiene mas de na @ es icnorrecto, si la @ esta al final es incorrecto

	>>> compruebaMail('juan@cursos.es')
	True


	>>> compruebaMail('juancursos.es@')
	False


	>>> compruebaMail('juancursos.es')
	False

	>>> compruebaMail('juan@curso@s.es')
	False
	"""

	arroba=mailUsuario.count('@')

	if (arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@') == 0):
		return False
	else:
		return True

import doctest
doctest.testmod()
