def es_primer(n):
    # Un número menor que 2 no és primer
    if n < 2:
        return False
    # Comprovem si el número és divisible per algun nombre entre 2 i la seva arrel quadrada
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Si trobem un divisor, el número no és primer
            return False
    return True

def numeros_prims():
    primers = []  # Llista per emmagatzemar els números primers
    for i in range(1, 101):
        if es_primer(i):
            primers.append(i)
    
    # Mostrem els números primers i la quantitat
    print("Números primers entre 1 i 100:", primers)
    print("Quantitat de números primers:", len(primers))

# Executem la funció
numeros_prims()
