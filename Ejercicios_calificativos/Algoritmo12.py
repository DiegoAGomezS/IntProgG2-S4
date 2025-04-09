precio_articulo = float(input("Ingrese el precio original del articulo: "))

ganancia60 = precio_articulo * 0.60
precio_venta = precio_articulo - ganancia60
print(f"El precio al que lo debes vender para ganar el 30% del precio original es {precio_venta:.2f}")