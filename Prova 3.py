def calculadora_Binaria(opcio):
    if opcio>0 and opcio<5:
        a = float(input("introdueixi el primer número: "))
        b = float(input("Introdueixi el segon número: "))
    match(opcio):
        case 1:
            #Suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de suma {} + {} és {}".format(a, b, c))
        case 2:
            #Resta
            print("Estic fent la Resta! \n")
            c = a - b
            print("El resultat de restar {} - {} és {}".format(a, b, c))
        case 3:
            #Multiplicacio
            print("Estic fent la Multiplicacio! \n")
            c = a * b
            print("El resultat de Multiplicacio {} * {} és {}".format(a, b, c))
        case 4:
            #Divisió
            print("Estic fent la multiplicació! \n")
            c = a // b
            print("El resultat de Divisió {} / {} és {}".format(a, b, c))
        case _:
            print("opció no valida! Torni-ho a provar! \n")