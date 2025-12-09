def crear_repetits(n, c):
    """Retorna el caràcter c repetit n vegades."""
    return c * n

# Proves
print(crear_repetits(5, "a"))    # "aaaaa"
print(crear_repetits(3, "x"))    # "xxx"
print(crear_repetits(0, "b"))    # ""
print(crear_repetits(7, "!"))    # "!!!!!!!"
