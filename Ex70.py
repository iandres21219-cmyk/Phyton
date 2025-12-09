def divisio(x, y):
    try:
        resultat = x / y
        return resultat
    except ZeroDivisionError:
        print("Error: No es pot dividir per zero.")
        return None  

print(divisio(10, 2))  
print(divisio(10, 0))  
