# [123k , 200k ,500k, 232k] ... k = 1000 ;   250 000 -> 250k 
# ["FIJO", "CONTRATADO", "FIJO", "FIJO", "CONTRATADO"... ] 45

sueldos = []
tiposSueldos= [] 

import random  # porque ? -> porque me piden cosas random en el parcial.
#45 veces. 
#Cargado de forma random tu lista de sueldos y tiposSueldos. 
for i in range(45):
    unSueldo = round(random.uniform(100000.0 ,700000.0), 1) 
    unTipo = random.choice( ["FIJO", "CONTRATADO"] )
    sueldos.append(unSueldo)
    tiposSueldos.append(unTipo)


sueldosNuevos = [] # Equivale a nuevos sueldos (palabras de la consigna)

for i in range(45):
    if sueldos[i] < 350000.0 and tiposSueldos[i] == "FIJO":
        sueldosNuevos.append( round(sueldos[i] + sueldos[i]*0.12, 1) )   #el aumento de 12%.
    elif sueldos[i] >= 350000.0 and sueldos[i] <= 676000.0 and tiposSueldos[i] == "CONTRATADO":
        sueldosNuevos.append( round(sueldos[i] + sueldos[i]*0.07, 1) ) 
    else:
        sueldosNuevos.append(sueldos[i])       

def printearRegistro():
    print("Empleado Nro    SueldoAnterior        NuevoSueldo")
    for i in range(45):
        print( str(i) + "     \t\t"  + str(sueldos[i]) + "\t\t"  + str(sueldosNuevos[i])  )


def informarHistorial(posicion):
    if( posicion <= 0 or posicion >=46 ):
        print("Che me pasaste una posicion invalida")
        return
    print("Empleado nro:\t" + str(posicion) )
    print("Sueldo anterior:\t " + str(sueldos[posicion-1]) )
    print("Nuevo sueldo:\t" + str(sueldosNuevos[posicion-1]))
    print("Incremento :\t" + str( round(sueldosNuevos[posicion-1] - sueldos[posicion-1] , 1 ) ) + "\n" )

for i in range(1,46): #// [1,46)
    informarHistorial(i)


def informeIncrementoMaximo():
    incrementos = []
    #Lleno la lista de incrementos. 
    for i in range(45):
        incrementos.append( round(sueldosNuevos[i] - sueldos[i], 1)   )
    
    #saco maximo de la lista de incrementos
    unMaximo = incrementos[0]
    for i in range(45):
        if unMaximo < incrementos[i]:
            unMaximo = incrementos[i]
    
    posicionesIncrementoMax = []
    # hacemos otro for para obtener las posiciones que coinciden con el maximo.
    for i in range(45):
        if incrementos[i] == unMaximo:
            posicionesIncrementoMax.append(i)
    
    return posicionesIncrementoMax


incrementosMaximosPos = informeIncrementoMaximo()
print(incrementosMaximosPos)


