def es_palindrom(paraula):
    """Retorna vertader si la paraula és un palíndrom i fals altrament."""
    paraula = paraula.lower()        # per evitar problemes de majúscules
    return paraula == paraula[::-1]  # compara amb la paraula invertida

# Proves
print(es_palindrom("radar"))   # True
print(es_palindrom("ara"))     # True
print(es_palindrom("civic"))   # True
print(es_palindrom("hola"))    # False
print(es_palindrom("Refer"))   # True
