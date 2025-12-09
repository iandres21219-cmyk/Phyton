def index_paraula(llista, paraula):
    try:
        # Intentem obtenir l'índex de la paraula a la llista
        return llista.index(paraula)
    except ValueError:
        # Si la paraula no es troba, retornem -1
        return -1

# Proves de la funció
llista_ordenada = ["alta", "baix", "gran", "mitjà", "petit"]
print(index_paraula(llista_ordenada, "gran"))  # Ha de retornar: 2
print(index_paraula(llista_ordenada, "mitjà"))  # Ha de retornar: 3
print(index_paraula(llista_ordenada, "molt gran"))  # Ha de retornar: -1
