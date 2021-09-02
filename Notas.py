Mi_lista = [1,2,3,4]
#for i in Mi_lista[0:3]:
    #valor_1 = Mi_lista.index(i)
    #print(Mi_lista)
    #print(f'El valor del iterando es: {valor_1}')




#Mi_dict = {"key_1":21, 405:"value_2"}
#for u in Mi_dict:
    #valor = Mi_dict[u]
    #print(f"La key es: {u} y su valor es: {valor}")


def imprimiendo(iterable, numero):
    var = type(iterable)
    #test = []
    #Se puede comparar con type(test)
    if len(iterable) <= numero:
        print("No se puede realizar la operacion")
    elif var == list:
        for i in iterable[0:numero]:
            print(i)
    else:
        contador = 0
        for key in iterable:
            print(f"Key: {key}  Valor: {iterable[key]}")
            contador += 1 
            if contador == numero:
                break
        
Mi_dict = {"key_1":21, 405:"value_2"}
imprimiendo(Mi_lista, 5)



            

            
