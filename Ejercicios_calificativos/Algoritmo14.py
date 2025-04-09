presupuesto_total = float(input("Ingrese el presupuesto total: "))

urgencias = presupuesto_total * 0.37
pediatria = presupuesto_total * 0.42
traumatologia = presupuesto_total * 0.21

def ftexto(texto): 
    return f"{texto:<10}"

print(f"{ftexto("Presupuesto para urgencias:")} {urgencias:>6}")
print(f"{ftexto("Presupuesto para pediatría:")} {pediatria:>6}")
print(f"{ftexto("Presupuesto para trumatología:")} {traumatologia:>6}")