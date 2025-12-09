def comptar_digits(n):
    # Convertim el número a cadena i retornem la seva llargada
    return len(str(n))

# Funció principal
def main():
    while True:
        try:
            numero = int(input("Introdueix un número entre 1 i 900000: "))
            if 1 <= numero <= 900000:
                break
            else:
                print("El número ha de ser entre 1 i 900000. Torna-ho a provar.")
        except ValueError:
            print("Per favor, introdueix un número vàlid.")
    
    # Comprovem la quantitat de dígits
    num_digits = comptar_digits(numero)
    
    # Mostrem el resultat
    print(f"El número {numero} té {num_digits} dígits.")

# Iniciar el programa
main()
