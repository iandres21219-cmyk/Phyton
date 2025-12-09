def comptar_vocals(palabra):
    # Inicializamos un diccionario para contar las vocales
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertimos la palabra a minúsculas para que la comparación no distinga entre mayúsculas y minúsculas
    palabra = palabra.lower()
    
    # Recorremos cada letra de la palabra
    for letra in palabra:
        if letra in vocals:
            vocals[letra] += 1
    
    # Generamos la cadena de texto que muestra los resultados
    resultat = ""
    for vocal, cantidad in vocals.items():
        resultat += f"Hi ha {cantidad} {vocal}'s, "
    
    return resultat[:-2]  # Eliminamos la última coma y el espacio extra

# Ejemplo de uso
palabra = "Ratapinyada"
print(comptar_vocals(palabra))
