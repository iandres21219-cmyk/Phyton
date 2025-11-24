"""
Definir una funció que agafi un caràcter i 
retorni vertader si és una vocal i en cas contrari retorni fals. 
Prova-la amb diferents exemples.
"""


def ex18(c):
    v = "aeiouAEIOUáàèéìíòóúùÀÁÈÉÌÍÒÓÙÚ"
    if c in v:
        return True
    else:
        return False

# Programa principal
c = input("Escriu un caràcter per a provar si és o o vocal: ")
print(ex18(c))