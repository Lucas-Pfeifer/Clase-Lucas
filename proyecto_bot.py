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


medicina = [
"Cuando te sonrojas tambien lo hace el revestimiento de tu estomago.",
"Tus ojos son siempre del mismo tamaño, pero tu nariz y tus orejas nunca paran de crecer.",
"Tu nariz puede recordar hasta 50.000 olores. Asimismo, la mujer tiene mejor olfato que el hombre.",
"Una persona con gripe se vuelve socialmente mas activa. Este es un comportamiento del virus para tratar de propagarse.",
"Siete segundos es lo que demora la comida en ir de la boca al estomago.",
"Se estima que en el cuerpo tenemos unos 96,000 kilometros de vasos sanguineos"]

comida = [
"El amor por el cafe esta en tus genes",
"Una mazorca siempre tiene un numero par de granos",
"Las zanahorias no siempre fueron de color naranja",
"Las setas contienen quitina (al igual que los insectos)",
"El sandwich fue inventado durante un juego de cartas",
"La pizza hawaiana fue inventada en Canada"]

ciencia = [
"La mariposa mas grande del mundo tiene un tamaño de casi medio metro.",
"Mas hombres que mujeres son daltonicos.",
"Se robaron el cerebro de Albert Eistein",
"Las jirafas tienen la lengua azul",
"Las hormigas son capaces de transportar objetos 50 veces su propio peso corporal",
"Los humanos no pueden sentir sabor sin saliva"]

gatos = [
"Los gatos se comunican a traves de vocalizaciones y entre ellas la mas popular es el maullido. Tambien, cabe mencionar que, junto con el perro, son los animales mas populares para escoger como mascota, debido a su adaptabilidad y caracteristicas.",
"Tienen una flexibilidad y agilidad impresionante, pueden saltar desde mas de 3 metros de altura.",
"Los gatos pueden rotar sus orejas 180 grados.",
"Debido a su naturaleza nocturna, los gatos suelen ser mucho mas hiperactivos en la tarde.",
"En la raza de gato mas grande, el macho promedio pesa aproximadamente 9 kilos.",
"Los gatos domesticos pasan cerca del 70 por ciento del dia durmiendo, y 15 por ciento del dia acicalandose.",
"Tienen uno de los sistemas sensoriales mas sofisticados del mundo."]

if opcion_elegida == "ciencia":
    print(ciencia[random.randint(0, len(ciencia) -1)])

elif opcion_elegida == "medicina":
    print(medicina[random.randint(0, len(medicina) -1)])    

elif opcion_elegida == "gatos":
    print(gatos[random.randint(0, len(gatos) -1)])

elif opcion_elegida == "comida":
    print(comida[random.randint(0, len(comida) -1)])

















