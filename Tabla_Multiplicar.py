#Pide al usuario un número entero y muestra la
# tabla de multiplicar de ese número del 1 al
# 10. El formato de salida debe ser claro, por ejemplo: 5 x 1 = 5.

num=int(input("Ingrese un número entero: "))

def multiplicar(num,resultado):
    """
    Esta función nos sirve para hacer la multiplicación
    con el numero que ingreso el usuario.

    Args:
        num(int):num
        resultado(int): resultado
    return:
    resultado(int): resultado


    """

for i in range(1,11):
    resultado=num*i
    print(f"{num} x {i} = {resultado}")