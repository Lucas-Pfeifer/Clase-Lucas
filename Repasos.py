import time
import random

class Bloque:

    ##Atributos

    dureza = 0
    textura = ""
    agarrable = False
    gravedad = False
    vida = 100
    x = -1
    y = -1
    z = -100

    def __init__(self, x, y, z, dureza, textura, agarrable, gravedad):
        self.x = x
        self.y = y
        self.z = z
        self.dureza = dureza
        self.textura = textura
        self. agarrable = agarrable
        self.gravedad = gravedad

    def recuperacion(self):
        while (self.vida < 100):
            time.sleep(1)
            print(f"Recupere 1 de vida \n Vida actual: {self.vida}")
            self.vida += 1

class Entity:

    ##Atributos

    vida = 0
    rapidez = 0
    armadura = 0
    salto = 0
    inventario = []
    mano = 10 
    equipamiento = False
    saciedad = 20
    x = -1
    y = -1
    z = -1000

    def __init__(self, vida, rapidez, armadura, salto, inventario, equipamiento):
        self.x  = random.randint(0,1000)
        self.y  = random.randint(0,1000)
        self.z = 0
        self.vida = vida
        self.rapidez = rapidez
        self.armadura = armadura
        self.salto = salto
        self.inventario = inventario
        self.equipamiento = equipamiento

    def hambre(self):
        if(self.saciedad > 0):
            self.saciedad -= 1
        else:
            if(self.vida>0):
                self.vida -= 1
            self.muerte()
        if (self.saciedad == 5):
            self.velocidad = self.velocidad/2
        
    def muerte(self):
        print("La entidad a muerto")

    def debilitar(self, bloque):
        for i in range(2):
            if(bloque.vida > 0):
                bloque.vida -= self.mano/2
                print(f"He golpeado {self.mano/2}")
                print(f"Vida del bloque {bloque.vida}")

                time.sleep(0.5)
        bloque.recuperacion()


tierra = Bloque(1 , 2, 3, 50, "File101.txt", True, True)

personaje = Entity(20, 1.5, 0, 1.5, [], True)

#personaje.debilitar(tierra)

personaje.vida = personaje.vida + 1

#Usuario: Rut, Nombre, Edad
#Instanciar un usuario con nombre carlos e imprimir su rut



class human:
    rut = None 
    name = None
    edad = None

    def __init__(self):
        self.rut = int(input("Escriba su rut: "))
        self.name = input("Escriba su nombre: ")
        self.edad = input("Escriba su edad: ")

user = human()

print(f"Rut: {user.rut}")
print(f"Nombre: {user.name}")
print(f"Edad: {user.edad}")



    
    
