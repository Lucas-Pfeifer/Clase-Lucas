from identidades import Quiosco, Producto

# instanciamos el Quiosco
Mi_Tienda = Quiosco()
Mi_Tienda.recibir_pedido("productos.txt")

carro = dict()
comprando = True
#   COMENZAMOS A AGREGAR PRODUCTOS AL CARRO
while comprando:

    Mi_Tienda.mostrar_stock(carro)
    Cantidad_No_Valida = True
    while Cantidad_No_Valida:
        id_producto = str(
            input("Ingresa el ID del producto que desea comprar: "))
        cantidad_producto = int(
            input("Ingresa la cantidad del producto ya seleccionado: "))
        # extra = 0   variable auxiliar , creada por si el cliente vuelve a comprar más del mismo producto
        # if carro[comprar_producto]:
        #    extra = cantidad_producto + carro[comprar_producto]
        # + extra (si quiero considerar los productos ya en el carro )
        if Mi_Tienda.validar(id_producto) and Mi_Tienda.productos[id_producto].validar(cantidad_producto):
            carro[id_producto] = cantidad_producto
            Cantidad_No_Valida = False
            print("Agregado al carro")
        else:
            print("Ingresa una cantidad / id valido!")
    # criterio de salida
    answ = int(input("Desea comprar otro producto? (1 SI ; NO 2): "))
    if answ == 2:
        comprando = False

# TERMINAMOS DE AGREGAR PRODUCTOS AL CARRO


for id in carro:
    print(f"Comprando {carro[id]}  {Mi_Tienda.productos[id].nombre} ")
    Mi_Tienda.productos[id].compra(carro[id])

if Respuesta:
    print("Compra exitosa")
if not Respuesta:
    print("Compra fallida")

Mi_Tienda.mostrar_stock()
