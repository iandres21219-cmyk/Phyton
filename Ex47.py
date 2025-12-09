def eliminarcapicua(llista):
    # Eliminem el primer i el darrer element de la llista
    return llista[1:-1]

# Prova de la funció
llista_original = [1, 2, 3, 4, 5, 6]
llista_nova = eliminarcapicua(llista_original)

print("Llista original:", llista_original)
print("Nova llista sense el primer i l'últim element:", llista_nova)
