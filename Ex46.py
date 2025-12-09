def mostrar_digits_parells(n):
    digits_parells = []  # Llista per guardar els dígits parells
    
    # Recórrer cada dígit del número
    for digit in str(n):
        if int(digit) % 2 == 0:  # Comprovem si el dígit és parell
            digits_parells.append(digit)
    
    # Si hi ha dígits parells, els mostrem
    if digits_parells:
        print("Els dígits parells són:", " ".join(digits_parells))
    else:
        print("No hi ha dígits parells en aquest número.")

# Funció principal
def main():
    while True:
        try:
            numero = int(input("Introdueix un número: "))
            break
        except ValueError:
            print("Per favor, introdueix un número vàlid.")
    
    # Mostrem els dígits parells del número
    mostrar_digits_parells(numero)

# Iniciar el programa
main()
