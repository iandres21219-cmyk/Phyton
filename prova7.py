v1 = 10
while (v1>=5 and v1<=10) or (v1>=15 and v1<=20) or (v1>25 and v1<=30) and (v1 !=6) and v1!=26:
    v1 = int(input("Introdueix l'operador"))
    print(v1)
print("Has inscrit un número menor o igual que 3, adéu!")




"""
r = v1 == v2
print(r)
r = v1 != v2
print(r)
r = v1 > v2
print(r)
r = v1 < v2
print(r)
r = v1 >= v2
print(r)
r = v1 <= v2
print(r)
"""
v1 = int(input("introdueix el primer operador:"))
v2 = int(input("introdueix el segon operador"))
r = v1 + v2
print(r)
r = v1 - v2
print(r)
r = v1 * v2
print(r)
r = v1 // v2 # Divisió entera
print(r)
r = v1 / v2 # Divisió real
print(r)
r = v1 % v2
print(r)
r = v1 ** v2
print(r)
r = v1 + (v2**2 / v1 - (v1%v2))
print(r)

