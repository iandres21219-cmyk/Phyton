def es_de_traspas(anyo):
    # Verificar si es un año de traspàs según las reglas
    if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
        return True
    else:
        return False

# Ejemplo de uso
anyo = int(input("Introduce un año para saber si es de traspàs: "))
if es_de_traspas(anyo):
    print(f"{anyo} és un any de traspàs.")
else:
    print(f"{anyo} no és un any de traspàs.")
