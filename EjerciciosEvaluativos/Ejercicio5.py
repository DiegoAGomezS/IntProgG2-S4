numero = float(input("Ingrese cualquier numero: "))
porcentaje1 = float(input("Ingrese su porcentaje: "))

porcentaje2 = porcentaje1 / 100
resultado = numero * porcentaje2

print(f'El {porcentaje1} % de {numero} es: {resultado:.2f}')