""" 7 -------- vaciar_lista(lista)
Nombre de la función:
[
Objetivo:
Eliminar todos los elementos de la lista, dejándola vacía.
Tarea:
Modificar la lista original, removiendo todos sus elementos.
No es necesario retornar un valor (solo modificar la lista).
Ejemplo: Si la lista es [1, 2, 3], al llamar a vaciar_lista(), la lista quedará [].
"""

def vaciar_lista(lista: list[any]) -> None:
    """
    Elimina todos los elementos de la lista, dejándola vacía.

    Args:
        lista (list[Any]): Lista original a vaciar.

    Returns:
        None
    """
    lista[:] = []