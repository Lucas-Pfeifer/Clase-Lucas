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

for j in range(len(keywords)):
    if(keywords[j] in input_phrase):
        print(str(w) + " Opciones de " + keywords[j] + ":\n")
        w = w + 1
        for k in opciones[j]:
            print("  " + k)
        print("\n")    

opcion_elegida = input("¿De que tema quieres hablar:? \n" )

while(int(opcion_elegida) > (w - 1) or int(opcion_elegida) < 1): 

    opcion_elegida = input("\n Porfavor ingrese un numero que este dentro de las opciones: \n" )


#Como identificar si una variable es de tipo string o de tipo numero... 

#Por hacer, IF de seleccion, respuestas del bot para que parezca conversacion real








