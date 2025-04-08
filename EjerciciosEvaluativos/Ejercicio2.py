print("Ingrese tres valores númericos para inicar el programa")

a = float(input())
b = float(input())
c = float(input())

suma = a + b
multiplicacion = suma * c
resultado = multiplicacion / 2

print(f"Su resultado es: {resultado:.2f}")
print(f'({a} + {b}) = {suma}')
print(f'{suma} * {c} = {multiplicacion}')
print(f'{multiplicacion} / 2 = {resultado}')