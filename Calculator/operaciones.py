def sumar(x:int,y:int) -> int:
    """
    Brief:Calcula la suma entre dos numeros.

    Args:
        x (int): Primer operando 
        y (int): Segundo operando

    Returns:
        int: Retorna el resultado de la suma.
    """
    return x + y

def restar(x:int,y:int) -> int:
    """
    Brief:Calcula la resta entre dos numeros.

    Args:
        x (int): Primer operando 
        y (int): Segundo operando

    Returns:
        int: Retorna el resultado de la resta.
    """
    return x - y

def multiplicar(x:int,y:int) -> int:
    """
    Brief:Calcula la multiplicacion entre dos numeros.

    Args:
        x (int): Primer operando 
        y (int): Segundo operando
    
    Returns:
        int: Retorna el resultado de la multiplicacion.
    """
    return x * y

def dividir(x:int,y:int) -> float:
    """
    Brief:Calcula la division entre dos numeros.

    Args:
    x (int): Primer operando 
    y (int): Segundo operando
    
    Returns:
        float: Retorna el resultado de la divison.
    """
    try:
        resultado = x / y
    except ZeroDivisionError:
        return "Error, no es posible dividir por cero"
    else:
        return resultado

def factorial(x:int) -> int:
    """
    Brief:Calcula el factorial de un numero.

    Args:
        x (int): Operando

    Returns:
        int: Retorna el factorial de un numero.
    """
    fact = None
    
    if x < 0:
        return "Error no se puede calcular el factorial de numeros negativos."
    elif x == 0 or x == 1:
        fact = 1
    else:
        fact = x * factorial(x - 1)
    
    return fact



