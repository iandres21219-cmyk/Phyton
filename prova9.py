def ordenar(x, y):
      
    if x>y:
        return y, x
    elif y<x:
        return x, y
    else:
        return x, y
v1 = int(input("Intro el 1r número " ))
v2 = int(input("Intro el 2r número " ))

v2, v1 = ordenar(v1, v2)
for e in range(v2, v1+1, 2):
    if e%2==1:
        print(e)