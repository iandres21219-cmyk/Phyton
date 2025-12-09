def gran_llista(llista):
    """Retorna el número més gran de la llista."""
    if not llista:          
        return None
    major = llista[0]
    for numero in llista[1:]:
        if numero > major:
            major = numero
    return major

# Proves
print(gran_llista([3, 4, 2, 3, 10]))    
print(gran_llista([7, 7, 7]))           
print(gran_llista([-5, -2, -10]))      
print(gran_llista([]))                  
