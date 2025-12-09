def paraules_per_letra(llista, lletra):
    return list(filter(lambda paraula: paraula.startswith(lletra), llista))

llista_paraules = ["maria", "manta", "peu", "mà"]
lletra = 'p'
resultat = paraules_per_letra(llista_paraules, lletra)
print(resultat)  