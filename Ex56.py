def suma_numeros_inclusos(inici, fi):
    # Utilitzem range per obtenir la seqüència de números entre inici i fi (ambdós inclosos)
    return sum(range(inici, fi + 1))

# Funció principal
def main():
    # Demanem els dos números a l'usuari
    try:
        inici = int(input("Introdueix el primer número: "))
        fi = int(input("Introdueix el segon número: "))
        
        if inici > fi:
            print("El primer número ha de ser menor o igual al segon número.")
        else:
            # Cridem la funció per sumar els números entre els dos valors
            resultat = suma_numeros_inclusos(inici, fi)
            print(f"La suma dels números entre {inici} i {fi} és: {resultat}")
    
    except ValueError:
        print("Per favor, introdueix números enters vàlids.")

# Iniciar el programa
main()
