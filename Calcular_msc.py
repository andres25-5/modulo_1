#Crea un programa que pida al usuario su peso (en kg)
# y su altura (en metros).
#Calcula el IMC usando la fórmula:IMC=altura2peso
#y muestre el resultado con un mensaje claro y formateado, redondeado a dos
#decimales.

peso=float(input("Ingrese el peso en kilogramos: "))
altura=float(input("Ingrese la altura en metros: "))
def division (peso,altura):
    """
    Esta función divide el peso por la altura en metros.

    Args:
    peso (float): peso en kilogramos
    altura (float): altura en metros.
    Returns:
       float: resultado de la division

    """
IMC=peso/altura**2
print(f"El IMC es: {IMC:.2f}")