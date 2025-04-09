nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

precio_final = precio * (1-(descuento / 100))

def ftexto(nombre_producto): 
    return f"{nombre_producto:>10}"

print(f"{ftexto(nombre_producto):>10} {precio_final:>6}")