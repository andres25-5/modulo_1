"""
Escribe un programa que utilice un diccionario para almacenar factores de
conversión (ej: de metros a pies). Luego, crea una función que reciba una
cantidad, la unidad de origen y la unidad de destino, y realice la conversión. La
función debe manejar el caso en que una unidad no exista en el diccionario.

• Conceptos aplicados: Diccionarios, funciones con múltiples parámetros,
return, manejo de errores básicos con if key in dict.
"""

factores_conversion = {
    "metro": 1,
    "pie": 3.28084,
    "pulgada": 39.3701,
    "kilometro": 0.001,
    "centimetro": 100,
    "milimetro": 1000,
    "yarda": 1.09361
}

def convertir(cantidad, unidad_origen, unidad_destino):
    if unidad_origen in factores_conversion and unidad_destino in factores_conversion:
        cantidad_en_metros = cantidad / factores_conversion[unidad_origen]
        resultado = cantidad_en_metros * factores_conversion[unidad_destino]
        return resultado
    else:
        return "Error: Unidad no válida. Revisa el nombre de las unidades."

cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Unidad de origen (ej. metro, pie, pulgada): ").lower()
unidad_destino = input("Unidad de destino (ej. metro, pie, pulgada): ").lower()

# Realizar conversión
resultado = convertir(cantidad, unidad_origen, unidad_destino)

print(f"\nResultado: {cantidad} {unidad_origen} = {resultado} {unidad_destino}")