def mostrar_majors_que(tupla_numeros, x):
    """Imprimeix tots els números de la tupla que són superiors a x."""
    for numero in tupla_numeros:
        if numero > x:
            print(numero)

# Programa principal
# Introduir els números de la tupla
valors = input("Introdueix els números separats per comes: ")
# Convertim la cadena introduïda a tupla d'enters
tupla_valors = tuple(int(num.strip()) for num in valors.split(","))

# Mostrem els números majors de 18
print("Números majors de 18:")
mostrar_majors_que(tupla_valors, 18)
