"""
Crea un programa que simule las operaciones de un cajero automático. El
programa debe gestionar un saldo inicial.

• Debe encapsular la lógica en funciones como consultar_saldo(),
depositar(), retirar().
• Utiliza un bucle while para mantener el programa en ejecución hasta que el
usuario decida salir.
• Valida las operaciones (ej. no se puede retirar más dinero del que hay en el
saldo).
• El código debe ser claro, legible y seguir las recomendaciones de PEP 8.
• Conceptos integrados: Funciones, bucle while, condicionales, variables,
operadores, I/O, PEP 8.
"""
opcion = 0
saldo = 0.0


def depositar():
    """
    Esta funcion permite al usuario depositar dinero en su cuenta
    actualizando el saldo disponible.

    Args:
        monto (float): Monto a depositar en la cuenta.

    Returns:
        str: Mensaje de confirmación del depósito y el nuevo saldo.
        str: Mensaje de error si el monto es menor o igual a cero.
    """
    global saldo  # Declaramos que usaremos la variable global 'saldo'
    print("---------------------")
    monto = float(input("Ingrese el monto a depositar: $ "))

    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    else:
        print("El monto debe ser mayor que cero.")


def consultar_saldo():
    """
    Esta funcion permite al usuario consultar su saldo actual
    mostrando el monto disponible en su cuenta.
    Args:
        saldo (float): Monto disponible en la cuenta.

    Returns:
        str: Mensaje que muestra el saldo actual.
    """
    global saldo
    print("-----------------------------------------")
    print("|\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t|")
    print(f"|\tSu saldo actual es $ {saldo:.2f}\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t|")
    print("-----------------------------------------")


def retirar():
    """
    Esta funcion permite al usuario retirar dinero de su cuenta
    actualizando el saldo disponible si hay fondos suficientes.

    Args:
        saldo (float): Monto disponible en la cuenta.
        saldo_retiro (float): Monto a retirar de la cuenta.

    Returns:
        str: Mensaje de confirmación del retiro y el nuevo saldo.
        str: Mensaje de error si el monto es mayor al saldo disponible o menor o igual a cero.
    """
    global saldo
    print("---------------------")
    saldo_retiro = float(input("Ingrese el monto a retirar: $ "))

    if saldo_retiro > 0:
        if saldo_retiro <= saldo:
            saldo -= saldo_retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("Fondos insuficientes.")
    else:
        print("El monto debe ser mayor que cero.")


print("-------------------------------")
print("Bienvenido al cajero :)")
print("-------------------------------")
while True:

    print("1. Depositar\n"
          "2. Consultar Saldo\n"
          "3. Retirar\n"
          "4. Salir")

    opcion = int(input("Ingrese la opcion: "))

    match opcion:
        case 1:
            depositar()
        case 2:
            consultar_saldo()
        case 3:
            retirar()
        case 4:
            respuesta = input("Esta seguro que desea salir (si o no): ").lower()
            if respuesta == "si":
                print("Saliendo...")
                break
            else:
                print("Volviendo al menu Principal")
        case _:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")
print("===================================================================")
print("Gracias por utilizar el cajero. ¡Hasta luego! :)")
print("===================================================================")

