nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))

edad_actual = anio_actual - nacimiento
edad_diez_anios_despues = edad_actual + 10

print(f"Usted nacio en el año de {nacimiento} y su edad actual es {edad_actual}")
print(f"Dado que actualmente es el año {anio_actual} dentro de 10 años tendrás {edad_diez_anios_despues}")