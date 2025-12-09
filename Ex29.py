def comptar_majuscules(cadena):
    """Retorna el nombre de lletres majúscules en la cadena."""
    contador = 0
    for car in cadena:
        if car.isupper():
            contador += 1
    return contador

# Proves
print(comptar_majuscules("Hola Mundo"))        # 2 (H i M)
print(comptar_majuscules("Python ES Divertit")) # 5 (P, E, S, D)
print(comptar_majuscules("ninguna"))           # 0
print(comptar_majuscules("123ABC!"))           # 3 (A, B, C)
