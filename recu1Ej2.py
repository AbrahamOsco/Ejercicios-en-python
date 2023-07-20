#Llenamos las listas 

"""  <- borrar esto si queres descomentar el codigo de arriba 

# 4 listas vacias
nombresCaballos = []
pesosCaballos = []
procedencias = []
cantTriunfos = []

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

borrar los 3 comillas dobles tambien para descomentar el codigo.
"""


nombresCaballos = ["pepe", "pepa", "pepo", "Lolo", "Lola"]
procedencias = ["Nacional", "Nacional", "Extranjero", "Extranjero", "Nacional"]
pesosCaballos = [30.0, 120.0, 90.0, 30.0, 400.0]
cantTriunfos = [1, 2, 4, 4, 10]
cantCaballos = 5

#decreciente
def imprimirRegistroCaballo():
    #Posiciones es una lista creada para obtener las posiciones de como quedo ordenado la copia de los pesosDeCaballos
    posiciones = list(range(0,cantCaballos)) # se crea una lista de numeros de 0 a cantCaballos -> [0,cantCaballos) ojo no olvidar poner list al inicio como esta
    copyPesosCablls = pesosCaballos.copy()  #no quiero cambiar la lista de pesosCaballos por eso "copio" la lista con copy. 
    
    # ordenamos la lista por peso decreciente 
    for i in range(0,cantCaballos):
        for j in range(i+1, cantCaballos):
            if copyPesosCablls[i] < copyPesosCablls[j]: #aca se hace un swap lo que esta en copyPes[i] debe pasar a copyPes[j]
                aux = copyPesosCablls[i]
                copyPesosCablls[i] = copyPesosCablls[j]
                copyPesosCablls[j] = aux

                #Muevo las posiciones como se esta moviendo en la lista de copyPesosCablls
                aux = posiciones[i]
                posiciones[i] = posiciones[j]
                posiciones[j] = aux
    
    print("NOMBRE DEL CABALLO\t\t PROCEDENCIA\t\t PESO\n")
    for i in range(cantCaballos): #Este es un for por elemento.
        print(f"{nombresCaballos[posiciones[i]]}\t\t\t\t {procedencias[posiciones[i]]}\t\t {pesosCaballos[ posiciones[i] ]}\n" )
    

imprimirRegistroCaballo()
                

