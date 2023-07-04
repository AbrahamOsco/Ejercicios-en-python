#Ejercicio 1) 

# Asi creamos una lista. 
unaLista = []
print("Se imprime una lista vacia", unaLista)

#Agregamos elementos a la lista   a la lista

nombre = "Pepe" # nombre es un "String"

unaLista.append(nombre) #Asi se agrega un elemento a una lista con append

nombre2= "Pepa"
unaLista.append(nombre2);

print("Se imprime la lista con dos elemento", unaLista)
#Agregamos numeros:  
unaEdad = 100  #esto es un entero
unaEdadFlotante = 12.31  #Esto es un float. va con punto no con coma ! 

unaLista.append(unaEdad)
unaLista.append(unaEdadFlotante)

print("A la lista se le agrego dos numeros nuevos ", unaLista)

#Conclusion? -> Una lista puede tener numeros, strings, enteros, float y lo que se te ocurra. 
#Recomendacion: tener una lista y que todos esos elementos sean de un mismo tipo de dato (solo string o solo numeros o solo floats,etc)


#Ejercicio2) 
numerosUno = [-1,2,-3,4,-5,6,-7,8,-9]

#Quiero conocer el tamanio de la lista? como hago= -> Con len. 
tamanioLista = len(numerosUno) 
print("tamanio de la lista es: ", tamanioLista) #imprime 9

#Quiero obtener el -1 como hago ? -> Accedemos a un elemento con el operador corchetes [].
elementoSeleccionado = numerosUno[0] #en este caso el -1 esta en la posicion 0 

#Este for tiene nombre se llama for por indice. 
for i in range(0,len(numerosUno)): # en matematica este rango es equivalente a [0,9) 0 inclusive menor a 9 estricto. 
    print("Indice actual i = ", i ," valor Actual es:  numerosUno[", i , "]  = ", numerosUno[i] )



#Ordenamos la lista In-Place es decir en la misma lista Ordenamos de menor a mayor : 
numerosUno.sort() 
print("Lista ordeanada de menor a mayor : ",numerosUno)

#Ordenamos la lista In-Place es decir en la misma lista Ordenamos de mayor a menor : 
numerosUno.sort(reverse=True) 
print("Lista ordeanada de mayor a menor : ",numerosUno)

# Quiero sacar el 4 de la lista ? como hago ?  -> Con remove 
numerosUno.remove(4);
print("Lista sin el elemento 4: ",numerosUno)



#Ejercicio 3)
""" 
Una Institución de Educación Superior tiene sus 68 aulas de clase, distribuidas en tres edificios, identificados con las letras A, B y C.
En cada edificio hay un número diferentes de aulas, identificadas con un número, cada una con una capacidad distinta, medida en puestos,
y con un área diferente, medida en metros cuadrados. Esa información debe ser almacenada en arreglos unidimensionales (Vectores) paralelos, 
de tal forma que se puedan trabajar como se muestra, por ejemplo, en el esquema siguiente:
 """
listaEdificios = ["B","C", "A", "A", "B"]
listaNumeros =   [14,  7,   2,  24,   8 ]
listaPuestos =   [42, 65,  45,  64,   38]
listaAreas =  [52.50, 70.00, 30.25, 55.00, 42.25]

#Calcular la capacidad total, en puestos, de cada edificio. 

edificioAConocer = "A"
acumuladorCapacidad = 0
for i in range(0 , len(listaEdificios) ):
    if listaEdificios[i] == edificioAConocer:
        acumuladorCapacidad += listaPuestos[i]

print(" acumulador de capacidad Edificio A : ", acumuladorCapacidad)




