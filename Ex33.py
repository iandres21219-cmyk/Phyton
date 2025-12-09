def nums_que_comencen_per(noms):
    # Contamos cuántos nombres comienzan con la letra 'a' o 'A'
    count = 0
    for nom in noms:
        if nom.lower().startswith('a'):
            count += 1
    return count

# Ejemplo de uso
llista_noms = ["Anna", "Maria", "Arnau", "Joan", "Albert"]
resultat = nums_que_comencen_per(llista_noms)
print(f"Nombre de noms que comencen per 'a': {resultat}")
