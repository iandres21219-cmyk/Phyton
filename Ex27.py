def paraula_mes_llarga(llista_paraules):
    """Retorna la paraula amb més caràcters de la llista."""
    if not llista_paraules:
        return None
    mes_llarga = llista_paraules[0]
    for paraula in llista_paraules[1:]:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga

# Proves
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))
print(paraula_mes_llarga(["a", "ab", "abc"]))                    
print(paraula_mes_llarga([]))                                    
