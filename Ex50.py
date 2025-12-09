import random

# Funció per generar una llista de 20 elements aleatoris entre 1 i 100
def llista_20_elements():
    llista = [random.randint(1, 100) for _ in range(20)]
    return llista

# Funció per comprovar si hi ha duplicats
def hi_ha_duplicats(llista):
    # Convertim la llista en un conjunt i comparem les longituds
    if len(llista) != len(set(llista)):
        return True  # Hi ha duplicats
    else:
        return False  # No hi ha duplicats

# Crear una llista aleatòria de 20 elements
llista = llista_20_elements()

# Mostrar la llista generada
print("Llista generada:", llista)

# Comprovar si la llista té duplicats
if hi_ha_duplicats(llista):
    print("La llista té duplicats.")
else:
    print("La llista no té duplicats.")
