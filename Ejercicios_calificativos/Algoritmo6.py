precio1 = float(input(" Ingrese el precio del primer producto: "))
precio2 = float(input(" Ingrese el precio del segundo producto: "))
precio3 = float(input(" Ingrese el precio del tercer producto: "))

subtotal = precio1 + precio2 + precio3
Iva = subtotal * 0.15
total = subtotal + Iva

def ftexto(texto): 
    return f"{texto:<10}"

print("\n----- FACTURA -----")
print(f"{ftexto("Subtotal")} {subtotal:>6}")
print(f"{ftexto("IVA:")} {Iva:>6}")
print(f"{ftexto("Total:")} {total:>6}")