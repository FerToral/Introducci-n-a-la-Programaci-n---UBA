#Las Tuplas son listas inmutables

#Conversion de Tupla a Lista
#miTupla=("Fer", 25, 2, 2001)

#miLista=list(miTupla)

#print(miLista)

#Conversion de Lista a Tupla

miLista=["Fer", 25, 2, 2001,2]

miTupla=tuple(miLista)

print(miTupla)
print("Fer" in miTupla)
print(miTupla.count(2)) #Cuenta las veces que esta ese elemento en la Tupla
print(len(miTupla))# Cuantos elementos hay en miTupla

miTupla2= ("Fer",)# Tupla Unitaria
print(len(miTupla2) )

# Empaquetado de Tupla
miTupla3= "Fer", 25, 2, 2001
print(miTupla3)

# Desempaquetado de Tuplas
miTupla4= ("Fer", 25, 2, 2001)
nombre, dia, mes, año=miTupla4 
print(nombre,dia,mes,año)
print(miTupla4.index(25))

#Prueba de demostracion de diferentre entre Tupla Uni. y Texto(STR)
miTupla=("Elemento",)
print(miTupla)
print(type(miTupla))
otraTupla=("Elemento")
print(otraTupla)
print(type(otraTupla))
