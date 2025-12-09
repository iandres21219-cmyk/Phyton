def hi_ha_duplicats(llista):
    # Convertim la llista en un conjunt i comparem les longituds
    if len(llista) != len(set(llista)):
        return True  # Hi ha duplicats
    else:
        return False  # No hi ha duplicats

# Proves de la funció
print(hi_ha_duplicats([1, 2, 3, 4, 5]))  # Ha de dir: False (no hi ha duplicats)
print(hi_ha_duplicats([1, 2, 3, 4, 5, 3]))  # Ha de dir: True (hi ha duplicats)
print(hi_ha_duplicats([10, 10, 10, 10]))  # Ha de dir: True (hi ha duplicats)
