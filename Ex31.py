# Any actual
any_actual = 2022

# Dades de les persones: nom i any de naixement
persones = [
    ("Pere", 2000),
    ("Maria", 1999),
    ("Anna", 2005),
    ("Joan", 2010)
]

# Capçalera
print(f"{'Nom':<10}\t{'Data naixement':<15}\t{'Anys que farà aquest any':<25}")

# Dades de cada persona
for nom, any_naixement in persones:
    edat = any_actual - any_naixement
    print(f"{nom:<10}\t{any_naixement:<15}\t{edat:<25}")
