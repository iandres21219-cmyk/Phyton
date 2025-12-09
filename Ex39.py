def comprobar_rima(palabra1, palabra2):
    # Convertimos las palabras a minúsculas para evitar problemas con mayúsculas y minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Comprobamos si las últimas 3 letras coinciden
    if palabra1[-3:] == palabra2[-3:]:
        return "Les paraules rimen!"
    # Si no, comprobamos si las últimas 2 letras coinciden
    elif palabra1[-2:] == palabra2[-2:]:
        return "Les paraules rimen un poc."
    # Si no coinciden ni las 3 ni las 2 últimas letras
    else:
        return "Les paraules no rimen."

# Funció principal
def main():
    # Solicitamos las dos palabras al usuario
    palabra1 = input("Introdueix la primera paraula: ")
    palabra2 = input("Introdueix la segona paraula: ")

    # Comprobamos si riman o no
    resultado = comprobar_rima(palabra1, palabra2)
    print(resultado)

# Iniciar el programa
main()
