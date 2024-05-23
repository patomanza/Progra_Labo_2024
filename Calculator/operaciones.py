def sumar(x:int,y:int) -> int:
    """Calcula la suma de dos numeros.

    Args:
        x (int): Primer operando 
        y (int): Segundo operando

    Returns:
        int: Retorna el resultado de la suma
    """
    return x + y

def restar(x:int,y:int) -> int:
    """_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    """
    return x - y

def multiplicar(x:int,y:int) -> int:
    """_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    """
    return x * y

def dividir(x:int,y:int) -> float:
    """_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        float: _description_
    """
    try:
        resultado = x / y
    except ZeroDivisionError:
        return "Error, no es posible dividir por cero"
    else:
        return resultado

def factorial(x:int) -> int:
    """_summary_

    Args:
        x (int): _description_

    Returns:
        int: _description_
    """
    fact = None
    
    if x < 0:
        return "Error no se puede calcular el factorial de numeros negativos."
    elif x == 0 or x == 1:
        fact = 1
    else:
        fact = x * factorial(x - 1)
    
    return fact



