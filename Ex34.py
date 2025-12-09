def nums_que_comencen_per(noms, lletra):
    # Contamos cuántos nombres comienzan con la letra introducida
    count = 0
    for nom in noms:
        if nom.lower().startswith(lletra.lower()):
            count += 1
    return count

# Solicitar la letra al usuario
lletra_usuari = input("Introduce una lletra per veure quants noms comencen amb ella: ")

# Ejemplo de lista de nombres
llista_noms = ["Anna", "Maria", "Arnau", "Joan", "Albert"]

# Llamamos a la función con la letra introducida por el usuario
resultat = nums_que_comencen_per(llista_noms, lletra_usuari)

print(f"Nombre de noms que comencen per '{lletra_usuari}': {resultat}")
