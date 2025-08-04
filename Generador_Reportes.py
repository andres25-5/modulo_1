"""
Este es el proyecto final que integra todo. Escribe un script de Python que haga lo
siguiente:

1. Define una estructura de datos principal: un diccionario de estudiantes.
Las claves serán los nombres de los estudiantes y los valores serán listas
con sus calificaciones.
2. Crea una función calcular_promedio(calificaciones) que reciba una lista de
números y devuelva su promedio.
3. Crea una función obtener_estado(promedio) que devuelva "Aprobado" si el
promedio es mayor o igual a 3.0, y "Reprobado" en caso contrario.
4. Crea una función principal generar_reporte(estudiantes) que itere sobre el
diccionario de estudiantes. Para cada uno, debe llamar a las funciones
anteriores e imprimir un reporte formateado, como:
5. Reporte de Calificaciones:
6. -------------------------
7. - Estudiante: Ana, Promedio: 4.5, Estado: Aprobado
8. - Estudiante: Juan, Promedio: 2.8, Estado: Reprobado
9. -------------------------
10. Todo el script debe estar comentado, con docstrings en cada función
explicando qué hace, qué recibe y qué devuelve. La nomenclatura de
variables y funciones debe seguir PEP 8.

• Conceptos integrados: Diccionarios, listas, funciones (modularidad),
bucles, condicionales, f-strings, docstrings, y buenas prácticas de PEP 8.
"""
opcion = 0
estudiantes={}

def calcular_promedio(calificaciones):
    """
    ESta función permite al usuario ingresar los nombres de los estudiantes
    y sus respectivas calificaciones, calcula el promedio de cada estudiante
    y almacena los resultados en un diccionario.

    Args:
        calificaciones (list): Lista de calificaciones ingresadas por el usuario.
        estudiantes (dict): Diccionario donde las claves son los nombres de los estudiantes
                            y los valores son sus promedios de calificaciones.
    Returns:
        str: Mensaje de confirmación al calcular el promedio de cada estudiante.
        str: Mensaje de error si no se ingresan calificaciones.
        str: Mensaje de error si el promedio no es válido.
        str: Mensaje de error si la cantidad de estudiantes es menor a 1.
        str: Mensaje de error si la cantidad de calificaciones es menor a 1.
        str: Mensaje de error si la calificación ingresada no es un número.
    """
    cantidad_estudiantes = int(input("¿Cuántos estudiantes desea ingresar? "))

    for i in range(cantidad_estudiantes):
        print(f"\nEstudiante {i + 1}")
        clave = input("Ingrese el nombre del estudiante: ")
        cantidad_notas = int(input(f"¿Cuántas calificaciones tiene {clave}? "))

        notas = []
        for j in range(cantidad_notas):
            valor = float(input(f"Ingrese la calificación {j + 1}: "))
            notas.append(valor)

        promedio = sum(notas) / len(notas)
        estudiantes[clave] = promedio
        print(f"El promedio de {clave} es: {promedio:.2f}")


def obtener_estatado(promedio):
    """
    Esta función recibe un diccionario de estudiantes y sus promedios,
    y determina si cada estudiante aprobó o no, basándose en su promedio.
    Args:
        estudiantes (dict): Diccionario donde las claves son los nombres de los estudiantes
                            y los valores son sus promedios de calificaciones.
    Returns:
        str: Mensaje de estado de cada estudiante, indicando si aprobó o no.
        str: Mensaje de error si el promedio no es válido.
        str: Mensaje de error si el promedio no está en el rango de 0 a
        str: Mensaje de error si el promedio no es un número.
    """



    print("\n==========================")
    print("Promedios de todos los estudiantes:")
    for clave, promedio in estudiantes.items():
        estado = "APROBÓ" if promedio >= 3.0 and promedio <= 5.0 else "NO APROBÓ"
        print(f"{clave}: {promedio:.2f} su estado es; {estado}")


def generar_reporte(estudiantes):
    """
    Esta función genera un reporte de calificaciones para cada estudiante,
    mostrando su nombre, promedio y estado (aprobado o no aprobado).
    Args:
        estudiantes (dict): Diccionario donde las claves son los nombres de los estudiantes
                            y los valores son sus promedios de calificaciones.
    Returns:
        str: Imprime un reporte formateado en la consola.
        str: Mensaje de error si el diccionario de estudiantes está vacío.
        str: Mensaje de error si no hay estudiantes con calificaciones.
    """

    print("\nReporte de Calificaciones\n")
    print("Nombre\t\tPromedio\tEstado")
    print("------\t\t--------\t------")


    for nombre, promedio in estudiantes.items():
        estado = "APROBÓ" if promedio >= 3.0 else "NO APROBÓ"
        print(f"{nombre}\t\t{promedio:.2f}\t\t{estado}")

while True:

    print("1. Definir promedio estudiantes\n"
          "2. Promedio si aprobo o no aprobo\n"
          "3. Reporte de Calificaciones\n"
          "4. Salir")
    opcion = int(input("Ingrese la opcion: "))
    match opcion:
        case 1:
            calcular_promedio(estudiantes)
        case 2:
            obtener_estatado(estudiantes)
        case 3:
            generar_reporte(estudiantes)
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
