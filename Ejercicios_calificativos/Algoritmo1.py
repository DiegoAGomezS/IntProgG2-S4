prestamo = 10000.00
tasa_interes = 0.27
tiempo = int(input("Ingrese el tiempo (En años) que posee para pagar el prestamo"))

interes = prestamo * tasa_interes * tiempo
print(f"El interes total en base al tiempo establecido es {interes:.2f}")

total = prestamo + interes
print(f"Su total a pagar contando los intereses es {total:.2f}")