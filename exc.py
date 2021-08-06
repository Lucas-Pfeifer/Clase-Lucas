import time
# Clase Persona -> Alumno ; Profesor. Sala de Clase

# Persona: rut: int, edad: int, genero: str, nombre_completo: str

    #Profesor: area: str, cursos: list[str]
    #Alumno: promedio: int, cursos: dic -> key: curso, data: notas

# Sala de clases:  cursos: list[str], personas_presentes[Personas], capacidad


#Todas las entidades deben poder ser imprimibles

class Persona():
    rut = 0
    edad = 0
    genero = ""
    nombre = ""

    def __init__(self, rut, edad, genero, nombre):
        self.rut = rut
        self.edad = edad
        self.genero = genero
        self.nombre = nombre

    def __str__(self):
        texto_creado = "Nombre: " + self.nombre + "\nEdad: " + str(self.edad) + "\nrut: " + str(self.rut) + "\nObjeto tipo: " + str(Persona)

        return(texto_creado)
    
class Profesor(Persona):
    area = ""
    cursos = []

    def __init__(self, rut, edad, genero, nombre, area, cursos):

        Persona.__init__(self, rut, edad, genero, nombre)
        self.area = area
        self.cursos = cursos 

    def __str__(self):
        texto_creado = "Nombre: " + self.nombre + "\nEdad: " + str(self.edad) + "\nrut: " + str(self.rut) + "\nArea: " + self.area + "\nCursos: " + str(self.cursos) +  "\nObjeto tipo: " + str(Profesor)

        return(texto_creado)
        
class Alumno(Persona):
    promedio = 0
    cursos = dict()

    def __init__(self, rut, edad, genero, nombre, cursos, universidad):

        Persona.__init__(self, rut, edad, genero, nombre)
        self.cursos = cursos
        self.universidad = universidad

    def __str__(self):
        t = f'Nombre: {self.nombre} \nEdad: {self.edad}'
        return t

Lucas = Alumno(435345346, 12, "Hombre", "Lucas Pfeifer", ["IIC203", "ING2030", "MAT1010"], "PUC")
print(Lucas)

Jirafales = Profesor(3535253, 12, "Hombre", "Profesor Jirafales", "Fisica", ["IIC203", "ING2030", "MAT1010"])
print(Jirafales)


notas = {"IIC203": [6.8, 6.0, 6.1, 3.0], "ING2030": [6.8, 6.0, 6.1, 3.0]}

print(notas["IIC203"])


count_down = 10

for i in range(11):
    print(count_down)
    count_down -= 1
    time.sleep(1)
