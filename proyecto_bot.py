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

opciones = [["Opciones de medicina 0", "Opciones de medicina 1"], ["Opciones de gatos"], ["Opciones de comida"], ["Opciones de ciencia"]]

#Acceder a un elemnto de la lista keywords[posicion de la palabra]

#Modo burdo

if(keywords[0] in input_phrase): #medicina esta en la frase
    #print(opciones[0])
    pass

if(keywords[1] in input_phrase):
    #print(opciones[1][0])
    pass

if(keywords[2] in input_phrase):
    #print(opciones[2][0])
    pass


if(keywords[3] in input_phrase):
    #print(opciones[3][0])
    pass

#Modo eficiente

#Ciclos y recorrer

i = 0 #Variable de control


while(i < len(keywords)):

    i = i + 1

for i in range(10):
    #instrucciones
