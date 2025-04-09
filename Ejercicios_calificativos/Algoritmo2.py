print("A continuación proporcione los siguientes datos")
varones = int(input("Cantidad de varones en un aula: "))
mujeres = int(input("Cantidad de mujeres en un aula: "))

alumnos = varones + mujeres
porcentaje_varones = (varones /alumnos) * 100
porcentaje_mujeres = (mujeres /alumnos) * 100

print(f"Porcentaje de varones: {porcentaje_varones:.2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")