cadena1 = "Hola Soy Joan"
cadena2 = "Bienvenidos a Python"

#libreria de metodos

#DIR devuelve la lsita de atributos válidos del objeto pasado

#UPPER convierte en Mayusculas
#LOWER convierte en minisculas
#CAPITALIZE convierte la primera letra en Mayuscula

#el upper convierte a mayusculas 
resultado = cadena1.upper() 

print(resultado)

#el lower convierte a minuscula
resultado = cadena2.lower() 

print(resultado)

#el capitalize convierte la primera letra en Mayuscula
resultado = cadena2.capitalize() 

print(resultado)

#FIND nos busca un valor que le pidamos (Busca el valor de una cadena en otra cadena) 
#arroja la posicion si no encuentra nada o no hay consiencia nos devuelve -1


busqueda_find = cadena1.find("a")
print(busqueda_find)

busqueda_index = cadena1.index("a")

print(busqueda_index)

