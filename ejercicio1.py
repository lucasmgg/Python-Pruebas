#ejercicio 1


#Ingreso de variables:
nom_padre = input("¿Nombre del padre?")
nom_madre = input("¿Nombre del madre?")
nom_bebe = input("¿Nombre del bebe?")

#Posición del espacio
ind_padre = nom_padre.index(" ")
ind_madre = nom_madre.index(" ")


#Variable
apellido_P = nom_padre[ind_padre:]
print("Hola mundo")

#mostrar en pantalla:
mensaje= (f"nombre del recien nacido es ")
print (nom_padre)