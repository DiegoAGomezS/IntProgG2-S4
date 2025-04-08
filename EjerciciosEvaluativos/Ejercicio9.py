print ("""Los siguientes nombres de variables están mal escritos o no siguen una convención
clara. Corrígelos utilizando camelCase o snake_case, según se indique.""")

a = "nombrepersona → camelCase"
b = "EdadPersona → snake_case"
c = "TotalPrecio → camelCase"
d = "numero-de-telefono → snake_case"
e = "DireccionEmail → camelCase"

print(f"{a} → nombrePersona")
print(f"{b} → edad_persona")
print(f"{c} → totalPrecio")
print(f"{d} → numero_de_telefono")
print(f"{e} → direccionEmail")