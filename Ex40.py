# Funció per calcular el capital final
def calcular_capital_final(capital_inicial, interes, anys):
    capital_final = capital_inicial * (1 + interes / 100) ** anys
    return capital_final

# Funció principal
def main():
    # Demanem el capital inicial
    while True:
        capital_inicial = float(input("Introdueix el capital inicial (entre 50,000€ i 800,000€): "))
        if 50000 <= capital_inicial <= 800000:
            break
        else:
            print("El capital ha de ser entre 50,000€ i 800,000€. Torna-ho a provar.")
    
    # Demanem el tipus d'interès
    while True:
        interes = float(input("Introdueix el tipus d'interès (entre 0.5% i 13%): "))
        if 0.5 <= interes <= 13:
            break
        else:
            print("L'interès ha de ser entre 0.5% i 13%. Torna-ho a provar.")
    
    # Demanem el número d'anys
    while True:
        anys = int(input("Introdueix el número d'anys (entre 3 i 40): "))
        if 3 <= anys <= 40:
            break
        else:
            print("El número d'anys ha de ser entre 3 i 40. Torna-ho a provar.")
    
    # Calculem el capital final
    capital_final = calcular_capital_final(capital_inicial, interes, anys)
    
    # Mostrem el resultat amb 2 decimals
    print(f"El capital final després de {anys} anys serà: {capital_final:.2f}€")

# Iniciar el programa
main()
