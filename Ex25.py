def crear_punts(llista):
    """Pinta tants punts com el valor de cada número de la llista, un salt de línia per cada element."""
    for numero in llista:
        print("." * numero)

def dibuixar_imatge():
    """Dibuixa una imatge utilitzant la funció crear_punts()."""
    # Cada número indica quants punts posar en cada línia
    patró = [1, 3, 5, 3, 1]  # Això farà una mena de diamant petit
    crear_punts(patró)

# Prova
dibuixar_imatge()
