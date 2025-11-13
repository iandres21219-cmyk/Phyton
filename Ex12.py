def majoredat (Edat):
    if Edat<18:
        print ("Eres menor de edat")
    elif Edat>18:
        print ("pots accidir ets mayor de edat")
    else:
        print ("tens la edad justa")
        print ("Hola, tens {} años".format(Edat))

Edat = int(input("Escriu la teva Edat: "))
majoredat(Edat)
Edat = int(input("Escriu la seva edat: "))
majoredat(Edat)