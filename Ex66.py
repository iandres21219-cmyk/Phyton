def comptar_coincidencies(llista):
    return sum(1 for index, valor in enumerate(llista) if index == valor)

# Prova de la funció
llista = [0, 2, 3, 3, 4]
resultat = comptar_coincidencies(llista)
print(resultat)  # Ha de retornar: 3
