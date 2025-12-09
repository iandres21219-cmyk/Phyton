import string

def crear_llista_fitxer(nom_fitxer):
    # Obrim el fitxer en mode lectura
    try:
        with open(nom_fitxer, 'r') as fitxer:
            # Llegim el contingut del fitxer
            contingut = fitxer.read()
        
        # Eliminar la puntuació de cada paraula i separar el contingut en paraules
        taula_puntuacio = str.maketrans('', '', string.punctuation)
        llista_paraules = [paraula.translate(taula_puntuacio).lower() for paraula in contingut.split()]
        
        return llista_paraules
    
    except FileNotFoundError:
        print(f"El fitxer '{nom_fitxer}' no existeix.")
        return []
