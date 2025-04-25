print("Tienda Riwi, Bienvenid@s")
print("1. Comprar")
print("2. Salir")

try:
    Opcion=int(input("Selecciona una opcion: "))
except ValueError:
    print("Error, Debes ingresar un numero entero.")
if Opcion == 1:
    producto=str (input("Ingresa el producto que deseas comprar: ")) #Arreglar
    print(f"Elegiste el producto: {producto}")
elif Opcion == 2:
    print("Gracias por visitarnos")

def solicitar_solo_numeros():
    while True:
precio_producto=input("Ingresa el precio de tu producto: ")
        if precio_producto.isalnum():
            print                                 #Arreglar
            break                                
        else :print("Ingresa una cantidad valida")
solicitar_solo_numeros()

cantidad_productos=int(input("Cuantas unidades deseas?: "))
precio_total= precio_producto*cantidad_productos
descuento_producto=float(input("Ingresa el descuento del producto: "))  #prueba 1
precio_final= precio_total/descuento_producto
print(f"El precio del producto es: {precio_final}")

#ARREGLAR

precio_producto=input("Ingresa el precio de tu producto: ")
cantidad_productos=int(input("Cuantas unidades deseas?: "))
precio_total=int (cantidad_productos*precio_producto)
descuento_producto=float(input("Ingresa el descuento del producto: "))  #prueba 2
precio_final=int (precio_total/descuento_producto)
print(f"El precio del producto es: {precio_final}")
