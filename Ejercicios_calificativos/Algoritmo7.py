tareas = float(input("Ingrese la calificación de tareas: "))
examen_parcial = float(input("Ingrese la calificación del examen parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)
print(f"La calificación final del estudiante es: {calificacion_final:.2f}")