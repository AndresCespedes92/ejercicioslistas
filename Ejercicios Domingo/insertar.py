""" 2 -----Insertar
Nombre de la función:
insertar(lista, elemento, indice)
Objetivo:
Insertar un elemento en una posición específica de la lista.
Tarea:
Modificar la lista original, colocando elemento en la posición indicada por indice.
Si el índice es mayor al tamaño de la lista, el elemento se agrega al final.
Ejemplo: Si la lista es [10, 20, 30] y se inserta 5 en el índice 1, la lista resultante será [10, 5, 20, 30]."""

def insertar(lista: list[any], elemento: any, indice: int) -> list[any]:
    """
    Crea una nueva lista que contiene los elementos de la lista original y añade el nuevo elemento en la posición indicada.
    Si la posición es mayor que la longitud de la lista, el elemento se añade al final.
    Si la posición ya está ocupada, se reemplaza el valor existente.

    Args:
        lista (list[any]): Lista original sobre la que se quiere insertar o reemplazar un elemento.
        elemento (any): Elemento que se desea insertar.
        indice (int): Posición (1-based) en la que se desea insertar o reemplazar el elemento.

    Returns:
        list[any]: Una nueva lista con el elemento añadido o reemplazado según corresponda.
    """
    indice = int(input("ingrese la posicion: "))
    indice = indice - 1
    if indice > len(lista):
        lista_nueva = lista + [elemento]
    
    else:
        lista[indice] = elemento
        lista_nueva = lista
    
    return lista_nueva