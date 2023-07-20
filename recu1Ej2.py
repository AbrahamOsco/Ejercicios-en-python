# 4 listas vacias
nombresCaballos = []
pesosCaballos = []
procedencias = []
cantTriunfos = []

#Llenamos las listas 

#Cargar informacion en listas. 
cantCaballos = int( input("Ingrese la cantidad de caballos a informar: ")) # "1" -> 1 (Casteo)

for i in range(cantCaballos):
    unNombre = input("Ingrese un nombre de un caballo: ")
    unPeso = float( input("Ingrese un peso en (KG) : ")) #idem
    unaProcedencia = input("Ingrese una procedencia (Nacional/Extranjero) :")
    unaCantTriunfo = int(input("Ingrese una cantida de triunfos: ")) #Ojo pasarlo a int porque si sacas max aca te explota todo. 
    nombresCaballos.append( unNombre)
    pesosCaballos.append( unPeso)
    procedencias.append( unaProcedencia)
    cantTriunfos.append( unaCantTriunfo)
    print("\n")        

#es que podes  
print(f"un Peso: {pesosCaballos[0]} y una procedencia: {procedencias[0]}") #Habilita que cambie las variables que estan en llaves por su valor.
print(nombresCaballos)
print(pesosCaballos)
print(cantTriunfos)    

# max triunfo de un caballo tipo nacional y luego el max de triunfo de un caballo de tipo extranjero. 
# Tomamos el primer maximo. 

# Hacemos las funciones para hacer cosas genericas
def mejorCaballoSegunTipo(tipoProcedencia): 
    maxTriunfo = 0 
    posMax = 0

    for i in range(cantCaballos):
        if ( maxTriunfo < cantTriunfos[i] and procedencias[i] == tipoProcedencia ): #Saco el max de triunfo que ademas matchee con el tipoProcedencia que me estan pasando
            maxTriunfo = cantTriunfos[i]
            posMax = i

    return nombresCaballos[posMax]

nombreMejorCabalNac =  mejorCaballoSegunTipo("Nacional")
nombreMejorCaballoExtr =  mejorCaballoSegunTipo("Extranjero")

print(f"El nombre del mejor caballo nacional es:  {nombreMejorCabalNac} El nombre del caballo Extranjero {nombreMejorCaballoExtr} ")


def imprimirRegistroCaballo():
    print("NOMBRE DEL CABALLO\t\t Procedencia\t\t Peso\t\n")
    # No sort, No diccionario, No Matrices, No Clases , se puede pero es mas jodido


