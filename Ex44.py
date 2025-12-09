def taula_multiplicar():
    # Demanem un número a l'usuari dins del rang 1-20
    while True:
        try:
            numero = int(input("Introdueix un número entre 1 i 20 per veure la seva taula de multiplicar: "))
            if 1 <= numero <= 20:
                break
            else:
                print("El número ha de ser entre 1 i 20. Torna-ho a provar.")
        except ValueError:
            print("Per favor, introdueix un número vàlid.")
    
    # Imprimim la taula de multiplicar del número
    print(f"\nTaula de multiplicar del {numero}:")
    for i in range(1, 11):  # La taula de multiplicar va de 1 a 10
        print(f"{numero} x {i} = {numero * i}")

# Funció principal
taula_multiplicar()
