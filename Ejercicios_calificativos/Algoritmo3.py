salario = float(input("Ingrese su salario actual: "))
inc_salario = salario / 0.08

print(f"Debido a su desempeño usted ahora posee un salario de {inc_salario:.2f}")

cantidad_producto = int(input("Ingrese la cantidad de productos: "))
precio_uni = float(input("Ingrese el precio unitario: "))
descuento = (cantidad_producto * precio_uni) * 0.025

print(f"Su compra en base al descuento por su trabajo es {descuento}")