"""
Diseña un sistema para gestionar el inventario de una tienda. El inventario se
almacenará en una lista de diccionarios. Cada diccionario representará un
producto con "nombre", "precio" y "cantidad". El programa debe:

• Usar funciones para cada operación: agregar_producto(), realizar_venta(),
mostrar_inventario().
• La función realizar_venta debe actualizar la cantidad del producto vendido.
• El código debe estar bien documentado con docstrings y seguir la
nomenclatura de PEP 8.
• Mostrar un menú interactivo para el usuario.
• Conceptos integrados: Listas, diccionarios, funciones, bucles,
condicionales, I/O, docstrings, PEP 8.
"""
print("=================================================")
print("Bienvenido al gestor de compras")
print("=================================================")
opcion = 0

producto = {}

def sistema(opcion):
    """
    Esta funcion permite al ususario gestionar un modulo de inventario
    permitiendo agregar, realizar venta, mostrar inventario. Utlizando un diccionario
    para almacenar los productos y un bucle while para mantener el menu acctivo hasta que el
    usuario desee salir

    Args:
        opcion (int): opccion ingresada por el ususario
        agregar_producto (fun): Funcion que agrega el producto
        realizar_venta (fun): Funcion que hace la venta el producto
        mostrar_inventario (fun): Funcion que muestra el producto con sus atrivutos

    Returns:
        bool: True si la opción es válida (1-4), False en caso contrario.
        str: Mensaje de salida si el usuario decide salir del programa.
    """
def agregar_producto():
    """
    Esta funcion permite al usuario crear o agregar un producto,
    con un stock con su respectiva informacion guardandolo en un diccionario


    Args:
        id (str): Codigo a agregar el producto.
        nombre (str): Nombre a agregar del producto.
        precio (float): Valor a agregar el producto.
        cantidad (int): Cantidad a agregar el producto.
        Producto (dic): guarda los productos en el inventario.

    Returns:
        str: Mensaje de confirmacion al agregar el producto
    """
    print("========================================")
    id = input("Ingrese el código del producto a agregar: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    print("========================================")

    # Guardar los datos como un diccionario dentro del diccionario
    producto[id] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

    print(f"Producto: {nombre} agregado correctamente.\n")

def realizar_venta():
    """
        Esta funcion permite al usuario registrar una venta de un producto,
        actualizando su stock y  guardando la informacion en un diccionario


        Args:
            id (str): Codigo a vender del producto.
            cantidad_vendida (int): Cantidad a vender el producto.
            precio_total (int): operacion para sacar el valor de la venta del producto

        Returns:
            str: Mensaje de confirmacion de la venta
            str: Mensaje de informacion sobre el valor de la venta
            str: Mensaje de informacion sobre el stock actual despues de la venta
            str: Mensaje de alerta sobre falta de stock
            str: Mensaje de alerta de que no encontro el producto
        """
    print("=====================================")
    id = input("Ingrese el código del producto a vender: ")
    cantidad_vendida = int(input("Ingrese la cantidad del producto que desea llevar: "))
    precio_total = cantidad_vendida*producto[id]['precio']
    if id in producto:
        if producto[id]["cantidad"] >= cantidad_vendida:
            producto[id]["cantidad"] -= cantidad_vendida
            print(f"Venta realizada de {cantidad_vendida} unidad(es) de {producto[id]['nombre']}.")
            print(f"Precio total: {precio_total}")
            print(f"Stock restante: {producto[id]['cantidad']}")
        else:
            print("No hay suficiente stock disponible.")
    else:
        print("Producto no encontrado.")

def mostrar_inventario():
    """
    Esta funcion permite al usuario mostrar la informacion del inventario en
    la que esta almacenada en el diccionario

    Args:
            valor_total (int): operacion para sacar el valor total que hay de cada producto

    Returns:
        str: Mensaje o cuadro con la informacion sobre el producto
    """
    print("Inventario Actual:")
    print("Código\tNombre\t\tStock\tPrecio\t\tPrecio total")
    print("------\t------\t\t------\t--------\t\t-------------")
    for id, datos in producto.items():
        valor_total = producto[id]['cantidad'] * producto[id]['precio']
        print(f"{id}\t{datos['nombre']}\t\t\t{datos['cantidad']}\t${datos['precio']:.2f}\t${valor_total}")
    print()


while True:
    print("1. Agregar producto \n"
          "2. Realizar venta \n"
          "3. Mostrar inventario \n"
          "4. Salir \n")
    opcion = int(input("Elija una opcion (1-4): "))
    match opcion:
        case 1:
            agregar_producto()
        case 2:
            realizar_venta()
        case 3:
            mostrar_inventario()
        case 4:
            respuesta = input("Esta seguro que desea salir (si o no): ").lower()
            if respuesta == "si":
                print("Saliendo...")
                break
            else:
                print("==============================")
                print("Volviendo al menu Principal")
                print("==============================")
        case _:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")
print("===================================================================")
print("Gracias por Utilizar el sistema. ¡Hasta luego!")
print("===================================================================")
