import sqlite3
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()


"""miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[

	("pelota",20,"jugueteria"),
	("pantalón",15,"confección"),
	("destornillador",25,"ferreteria"),
	("jarrón",45,"cerámica"),
	("pantalónes",35,"confección")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)"""

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'jugueteria')")

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION= 'confección'")
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO= 35 WHERE NOMBRE_ARTICULO='pelota'")
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

"""productos=miCursor.fetchall()
print(productos)"""


miConexion.commit()
miConexion.close()
