"""1 --- Agregar
Nombre de la función:
agregar(lista, elemento)
Objetivo:
Agregar un elemento al final de la lista.
Tarea:
Modificar la lista original, añadiendo elemento como su último elemento.
No es necesario retornar un valor (solo modificar la lista).
"""
from controlador import controlador_de_lista


def agregar(lista: list[any], elemento: any) -> list[any]:
    """Crea una nueva lista que contiene los elementos de la lista original y añade el nuevo elemento al final.

    Args:
        lista (List[Any]): Lista original a la que se desea agregar el elemento.
        elemento (Any): Elemento que se desea agregar al final de la lista.
    Returns:
        list[Any]: Una nueva lista con el elemento añadido al final.

    """
    controlador_de_lista(lista)
    lista_nueva = lista + [elemento]
    return lista_nueva

