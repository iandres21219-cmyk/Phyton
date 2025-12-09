def elevar_a_potencia(potencia):
    # Generem la llista dels primers 10 números elevats a la potència indicada
    return [i ** potencia for i in range(11)]

# Proves de la funció

# Quadrats (potència 2)
print("Quadrats:", elevar_a_potencia(2))  # Ha de retornar: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Cubs (potència 3)
print("Cubs:", elevar_a_potencia(3))  # Ha de retornar: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Altres potències (potència 4)
print("Potència 4:", elevar_a_potencia(4))  # Ha de retornar: [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]
