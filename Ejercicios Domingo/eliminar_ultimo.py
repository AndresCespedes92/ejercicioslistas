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
    lista[:] = nueva_lista

    return f"La lista queda {lista}. Se elimino {eliminado}"