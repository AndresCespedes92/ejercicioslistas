""" 6 ------- Eliminar todas las instancias
Nombre de la función:
eliminar_todos(lista, elemento)
Objetivo:
Eliminar todas las ocurrencias de un elemento en la lista.
Tarea:
Modificar la lista original, removiendo todos los elementos iguales al valor recibido.
No es necesario retornar un valor (solo modificar la lista).

Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].

"""

def eliminar_todos(lista: list[any], elemento: any) -> str | None:
    """
    Elimina todas las apariciones de un elemento en la lista original
    y devuelve un mensaje describiendo la operación. Si el elemento no está presente,
    retorna None.

    Args:
        lista (list[Any]): Lista original.
        elemento (Any): Elemento a eliminar.

    Returns:
        str | None: Mensaje describiendo el resultado, o None si no se encontró el elemento.
    """
    
    # Verificamos si el elemento está en la lista
    if elemento not in lista:
        return None
    
    nueva_lista = []

    for i in lista:
        if i != elemento:
            nueva_lista = nueva_lista + [i]
            lista[:] = nueva_lista

    return f"La lista queda {lista}. Se eliminaron todas las instancias de {elemento}"