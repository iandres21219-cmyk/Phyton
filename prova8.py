for i in range(1,1001):
    if (i%9==0 or i%7==0) and not (i%5!=0 and i%8!=0):
        print(i)

print("Has inscrit un número menor o igual que 3, adéu!")