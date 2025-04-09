tiempo_lunes = float(input("Ingrese el tiempo en horas de su ruta el lunes: "))
tiempo_miercoles = float(input("Ingrese el tiempo en horas de su ruta el miercoles: "))
tiempo_viernes = float(input("Ingrese el tiempo en horas de su ruta el viernes: "))

tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3
print(f"Su tiempo promedio de recorrido a la semana es: {tiempo_promedio:.2f}")