edad_actual = int(input("Ingrese su edad actual: "))

edad_5anios = edad_actual + 5
edad_10anios = edad_actual + 10
edad_20anios = edad_actual + 20

def ftexto(texto): 
    return f"{texto:<10}"

print(f"{ftexto("Edad en 5 años:")} {edad_5anios:>6}")
print(f"{ftexto("Edad en 10 años:")} {edad_10anios:>5}")
print(f"{ftexto("Edad en 20 años")} {edad_20anios:>6}")