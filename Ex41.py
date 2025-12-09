def suma_quadrats(n):
    suma = 0
    while n >= 0:  # Continuar mientras el número sea mayor o igual que 0
        suma += n**2  # Sumar el cuadrado del número
        n -= 4  # Restar 4 al número
    return suma

# Funció principal
def main():
    # Sol·licitem l'entrada de l'usuari
    while True:
        numero = int(input("Introdueix un número menor de 100: "))
        if numero < 100:
            break
        else:
            print("El número ha de ser menor de 100. Torna-ho a provar.")
    
    # Calculem la suma dels quadrats
    resultat = suma_quadrats(numero)
    
    # Mostrem el resultat
    print(f"La suma dels quadrats és: {resultat}")

# Iniciar el programa
main()
