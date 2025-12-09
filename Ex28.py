def filtrar_paraules(llista_paraules, x):
    """Retorna una llista amb les paraules que tenen més de x caràcters."""
    resultat = []
    for paraula in llista_paraules:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat

# Proves
print(filtrar_paraules(["Hola", "Ramis", "IES", "Paraula"], 3))  # ['Hola', 'Ramis', 'Paraula']
print(filtrar_paraules(["a", "ab", "abc", "abcd"], 2))           # ['abc', 'abcd']
print(filtrar_paraules(["petit", "gran", "mitjà"], 5))           # ['mitjà']
print(filtrar_paraules([], 3))                                    # []
