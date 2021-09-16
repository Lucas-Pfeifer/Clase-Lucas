class Quiosco:



    def __init__(self):
        self.productos = {}
    
    def registrar_venta(self, Producto):
        pass
        

    def recibir_pedido(self, path):
        recibidos = open(path, "r", encoding='UTF-8').readlines()
        primera_linea = True
        for line in recibidos: 
            if primera_linea:
                primera_linea = False
            else:
                datos = line.strip().split(";")
                Nuevo_Producto = Producto(datos[1], datos[2], datos[0], datos[3], self)
                self.productos[Nuevo_Producto.id] = Nuevo_Producto
   
    def mostrar_stock(self, carro): 
        for key in self.productos:
            aux = 0
            if key in carro:
                aux = carro[key]
            print(f" Nombre: {self.productos[key].nombre}\n ID: {self.productos[key].id} \n Precio: {self.productos[key].precio}\n Cantidad: {self.productos[key].stock - aux}")
            print(f"----------------------------------------------------------------------------------------------")
            
    def validar(self, id):
        if id in self.productos:
            return True  
        return False          


    def cambiar_stock(self, productoId, cantidad):
        pass

class Producto:

    def __init__(self, nombre, precio, id, stock, quiosco):
        self.nombre = nombre
        self.comprado = int(precio)
        self.precio = int(precio)*1.25
        self.id = id
        self.quiosco = quiosco
        self.stock = int(stock)

    def validar(self, cantidad):
         
        if cantidad > self.stock:
            return False
            
        return True


    def compra(self, cantidad):
        self.stock -= cantidad
    




    
