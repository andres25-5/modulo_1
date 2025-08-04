"""
Crea una función que reciba un texto (string) y devuelva un diccionario con la
frecuencia de cada palabra. El diccionario tendrá las palabras como claves y su
conteo como valor. No debe distinguir entre mayúsculas y minúsculas.

• Conceptos aplicados: Diccionarios (método get), funciones, strings)
(métodos split, lower), bucle for.
"""



# Pedir al usuario que ingrese el texto
texto = input("Ingrese el texto: ")
def frecuencia(texto):
    """
    Esta funcion recibe un texto o una palabra y determina que cantidad de
    veces esta esa palabra en el texto.

    Args:
        texto (str): Texto que desea ser frecuencia
        palabras (list): Lista de palabras
        frecuencia (dic): Diccionario que contiene la frecuencia de las palabras

    Returns:
        La frecuencia de las palabras (dic)
        La cantidad de palabras (int)
    """
# Convertir el texto a minúsculas y dividir en palabras
texto = texto.lower()
palabras = texto.split()
frecuencia = {}

# Contar frecuencia de cada palabra
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Mostrar el resultado
print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencia.items():
    print(f"{palabra} = {cantidad}")
