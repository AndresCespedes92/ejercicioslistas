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