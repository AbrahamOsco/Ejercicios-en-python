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
numerosUno.remove(4)
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




#Ejercicio 4)
"""" 
Tenemos 3 vectores de Edad, sexo e Indice. Sabemos ademas que su tamanio tiene un tope que es 100. (Tope = cantidad maxima de elementos de una lista o vector)

"""


Edades = []
Sexos = []
Indices = []

#cargamos los vectores de manera aleatoria:
import random
def cargamosDatosRandom():
    tamanioActual = 0
    while(tamanioActual < 100 ):
        unaEdad = random.randint(15,30)        #te escupe un entero entre:   15<= enteroRandom <= 30
        unIndice = random.uniform(3.8, 9.0)   #te escupe floats random:  3.0 <= floatRandom <= 10.0   
        unIndice = round(unIndice,2 )          #Truncamos el indice obtenido con  2 decimales, usamos round para lograrlo.    
        unSexo = random.choice( ["M", "F"])    #te escupe un string random "M" o "F"

        if( (unaEdad>=17 and unaEdad<=24 ) and ( unIndice>=3.80 and unIndice<=9)  ):         #en general en el if poner el caso "feliz" es mas sencillo
            Edades.append(unaEdad)
            Sexos.append(unSexo)
            Indices.append(unIndice)
            tamanioActual +=1


def calcularMedidaPorSexo(unSexo):
    indiceAcumulado = 0
    cantidadPersonasDelSexo = 0
    for i in range(0,100): #este for su intervalo es -> [0,100)
        if Sexos[i]== unSexo:
            indiceAcumulado +=Indices[i]
            cantidadPersonasDelSexo +=1

    media = indiceAcumulado/cantidadPersonasDelSexo
    print("La medida especifica por  el sexo", unSexo,"es: ", media  )


def eliminarMenorIndiceYMostrar():
    menorIndice = Indices[0]     #suponemos que el primer elemento de la lista es el de menor indice.
    #Encontramos el menor indice
    for i in range(0,100):
        if menorIndice > Indices[i]:
            menorIndice = Indices[i]
    
    posicionesAEliminar = []
    for i in range(0,100):
        if Indices[i] == menorIndice:
            print("Edad: ", Edades[i], "Indice: ", Indices[i], "Sexo: ", Sexos[i])
            posicionesAEliminar.append(i)
    for posicion in posicionesAEliminar:
        Indices.pop(posicion)
        Sexos.pop(posicion)
        Indices.pop(posicion)
    
    

def ordenadosPorIndiceMayorAMenor():
    #Agrupo tanto edad sexo e Indice a esa asociacion lo llamo unAlumno (como juntas galletas en un empaque de galletas asi ).
    matrixAlumnos = []
    for i in range(0, 100):
        unAlumno = []
        unAlumno.append( Sexos[i] )
        unAlumno.append( Edades[i] )
        unAlumno.append( Indices[i] )
        matrixAlumnos.append(unAlumno)
    #Ahora que tengo una lista con datos para cada alumno ordeno por indice. 
    ordenados = sorted(matrixAlumnos, key= lambda alumno: alumno[2] , reverse=True ) # ordena a los alumnos por indice. porque 2? -> 
    print(ordenados)                                                  # mira la posicion 2 le pertenece a indice ordenamos por ese criteri


cargamosDatosRandom()
ordenadosPorIndiceMayorAMenor()
#calcularMedidaPorSexo("F")
#eliminarMenorIndiceYMostrar()



