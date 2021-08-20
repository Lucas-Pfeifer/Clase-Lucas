import time

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
    cursos = []

    def __init__(self, rut, edad, genero, nombre, cursos, universidad, notas):

        Persona.__init__(self, rut, edad, genero, nombre)
        self.cursos = cursos
        self.universidad = universidad
        self.notas = notas
        self.Promedio()
        print(self.promedio)
        #self.promedio = #Llamar a funcion de promedio que actualiza este

    def __str__(self):
        t = f'Nombre: {self.nombre} \nEdad: {self.edad}'
        return t

    def Promedio(self):
        self.notas
        cantidad_notas = 0
        suma_notas = 0
        for i in self.notas:
            for j in self.notas[i]:
                suma_notas += j
                cantidad_notas += 1
        self.promedio = suma_notas / cantidad_notas 





notas = {"IIC203": [6.8, 6.0, 6.1, 3.0], "ING2030": [6.8, 6.0, 6.1, 3.0], "diplomado_danza": [5.4, 3.2, 4.3]}

Lucas = Alumno(435345346, 12, "Hombre", "Lucas Pfeifer", ["IIC203", "ING2030", "MAT1010"], "PUC", notas)

Jirafales = Profesor(3535253, 12, "Hombre", "Profesor Jirafales", "Fisica", ["IIC203", "ING2030", "MAT1010"])

# diccionario -> [(key, value), ..., (key, value)]

for j in notas:
    print(j, notas[j])
