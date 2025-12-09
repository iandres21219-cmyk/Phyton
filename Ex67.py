def lletres_a_llista(paraula):
    # Utilitzem list comprehension per convertir la paraula en una llista de lletres
    return [lletra for lletra in paraula]

# Prova de la funció
paraula = "institut"
resultat = lletres_a_llista(paraula)
print(resultat)  # Ha de retornar: ['i', 'n', 's', 't', 'i', 't', 'u', 't']
