""" 
Describe y ejemplifique 3 buenas practicas de programacion estructurada y modular. Citar fuentes. 

1. Nombre de las funciones que incluyan almenos un verbo que describe la tarea. 
Por ejemplo: Si estamos creando un juego y el persanje debe recibir daño la funcion se deberia nombrar algo como:
    def takeDamage(aCharacter, aDamage):
        ...
    Fuente clase2. 

2.Nombres de las variables deben ser representativos, es decir deben tener sentido.  
Por ejemplo: Si tenemos una lista con los nombres de los estudiantes y otra con las notas seria un posible nombre seria:
    nombresEstudiantes = ["carlos", "juan", "maria", ...]
    notasEstudiantes = [2, 1, 4, ...]

    Fuente clase1

3.Cada funcion debe realizar una actividad: Al separar operaciones en pequeños funcions se podria reutilizar el codigo muchas veces. 
Por ejemplo: Tenemos una funcion que elimina los elementos repetidos de una lista de enteros y que tambien halla el maximo y el min y lo devuelve: 
    def eliminarRepetidosYObtenerMaxYMin(unaLista):
        listaSinRepetidos = []
        for elemento in unaLista:
            if (elemento not in listaSinRepetidos):
                listaSinRepetidos.append(elemento)

        if len(listaSinRepetidos) > 0:
            maximo = minimo = listaSinRepetidos[0]
            for elemento in listaSinRepetidos:
                if elemento > maximo:
                    maximo = elemento
                elif elemento < minimo:
                    minimo = elemento
        else:
            maximo = minimo = None  
        return listaSinRepetidos, maximo, minimo       

Esta haciendo demasiadas cosas esta funcion, en este caso lo mejor es "dividirla" en 3 funciones pequeñas:
def getListSinRepetidos(unaLista), def getMax(unaLista), def getMin(unaLista).
y que podrian ser reutilizadas en otros archivos del codigo. 
"""

import random

# Sistema de control de stocks 

#Retorna true si se agrego con exito el nuevoProducto, sino retorna false
def agregarNuevoProducto(productos = [], nuevoProducto = []):
    if len(productos) == 0 :
        productos.append(nuevoProducto)
    elif len(productos) > 0:
        productosConCodRepetido = list(filter(lambda unProducto: unProducto[0] == nuevoProducto[0], productos) )
        if(len(productosConCodRepetido) == 0):
            productos.append(nuevoProducto)
            return True
        else: 
            print(f"Error No se pudo agregar el producto, El codigo de producto: {nuevoProducto[1]} ya existe: ")
            return False

def printProducto(unProducto):
    print(f"{unProducto[0]}\t\t\t\t {unProducto[1]}\t\t\t\t {unProducto[2]}", end="\t\t\n")


def printRegistroCompletoProductos(productos = []):
    productosPorCodProd = sorted(productos, key=lambda unProducto: unProducto[0]) # del mas chico al mas grande
    print("Codigo de producto\t\t\t Nombre\t\t\t StockActual")
    list(map(lambda unProducto: printProducto(unProducto), productosPorCodProd))  # Funcion map no ejecuta la funcion prinProducto por si sola necesitamos ponerle list() para q la ejecute 


def printProductosDebajoDelStockMin(productos = []):
    productoStockMin = list(filter(lambda unProducto: unProducto[2] < 5, productos))
    if( len(productoStockMin) > 0 ):
        print("Codigos de los productos que esta debajo del stock minimo (5): \n")
        list(map(lambda unProducto: print(f" {unProducto[0]}\n "), productoStockMin))
    else: 
        print("No hay ningun producto cuyo stock este por debajo del minimo (5) \n")

        
def printProductosMayorCantEnStock(productos = []):
    stocks =  list(map(lambda unProducto: unProducto[2], productos)) #  de todos los productos nos quedamos con todos los stocks.
    maxStock = sorted(stocks, reverse=True)[0] # ordenamos del mas grande al mas chico y obtenemos el primer valor (el maximo). 
    print(f"La mayor cantidad en stock es {maxStock}\n")
    productosConStockMax = list(filter(lambda unProducto: unProducto[2] == maxStock, productos ))
    print("Codigo de productos que tienen el stock Maximo: \n")
    list(map(lambda unProducto: print(f"{unProducto[0]}\n "), productosConStockMax))


def ingresoCodProducto():
    seIngresoConExito = False
    codProducto = 0
    while( not seIngresoConExito ):
        codProducto = int (input("Ingrese el codigo del producto: "))
        if(codProducto < 1000 or codProducto > 9999):
            print("Error el codigo de producto debe ser entre 1000 y 9999 inclusives")
        else: 
            seIngresoConExito = True
    return codProducto

def ingresoProductos():
    cantMaxProductos = 2  # Es el valor N de la consigna.
    i = 0       #Se asignan a variables como: i,j,k, para iterar listas, matrices,etc 
    productos = [] 
    # productos sera una matriz (lista de lista) y cada elemento de esta "lista" "productos" sera otra lista con el codigoProducto, nombre, stock)
    # seria algo asi:  ej: productos = [ [1002, "AlfajorOreo", 15], [3015, "Doritos", 5], ... ];

    while( i < cantMaxProductos):
        modelo = input("Ingrese el nombre del modelo : ")
        codProducto = ingresoCodProducto()
        numberStock = random.randint(0,100)  # Random de [0,100] incluye limites.
        unProducto = [codProducto, modelo, numberStock]

        if( agregarNuevoProducto(productos, unProducto)):
            i +=1

    printRegistroCompletoProductos(productos)
    printProductosDebajoDelStockMin(productos)
    printProductosMayorCantEnStock(productos)


def main():
    ingresoProductos()

main()