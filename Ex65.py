def llista_a_diccionari(llista):
    # Utilitzem enumerate per obtenir l'índex i el valor, i construïm el diccionari
    return {valor: index for index, valor in enumerate(llista)}

# Prova de la funció
llista = ['casa', 'cotxe', 'cadira', 'taula']
diccionari = llista_a_diccionari(llista)
print(diccionari)  # Ha de retornar: {'casa': 0, 'cotxe': 1, 'cadira': 2, 'taula': 3}
