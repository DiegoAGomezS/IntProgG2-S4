cuenta = float(input("Ingrese la cantidad total de la cuenta a pagar: "))
porcentaje_propina = float(input("Ingrese el porcentaje del descuento"))

propina = (porcentaje_propina / 100) * cuenta
total_pagar = propina + cuenta

print(f"La propina es: ${propina:.2f}")
print(f"El total a pagar incluyendo la propina es: ${total_pagar:.2f}")