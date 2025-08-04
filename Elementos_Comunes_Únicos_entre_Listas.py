"""
Desarrolla una función que reciba dos listas y devuelva una tupla con tres
conjuntos (sets):

1. Un conjunto con los elementos que están en ambas listas.
2. Un conjunto con los elementos que solo están en la primera lista.
3. Un conjunto con los elementos que solo están en la segunda lista.

• Conceptos aplicados: Funciones, listas, conjuntos (sets), operadores de
conjuntos (&, -).
"""

entrada1 = input("Ingrese la primera lista de números separados por comas: ")
entrada2 = input("Ingrese la segunda lista de números separados por comas: ")

def validar_entrada(entrada):
    """
    Valida que la entrada sea una lista de números enteros separados por comas.

    Args:
        entrada (str): Cadena de texto con números separados por comas.
        conjunto (set): Conjunto de números enteros.
        set1 (set): Conjunto de números enteros de la primera lista.
        set2 (set): Conjunto de números enteros de la segunda lista.

    Returns:
        Un conjunto  que estan en ambas listas (int).
        Conjunto que solo estan en la primera lista (int).
        Conjunto que solo estan en la segunda lista (int).
    """
lista1 = list(map(int, entrada1.split(",")))
lista2 = list(map(int, entrada2.split(",")))

set1 = set(lista1)
set2 = set(lista2)

conjunto = set1 & set2           # ambas listas
conjunto1 = set1 - set2          # Solo en la primera
conjunto2 = set2 - set1          # Solo en la segunda

print(f"Conjunto de elementos que están en ambas listas: {conjunto}")
print(f"Conjunto de elementos que solo están en la primera lista: {conjunto1}")
print(f"Conjunto de elementos que solo están en la segunda lista: {conjunto2}")
