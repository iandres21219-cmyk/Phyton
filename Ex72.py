import os

# 1. Crear el directori /home/cicles/AO/Prova
directori = '/home/cicles/AO/Prova'
if not os.path.exists(directori):
    os.makedirs(directori)  # Creem el directori Prova si no existeix

# 2. Canviar-nos a aquest directori
os.chdir(directori)

# 3. Crear el fitxer Ex12.txt i escriure els noms dels companys de classe
nom_fitxer = 'Ex12.txt'

# Obrim el fitxer per escriure els noms dels companys de classe
with open(nom_fitxer, 'w') as fitxer:
    fitxer.write("Company 1\n")  # Afegeix els noms dels companys de classe
    fitxer.write("Company 2\n")
    fitxer.write("Company 3\n")
    # Afegir més noms segons sigui necessari
    fitxer.close()

# 4. Obrir el fitxer per afegir els noms dels professors
with open(nom_fitxer, 'a') as fitxer:
    fitxer.write("Professor 1\n")  # Afegeix els noms dels professors
    fitxer.write("Professor 2\n")
    fitxer.close()

# 5. Obrir el fitxer per llegir tot el contingut i posar-lo en una llista
llista_noms = []
with open(nom_fitxer, 'r') as fitxer:
    llista_noms = fitxer.readlines()  # Llegim totes les línies i les emmagatzemem en una llista

# Eliminem el salt de línia al final de cada element de la llista
llista_noms = [nom.strip() for nom in llista_noms]

# 6. Mostrem la llista de noms
print(llista_noms)
