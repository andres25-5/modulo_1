"""
Crea una función que reciba una lista de calificaciones (números). La función
debe calcular y retornar el promedio, la calificación más alta y la más baja en una
tupla. Luego, escribe el código para probar esta función con una lista de ejemplo.
"""
cantidad = int(input("Ingrese la cantidad de calificaciones: "))


def validar_cantidad(cantidad):
    """
    Esta función valida el promedio de las notas sabiendo la cantidad a ingresar, muestra la nota mas baja y la nota mas alta,
    con la cantidad de notas ingresadas y cuales fueron las notas.

    Args:

        cantidad (int): Cantidad de calificaciones a ingresar.
        calificaciones (list): Lista para almacenar las calificaciones ingresadas.
        calificacion (float): Variable para almacenar cada calificación ingresada.

    Returns:
        list: Lista de calificaciones ingresadas.
        int: Cantidad de calificaciones.
        float: Promedio de las calificaciones.
        float: Calificación más alta.
        float: Calificación más baja.

    """


def calcular_calificaciones():
    calificaciones = []  # Lista vacía para guardar las calificaciones

    for i in range(cantidad):
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(calificacion)
        while calificacion < 0 or calificacion > 5:
            print("La calificación debe estar entre 0 y 5. Inténtalo de nuevo.")
            calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
            calificaciones[i] = calificacion
    # Calcular promedio, calificación más alta y más baja
    promedio = sum(calificaciones) / len(calificaciones)
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)

    # Mostrar resultados
    print(f"Las calificaciones ingresadas fueron: {calificaciones}")
    print(f"Cantidad total de calificaciones ingresadas: {len(calificaciones)}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Calificación más alta: {calificacion_mas_alta:.2f}")
    print(f"Calificación más baja: {calificacion_mas_baja:.2f}")


calcular_calificaciones()
