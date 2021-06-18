import random

############ BOT PROYECTO #################


# Things to do:

# Bonus: Ignorar faltas de tildes, ignorar mayusculas, puntos y comas,  b o v, s o z

# Introduccion

# Menu:

# Se introduce un frase, cualquier cosa, y se reconocen los keywords soportados se deplegan opciones #Bonus 2: Keywords

# Se despliegan las opciones de tematicas, ofreciendo las opciones para "hablar, conversar, preguntar etc."

# Usuario elige el tema que quiere tratar, Ej: Medicina

# Despliega tematicas dentro de la elegida, Ej: odontologia, neurologia, famarcologia, whatever.

# Tenemos un set de frases relevantes dentro de la tematica, de las cuales elegimos una al azar y la imprimimos.

#Recorrer arreglos y ciclos simples

print("Estes un bot de simulacion de conversaciones")


input_phrase = input("Ingrese su frase a continuacion: ")
#input_phrase = "Quiero saber de medicina o ciencia"

#lista = input_phrase.split(",")

#print(lista)

keywords = ["medicina", "gatos", "comida", "ciencia"] #Lista

#Medicina es el elemento 0 de la lista keywords -> Las opciones de medicina van a ser el elemento 0 en la lista opciones

opciones = [["Opciones de medicina 0", "Opciones de medicina 1"], ["Gatos siameses", "Alergia a gatos", "Gatos o perros"], ["Opciones de comida"], ["Opciones de ciencia"]]


#Acceder a un elemnto de la lista keywords[posicion de la palabra]

#Modo burdo

#if(keywords[0] in input_phrase): #medicina esta en la frase
    #print(opciones[0])
  

#if(keywords[1] in input_phrase):
    #print(opciones[1][0])
 

#if(keywords[2] in input_phrase):
    #print(opciones[2][0])



#if(keywords[3] in input_phrase):
    #print(opciones[3][0])

#Modo eficiente

print("Las opciones de conversacion son las siguientes:\n\n")

w = 1 

diccionario = {"gatos": -1, "ciencia": -1, "comida": -1, "medicina": -1}


for j in range(len(keywords)):
    if(keywords[j] in input_phrase):
        diccionario[keywords[j]] = w
        print(str(w) + " Opciones de " + keywords[j] + ":\n")
        w = w + 1
        for k in opciones[j]:
            print("  " + k)
        print("\n")    

opcion_elegida = input("¿De que tema quieres hablar:? \n" )

while(not opcion_elegida.isnumeric()):

    opcion_elegida = input("\n Porfavor ingrese un numero, non una letra: \n" )

while(int(opcion_elegida) > (w - 1) or int(opcion_elegida) < 1):    

    opcion_elegida = input("\n Porfavor ingrese un numero que este dentro de las opciones: \n" )



for keys in diccionario:
    if(int(opcion_elegida) == diccionario[keys]):
        opcion_elegida = keys 
        break



def load_list(category, lista, ruta):
    control = 0
    listas = open(ruta, "r")
    for linea in listas:
        if linea == category and control == 0:
            control = 1
        elif control == 1:
            lista.append(linea)
    listas.close()
    return lista

medicina =  load_list("medicina", [], "listas.txt")
gatos = load_list("gatos", [], "listas.txt")
ciencia = load_list("ciencia", [], "listas.txt")
comida = load_list("comida", [], "listas.txt")


if opcion_elegida == "ciencia":
    print(ciencia[random.randint(0, len(ciencia) -1)])

elif opcion_elegida == "medicina":
    print(medicina[random.randint(0, len(medicina) -1)])    

elif opcion_elegida == "gatos":
    print(gatos[random.randint(0, len(gatos) -1)])

elif opcion_elegida == "comida":
    print(comida[random.randint(0, len(comida) -1)])
















