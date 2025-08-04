"""
Crea un programa que simule una agenda de contactos. Utiliza un diccionario
donde las claves sean los nombres de los contactos y los valores sean sus
números de teléfono. Implementa funciones para:
1. Añadir un nuevo contacto.
2. Buscar el teléfono de un contacto por su nombre.
3. Mostrar todos los contactos.

• Conceptos aplicados: Diccionarios, funciones, input(), bucle for para
iterar sobre diccionarios.
"""
print("=================================================")
print("Bienvenido a la agenda de contactos")
print("=================================================")
opcion = 0  # Variable para controlar el bucle


def validar(opcion):
    """
    Esta funcion permite al usuario gestionar una agenda de contactos
    permitiendo agregar, buscar, mostrar, salir. Utlizando un diccionario
    para almacenar todos los contacos y un bucle while para mantener el menu activo
    hasta que el usuario desee salir.

    Args:
        opcion (int): Opción ingresada por el usuario.
        clave (str): Nombre a agregar o buscar el contacto.
        valor (str): Numero a agregar el contacto.
        combinado (dic): guarda los nombres y numeros de contacto.
        buscar (str): Nombre que desea buscar el contacto.

    Returns:
        bool: True si la opción es válida (1-4), False en caso contrario.
        str: Mensaje de confirmación al agregar o buscar un contacto.
        dic: guarda los nombres y numeros de contacto
        str: Mensaje de error si no encuentra el contacto.
        str: Mensaje de error si el contacto no se encuentra en la lista.
        str: Mensaje de salida si el usuario decide salir del programa.
    """


combinado = {}

while True:
    print("Seleccione una opcion:\n"
          "1. Agregar contacto\n"
          "2. Buscar contacto\n"
          "3. Mostrar contactos\n"
          "4. Salir")
    opcion = int(input("Ingrese una opcion (1-4): "))
    match opcion:
        case 1:
            print("========================================")
            clave = input("Ingrese el nombre del contacto: ")
            print("========================================")

            print("=========================================")
            valor = input("Ingrese el numero de contacto: ")
            print("=========================================")

            combinado[clave] = valor
            for clave, valor in combinado.items():
                print(f"Nombre: {clave}, contacto: {valor}")

            print(f"Contacto '{clave}' fue agregado a la agenda.")
        case 2:
            print("===================================================")
            buscar = input("Ingrese el nombre  del contacto a buscar: ")
            print("===================================================")
            if buscar in combinado:
                print(f" contacto {buscar} su numero de telefono es: {combinado[buscar]}")
            else:
                print(" Contacto no encontrado.")
        case 3:
            if combinado:
                print("========================")
                print("Lista de contactos:")
                for i, combinado in enumerate(combinado, start=1):
                    print(f"El contacto {i} es:{combinado}")
                    print("====================================")
            else:
                print("La lista de contactos esta vacia")
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
print("Gracias por agendar el/los contacto/os. ¡Hasta luego!")
print("===================================================================")
