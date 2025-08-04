#Escribe una función que reciba una palabra o frase y determine si es un
#palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda),
#ignorando espacios y mayúsculas/minúsculas. La función debe retornar True o
#False.

frase =str.lower(input("Ingrese la frase : "))
frase=frase.replace(" ","")
frase_invertida = frase[::-1] # Variable para almacenar el texto invertido

def palindromo(frase):
    """
    Esta función recibe una palabra o una frase y determina si es palindromo.
    Tambien ignora espacios y caracteres especiales,diferencia entre mayusculas y minusculas.

    Args:
    frase  (str): una palabra o frase

    Returns:
     retorna si es o no un palindromo (bool)


    """

for i in range(len(frase) - 1, -1, -1): # 0 hasta 4
    frase_invertida = frase_invertida + frase[i]

if frase_invertida == frase:
    print(f"{frase} es un palíndromo")
else:
    print(f"{frase} no es un palíndromo")