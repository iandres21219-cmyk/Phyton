def crear_llista_fitxer(nom_fitxer):
    # Obrim el fitxer en mode de lectura
    with open(nom_fitxer, 'r') as fitxer:
        # Llegim tot el contingut del fitxer i separem en paraules
        contingut = fitxer.read()
        llista_paraules = contingut.split()  # Separa per espais, salts de línia, etc.
    return llista_paraules

# Prova de la funció
nom_fitxer = "exemple.txt"  # El nom del fitxer que volem llegir

# Creem una llista de paraules a partir del fitxer
llista = crear_llista_fitxer(nom_fitxer)

# Mostrem el resultat
print("Llista de paraules:", llista)
