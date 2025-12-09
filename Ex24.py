def crear_punts(llista):
    """Pinta tants punts com el valor de cada número de la llista, un salt de línia per cada element."""
    for numero in llista:
        print("." * numero)

# Prova
crear_punts([2, 3, 4])
