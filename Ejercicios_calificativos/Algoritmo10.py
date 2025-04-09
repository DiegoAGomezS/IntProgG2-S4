presion = float(input("Ingrese la presión en atomósferas: "))
volumen = float(input("Ingrese el volumen en litros: "))
temperatura = float(input("Ingrese la temperatura en farenheit: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f"La masa total del objeto es: {masa:.2f}")