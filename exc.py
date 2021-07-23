# Clase Persona -> Alumno ; Profesor. Sala de Clase


#Persona: rut: int, edad: int, genero: str, nombre_completo: str

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
    
class Profesor(Persona):
    area = ""
    cursos = []

    def __init__(self, rut, edad, genero, nombre, area, cursos):

        Persona.__init__(self, rut, edad, genero, nombre)
        self.area = area
        self.cursos = cursos 

class Alumno(Persona):
    promedio = 0
    cursos = dict()

    def __init__(self, rut, edad, genero, nombre, promedio, cursos):

        Persona.__init__(self, rut, edad, genero, nombre)
        self.promedio = promedio
        self.cursos = cursos



Lucas = Alumno(435345346, 12, "Hombre", "Lucas Pfeifer", 6.9, ["IIC203", "ING2030", "MAT1010"])
print(Lucas)