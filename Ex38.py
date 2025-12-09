import random

# Funció per generar un codi secret de 4 xifres
def generar_codi():
    codi_secret = random.randint(1000, 9999)  # Genera un número entre 1000 i 9999
    return str(codi_secret)

# Funció per comparar el codi introduït per l'usuari amb el codi secret
def comparar_codis(codi_secret, codi_introduit):
    encertats = 0  # Nombre de xifres en la posició correcta
    mal_posicio = 0  # Nombre de xifres que són en el codi però no en la posició correcta
    
    # Comprovem les xifres en la posició correcta
    for i in range(4):
        if codi_introduit[i] == codi_secret[i]:
            encertats += 1
    
    # Comprovem les xifres que són al codi però no en la posició correcta
    for i in range(4):
        if codi_introduit[i] != codi_secret[i] and codi_introduit[i] in codi_secret:
            mal_posicio += 1

    return encertats, mal_posicio

# Funció principal
def jugar():
    codi_secret = generar_codi()  # Generem el codi secret
    intents = 0  # Comptem els intents

    print("Bévingut al joc MasterMind! Has de descobrir un codi de 4 xifres.")
    
    while True:
        # Demanem l'entrada de l'usuari
        codi_introduit = input("Introdueix un codi de 4 xifres: ")
        
        # Comprovem que la llargada sigui de 4 xifres i que sigui un número
        if len(codi_introduit) != 4 or not codi_introduit.isdigit():
            print("Per favor, introdueix un codi vàlid de 4 xifres.")
            continue

        intents += 1
        
        # Comprovem les xifres del codi
        encertats, mal_posicio = comparar_codis(codi_secret, codi_introduit)
        
        # Informem de la situació
        print(f"Xifres encertades en la posició correcta: {encertats}")
        print(f"Xifres que són al codi però en una posició incorrecta: {mal_posicio}")
        
        # Si el jugador ha encertat el codi
        if encertats == 4:
            print(f"Felicitats! Has endevinat el codi {codi_secret} en {intents} intents.")
            break

# Iniciar el joc
jugar()
