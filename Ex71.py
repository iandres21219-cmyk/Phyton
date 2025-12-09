def llegir_fitxer(nom_fitxer):
    try:
        # Intentem obrir el fitxer amb 'with' per garantir el tancament automàtic
        with open(nom_fitxer, 'r') as fitxer:
            # Llegim tot el contingut del fitxer
            contingut = fitxer.read()
            return contingut
    except FileNotFoundError:
        # Si el fitxer no existeix, capturem l'error i avisem l'usuari
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except Exception as e:
        # Si es produeix qualsevol altre error, el capturem i el mostrem
        print(f"Error inesperat: {e}")
        return None

# Proves de la funció
nom_fitxer = "exemple.txt"
contingut = llegir_fitxer(nom_fitxer)

if contingut is not None:
    print("Contingut del fitxer:")
    print(contingut)
else:
    print("No s'ha pogut llegir el fitxer.")
