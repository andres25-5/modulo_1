"""
Desarrolla un programa que permita al usuario gestionar una lista de compras. El
programa debe usar un bucle while para mostrar un menú con opciones:

1. Agregar ítem a la lista.
2. Eliminar ítem de la lista.
3. Ver la lista completa.
4. Salir. El programa debe gestionar la lista de compras y seguir las
instrucciones del usuario.
"""
print("=================================================")
print("Bienvenido al gestor de lista de compras")
print("=================================================")
opcion = 0  # Variable para controlar el bucle


def validar_opcion(opcion):
    """
    Esta funcion permite al usuario gestionar una lista de compras de manera interactiva,
    permitiendo agregar, eliminar y ver ítems en la lista. Utiliza un bucle while para
    mantener el menú activo hasta que el usuario decida salir.
    Args:
        opcion (int): Opción ingresada por el usuario.
        item (str): Ítem a agregar o eliminar de la lista.
        items (list): Lista para almacenar los ítems de la lista de compras.


    Returns:
        bool: True si la opción es válida (1-4), False en caso contrario.
        str: Mensaje de confirmación al agregar o eliminar un ítem.
        list: Lista de ítems actualizada.
        str: Mensaje de error si el ítem no se encuentra en la lista.
        str: Mensaje de salida si el usuario decide salir del programa.
    """
    return opcion in [1, 2, 3, 4]


items = []  # Lista para almacenar los ítems de la lista de compras
while True:
    print("Seleccione una opción:\n"
          "1. Agregar ítem a la lista\n"
          "2. Eliminar ítem de la lista\n"
          "3. Ver la lista completa\n"
          "4. Salir")
    opcion = int(input("Ingrese una opción (1-4): "))
    match opcion:
        case 1:
            print("========================================")
            item = input("Ingrese el ítem a agregar: ")
            print("========================================")
            items.append(item)
            print(f"Ítem '{item}' agregado a la lista.")
        case 2:
            print("========================================")
            item = input("Ingrese el ítem a eliinar: ")
            print("========================================")
            if item in items:
                items.remove(item)
                print(f"Ítem '{item}' eliminado de la lista.")
            else:
                print(f"Ítem '{item}' no encontrado en la lista.")
        case 3:
            if items:
                print("========================")
                print("Lista de compras:")
                print("========================")
                for i, item in enumerate(items, start=1):
                    print(f"{i}. {item}")
            else:
                print("La lista de compras está vacía.")
        case 4:
            respuesta = input("¿Está seguro de que desea salir? (si o no): ").lower()
            if respuesta == "si":
                print("Saliendo del programa. ¡Gracias por usar el gestor de lista de compras")
                break
            else:
                print("Volviendo al menú principal.")
        case _:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")
print("===================================================================")
print("Gracias por usar el gestor de lista de compras. ¡Hasta luego!")
print("===================================================================")





