"""
1.elegir operando
2. elegir segundo operando (no puedo entrar sin entrar al 1)
3. elegir operacio (no puedo enrar sin entrar a 1 y 2)
4. mostrar resultado (no puedo entrar sin ninguno de los anteriores)
5. salir"""

import operaciones as op

def ingresar_operando(mensaje) -> int:
    """_summary_

    Args:
        mensaje (_type_): _description_

    Returns:
        int: _description_
    """
    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            print("Error, ha ingresado letras. Ingrese solo numeros.")
        else:
            try:
                x = int(entrada)
                return x
            except ValueError:
                print("Por favor, ingrese un número válido: ")

menu = ["\n---------------------------Caclculadora---------------------------------\n",
        "1.Ingresar 1er operando: (A=x) ","2.Ingresar 2do operando: (B=y)","3.Elegir operacion: ","4.Mostrar resultado: ","5.Salir\n"]

def mostrar_menu(a,b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_
    """
    valor_a = str(a) if a is not None else "x"
    valor_b = str(b) if b is not None else "y"
    for opcion in menu:
        print(opcion.replace("x", valor_a).replace("y", valor_b))

def calcular_operaciones(a,b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    resultados = {
        'suma': op.sumar(a,b),
        'resta': op.restar(a,b),
        'multiplicacion': op.multiplicar(a,b),
        'division': op.dividir(a,b),
        'factorial_a': op.factorial(a),
        'factorial_b': op.factorial(b)
    }
    
    return resultados

def mostrar_resultados(resultados):
    """_summary_

    Args:
        resultados (_type_): _description_
    """
    results = [f"El resultado de A+B es: {resultados['suma']}",
                f"El resultado de A-B es: {resultados['resta']}",
                f"El resultado de A*B es: {resultados['multiplicacion']}",
                f"El resultado de A/B es: {resultados['division']}",
                f"El resultado de factorial de A es: {resultados['factorial_a']}",
                f"El resultado de factorial de B es: {resultados['factorial_b']}"]
    
    for resultado in results:
        print(f"{resultado}")

seguir = True
a = None
b = None
resultados = {}

while seguir == True:
    mostrar_menu(a,b)
    
    respuesta = ingresar_operando("Ingrese una opcion: ")
    if respuesta < 0 or respuesta > 5:
        print("Error, ingrese una opcion valida: ")
    
    match respuesta:
        case 1: 
            if a is None:
                a = ingresar_operando("\nIngresar 1er operando: ")
            else:
                print(f"\nYa ha ingresado el primer operando: {a}")
        case 2:
            if b is None:
                b = ingresar_operando("\nIngresar 2do operando: ")
            else:
                print(f"\nYa ha ingresado el segundo operando: {b}")
        case 3:
            if a is None or b is None:
                print("\nError, debe ingresar los operandos: ")
            else:
                resultados = calcular_operaciones(a,b)
                print("\nOperaciones calculadas.\n")
        case 4:
            if not resultados:
                print("\nError, primero debe calcular las operaciones.")
            else:
                print("\n")
                mostrar_resultados(resultados)
        case 5:
            break


