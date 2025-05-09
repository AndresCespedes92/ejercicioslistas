"""1 --- Agregar
Nombre de la función:
agregar(lista, elemento)
Objetivo:
Agregar un elemento al final de la lista.
Tarea:
Modificar la lista original, añadiendo elemento como su último elemento.
No es necesario retornar un valor (solo modificar la lista).
"""

def agregar(lista: list[any], elemento: any) -> list[any]:
    """Crea una nueva lista que contiene los elementos de la lista original y añade el nuevo elemento al final.

    Args:
        lista (List[Any]): Lista original a la que se desea agregar el elemento.
        elemento (Any): Elemento que se desea agregar al final de la lista.
    Returns:
        list[Any]: Una nueva lista con el elemento añadido al final.

    """
    lista_nueva = lista + [elemento]
    return lista_nueva


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


""" 3 ----- Obtener indice
Nombre de la función:
obtener_indice(lista, elemento)
Objetivo:
Encontrar el índice de la primera ocurrencia de un elemento en la lista.
Tarea:
Buscar en la lista el elemento recibido y retornar su posición (índice).
Si el elemento no existe en la lista, retornar -1."""

def obtener_indice(lista: list[any], elemento: any) -> int:
    """
    Busca un elemento en la lista y devuelve su posición si se encuentra o sino -1.

    Args:
        lista (list[any]): Lista en la que se busca el elemento.
        elemento (any): Elemento cuyo índice se desea encontrar.

    Returns:
        int: La posición del elemento en la lista (comenzando en 1).
             Devuelve -1 si el elemento no se encuentra.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return f"Su posicion es {i + 1}"
    return -1


""" 4 ----- Eliminar el último elemento
Nombre de la función:
eliminar(lista)
Objetivo:
Eliminar el último elemento de la lista y retornarlo.
Tarea:
Modificar la lista original, removiendo su último elemento.
Retornar el elemento eliminado.
Ejemplo: Si la lista es ["a", "b", "c"], al llamar a eliminar(), se retorna "c" y la lista queda ["a", "b"]."""

def eliminar(lista: list[any]) -> str:
    """
    Elimina el último elemento de la lista y devuelve un mensaje con el estado original,
    el nuevo estado de la lista y el elemento eliminado.

    Args:
        lista (list[Any]): Lista original de la que se eliminará el último elemento.

    Returns:
        str: Mensaje que describe la lista original, la lista resultante y el elemento eliminado.
    """
    eliminado = lista[-1]
    nueva_lista = lista[:-1]

    return f"La lista original {lista} queda {nueva_lista}. Se elimino {eliminado}"


""" 5 -------- Eliminar primera instancia
Nombre de la función:
eliminar_primer_instancia(lista, elemento)
Objetivo:
Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.
Tarea:
Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.
Si el elemento no existe, retornar None y dejar la lista sin cambios.
Ejemplo: Si la lista es [5, 3, 5, 7] y se elimina 5, la lista queda [3, 5, 7] y se retorna 5.
"""

def eliminar_primer_instancia(lista: list[any], elemento: any) -> str:
    """
    Elimina la primera aparición de un elemento en la lista y devuelve
    un mensaje con la lista original, la modificada y el elemento eliminado.

    Args:
        lista (list[any]): Lista original.
        elemento (any): Elemento a eliminar.

    Returns:
        str: Descripción del resultado de la operación.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            eliminado = lista[i]
            nueva_lista = lista[:i] + lista[i+1:]
            return f"La lista original {lista} queda {nueva_lista}. Se elimino {eliminado}"
    return None


