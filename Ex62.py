from functools import reduce

def Passar_a_Numero(llista):
    # Utilitzem reduce per combinar els dígits i construir el número
    return reduce(lambda x, y: x * 10 + y, llista)

# Prova de la funció
llista_digits = [3, 4, 1, 5]
numero = Passar_a_Numero(llista_digits)
print(numero)  # Ha de retornar: 3415
