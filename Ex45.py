def sumar_digits(n):
    # Convertim el número a cadena per poder accedir als seus dígits
    suma = 0
    for digit in str(n):
        suma += int(digit)  # Sumem cada dígit convertit a enter
    return suma

def main():
    while True:
        try:
            numero = int(input("Introdueix un número: "))
            break
        except ValueError:
            print("Per favor, introdueix un número vàlid.")
    
    # Sumar els dígits del número
    suma_dits = sumar_digits(numero)
    
    # Comprovar si la suma és parell o senar
    if suma_dits % 2 == 0:
        print(f"La suma dels dígits de {numero} és {suma_dits} i és parell.")
    else:
        print(f"La suma dels dígits de {numero} és {suma_dits} i és senar.")

# Iniciar el programa
main()
