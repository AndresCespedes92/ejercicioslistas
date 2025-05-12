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