def lenp(frase):
    # Dividim la frase en paraules
    paraules = frase.split()
    
    # Utilitzem map per aplicar la funció len a cada paraula
    longituds = list(map(len, paraules))
    
    return longituds

# Prova de la funció
frase = "Aquesta és una prova"
print(lenp(frase))  # Ha de retornar: [7, 2, 3, 4]
