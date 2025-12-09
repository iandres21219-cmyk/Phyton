def superposicio(llista1, llista2):
    """Retorna vertader si les dues llistes tenen algun element en comú."""
    for element in llista1:
        if element in llista2:
            return True
    return False

# Proves
print(superposicio([1, 2, 3], [4, 5, 6]))       # False
print(superposicio([1, 2, 3], [3, 4, 5]))       # True
print(superposicio(["a", "b"], ["c", "d"]))     # False
print(superposicio(["hola"], ["adéu", "hola"])) # True
