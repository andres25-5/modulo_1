#Escribe un programa que solicite la edad del usuario y
# determine si es mayor de edad o no. El
# programa debe mostrar un mensaje apropiado. Adicionalmente, si la
# edad está entre 18 y 25 años, debe mostrar un
# mensaje indicando que es un "joven adulto".

edad=int(input("Ingrese su edad: "))

def relacional(edad):
    """
    Esta función lo que hace es comparar la edad que
    ingresa la persona para identificar si es joven adulto,mayor o menor de edad.

    Args:
        edad (int): edad
    Returns:no retorna nada lo que hace es imprimir el mensaje
"""

if edad<=0:
    print(f"La edad que ingreso es {edad},no es valida")
elif edad<18:
    print(f"La edad que ingreso es {edad},entonces usted es menor de edad")
elif edad>=18 and edad<=25:
      print(f"La edad que ingreso es {edad},entonces usted es un Joven Adulto")
else :
     print(f"La edad que ingreso es {edad},entonces usted es mayor de edad ")