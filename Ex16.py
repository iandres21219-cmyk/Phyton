def gran_de_tres(a, b, c):
    """Retorna el número més gran entre a, b i c."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Proves
print(gran_de_tres(3, 7, 5))     # 7
print(gran_de_tres(10, 2, 8))    # 10
print(gran_de_tres(-5, -1, -3))  # -1
print(gran_de_tres(4, 4, 2))     # 4
print(gran_de_tres(6, 6, 6))     # 6 (tots iguals)
