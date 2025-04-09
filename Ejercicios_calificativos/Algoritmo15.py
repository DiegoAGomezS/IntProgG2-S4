nombre_trabajador = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio que cobra por hora: "))

sueldo_bruto = horas_trabajadas * precio_por_hora

descuento_renta = sueldo_bruto * 0.05

salario_neto = sueldo_bruto - descuento_renta

def ftexto(texto): 
    return f"{texto:<10}"

print(f"{ftexto("Nombre del trabajador:")} {nombre_trabajador:>6}")
print(f"{ftexto("Sueldo bruto:")} ${sueldo_bruto:>6}")
print(f"{ftexto("Descuento por renta:")} ${descuento_renta:>6}")
print(f"{ftexto("Salario a pagar:")} ${salario_neto:>6}")