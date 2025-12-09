"""
Llegir el numero de frases i ses frases
A cada frase substituir les consonants per una Majúscula
Imprimer ses frases modificades
"""

def llegir_frases(n):
# Prec: donat un número
# Posta: retorna una llista de n-element llegits del teclat
    llista=list()
    for i in range(n):
        llista.append(input(""))
    return llista

def escriure_frases(llista):
#Prec: donada una llista d'element
#Post: Imprimeix cada element de la llista
    for e in llista:
        print(e)
    
def convertir_majuscules(s):
    vocal="aeiouAEIOU"
    llista = list(s)
    for i,e in enumerate(llista):
        if e not in vocal:
            llista[i]=e.upper()
    return "".join(llista)


#Programa principal
n = int(input(""))
llistat= llegir_frases(n)
for i,e in enumerate(llista):
    llista[i]=convertir_majuscules(e)
escriure_frases(llista)
