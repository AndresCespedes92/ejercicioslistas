# Instancia de control de datos ingresados
def controlador_de_lista (lista : any) -> bool:
    """
    Verifica si el parámetro ingresado es una lista.

    Args:
        lista (any): Objeto a evaluar.

    Returns:
        bool: Retorna True si el objeto es una lista, de lo contrario retorna False.
    """
    if type(lista) == list:
        return True
    else:
        return False