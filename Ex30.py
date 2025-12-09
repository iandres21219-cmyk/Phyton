# Funció per convertir un binari a enter
def binari_a_enter(binari):
    """Converteix una cadena que representa un número binari a un enter."""
    return int(binari, 2)

# Proves
print(binari_a_enter("101"))    # 5
print(binari_a_enter("1111"))   # 15
print(binari_a_enter("100000")) # 32
print(binari_a_enter("0"))      # 0
