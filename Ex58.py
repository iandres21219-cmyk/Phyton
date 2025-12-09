def elements_parells(llista):
    # Iterem sobre la llista utilitzant els índexs parells
    for i in range(0, len(llista), 2):  # Comencem des de l'índex 0, amb pas 2
        print(llista[i])

# Prova de la funció
llista_paraules = ["gira", "elefant", "sol", "llum", "carretera", "mar"]
print("Paraules en posicions parelles:")
elements_parells(llista_paraules)
