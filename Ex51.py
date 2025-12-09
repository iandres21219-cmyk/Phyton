def elimina_duplicats(llista):
    # Convertim la llista en un conjunt per eliminar duplicats i després la tornem a convertir en llista
    return list(set(llista))

# Prova de la funció
llista_original = [1, 2, 3, 4, 5, 1, 2, 6, 7, 3]
llista_sense_duplicats = elimina_duplicats(llista_original)

print("Llista original:", llista_original)
print("Llista sense duplicats:", llista_sense_duplicats)
