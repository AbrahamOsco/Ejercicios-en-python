###
unaLista = [] # es una lista vacia. 
unaEdad= 20   # un numero entero.
unNombre = "Lara"  #un string una cadena de caracteres
unfloat = 3.1421   #un numero con decimales lo podemos llamar float

print("una lista recien creada: ", unaLista)

unaLista.append(unaEdad)
unaLista.append(unNombre)
unaLista.append(unfloat)

print("imprimo lista con dos elementos", unaLista)

print(unaLista[0])
print(unaLista[1])
print(unaLista[2])

print("Tamanio de una lista : ", len(unaLista)  )

# Existen dos maneras de recorrer una lista: 
# por indice: 

for i in range(len(unaLista)):  # [0,3) ->   0<= x < 3 i = 2
    print("i :", i, "valor:",unaLista[i] )


""" 
Cargar dos listas VEC1 y VEC2 de 20 posiciones cada una. Analizar s ei son iguales (se consideran iguales cuando
cada elemento de VEC1 es igual a cada elemento de VEC2). Imprimir “Las listas son iguales” o “Las listas no son iguales”,
de acuerdo al resultado. 
"""

VEC1 = []
VEC2 = []
for i in range(1): # 
    valorIngresadoParaVec1 = input("Ingrese un numero: para VEC1 ")
    valorIngresadoParaVec2 = input("Ingrese un numero: para VEC2 ")

    VEC1.append( int(valorIngresadoParaVec1) )
    VEC2.append( int(valorIngresadoParaVec2) )

print(VEC1)
print(VEC2)
#Comparamos cosas en informatica con ifs. 

sonVectoresIguales = "NoCambio"

for i in range(1):
    if VEC1[i] != VEC2[i]:
        sonVectoresIguales = "CambioValor"
        break

if sonVectoresIguales == "NoCambio":
    print("Listas son iguales")

if sonVectoresIguales == "CambioValor":
    print("Listas no son iguales")


#Ejercicio 4)
"""" 
Tenemos 3 vectores de Edad, sexo e Indice. Sabemos ademas que su tamanio tiene un tope que es 100.
"""
edades = []
sexos = []
indices = []

import random
contador = 0

for i in range(0,100):
    unaEdad = random.randint(17, 24) # -> 25 , 15 , 22 , 28
    unIndice = round( random.uniform(3.80, 9.0), 2  )  # ROUND sirve para truncar decimales con muchos digitos -> 
    unSexo = random.choice( ["M", "F"] ) 
    edades.append(unaEdad)
    sexos.append(unSexo)
    indices.append(unIndice)

#Queda pendiente para ustedes hacerlo con edad. 
def calcularMediaSegunSexo(sexoACalcularMedia):
    acumuladorIndice = 0
    cantidadVecesDeMatcheo = 0
    for i in range(100):
        if sexos[i] == sexoACalcularMedia:
            acumuladorIndice += indices[i]
            cantidadVecesDeMatcheo +=1

    media = acumuladorIndice/cantidadVecesDeMatcheo
    print( round(media,3))

calcularMediaSegunSexo("M")
calcularMediaSegunSexo("F")

def calcularYMostarAlumnosConMinimorIndice():
    menorValorIndice = indices[0]
    for i in range(100):
        if menorValorIndice > indices[i]:  #COmo comparas un element con todos los elementos del vector de indices con esto. el if.
            menorValorIndice = indices[i]

    for i in range(100):
        if indices[i] != menorValorIndice:
            print("Edad: ", edades[i], "Indice: ", indices[i], "Sexo: ", sexos[i])
    


def obtenerListadoDeAlumnosOrdenados():
    indices.sort(reverse=True) 
    print(indices)




obtenerListadoDeAlumnosOrdenados()
