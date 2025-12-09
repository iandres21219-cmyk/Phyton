from abc import ABC, abstractmethod

# Classe base Animal
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass
    
    @abstractmethod
    def moure(self):
        pass
    
    @abstractmethod
    def quisoc(self):
        pass

# Subclass Cavall
class Cavall(Animal):
    def __init__(self, edat):
        super().__init__("Cavall", edat)
    
    def xerrar(self):
        print("El cavall no pot xerrar.")
    
    def moure(self):
        print("El cavall galopa.")
    
    def quisoc(self):
        print("El cavall fa un neig.")
        
# Subclass Dofí
class Dofí(Animal):
    def __init__(self, edat):
        super().__init__("Dofí", edat)
    
    def xerrar(self):
        print("El dofí fa so de saltar a l'aigua.")
    
    def moure(self):
        print("El dofí nedant.")
    
    def quisoc(self):
        print("El dofí fa un crit característic.")

# Subclass Abella
class Abella(Animal):
    def __init__(self, edat):
        super().__init__("Abella", edat)
    
    def xerrar(self):
        print("L'abelleta no pot xerrar.")
    
    def moure(self):
        print("L'abelleta vola.")
    
    def quisoc(self):
        print("L'abelleta fa zumbidos.")
    
    def picar(self):
        print("L'abelleta pica amb el seu agulló.")

# Subclass Humà
class Humà(Animal):
    def __init__(self, edat, nom):
        super().__init__("Humà", edat)
        self.nom = nom
    
    def xerrar(self):
        print(f"{self.nom} diu hola.")
    
    def moure(self):
        print(f"{self.nom} camina.")
    
    def quisoc(self):
        print(f"{self.nom} fa un crit humà.")
        
# Subclass Fiet (subclasse de Humà)
class Fiet(Humà):
    def __init__(self, edat, nom, pares):
        super().__init__(edat, nom)
        self.pares = pares
    
    def nompares(self):
        return ", ".join(self.pares)

# Subclass Centaure (herència múltiple, de Cavall i Humà)
class Centaure(Cavall, Humà):
    def __init__(self, edat, nom):
        Cavall.__init__(self, edat)
        Humà.__init__(self, edat, nom)
    
    def xerrar(self):
        print(f"{self.nom} (Centaure) diu: sóc un centaure!")
    
    def moure(self):
        print(f"{self.nom} galopa com un cavall i camina com un humà.")
    
    def quisoc(self):
        print("El centaure fa un crit de batalla!")

# Classe Xou (sense herència, implementa els mètodes d'Animal)
class Xou(Animal):
    def __init__(self, edat):
        super().__init__("Xou", edat)
    
    def xerrar(self):
        print("El xou fa sorolls excèntrics.")
    
    def moure(self):
        print("El xou balla en una coreografia.")
    
    def quisoc(self):
        print("El xou crida '¡Som-hi!'")

# Crear llista d'objectes
animals = [
    Cavall(5),
    Dofí(3),
    Abella(1),
    Humà(30, "Marc"),
    Fiet(20, "Laura", ["Paula", "Joan"]),
    Centaure(100, "Centaureus"),
    Xou(10)
]

# Bucle per cridar els mètodes de cada objecte
for animal in animals:
    print(f"\n{animal.especie} ({animal.edat} anys):")
    animal.xerrar()
    animal.moure()
    animal.quisoc()
    
    if isinstance(animal, Abella):
        animal.picar()
    
    if isinstance(animal, Fiet):
        print(f"Nom dels pares: {animal.nompares()}")
