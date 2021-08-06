lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Funcion recibe 2 argumentos, el elemento a agregar y su posicion
#Tip: len(lista) entrega el tamaño de la lista que estas trabajando
# Sean A y B listas, A + B sera la union de ambas.

# lista[0] = 80
# temporal = lista[1]

#Ojo a los casos limites, ej estas agregando en la ultima posicion y no hay nada que desplazar o estas agregando en una posicion que no existe

def insert(data, position, array):
    if position == len(array) -1:
        array.append(data)
        return array

    elif position == 0:
        A = [data]
        B = A + array
        return B
    
    elif position >= len(array):
        print("Index out of range!")
        return array
        
    else:
        A = array[0:position]
        B = array[position:]
        A.append(data)
        C = A + B
        return C
    



new_list = insert(11, 99, lista)

print(new_list)


