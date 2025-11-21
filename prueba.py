# Recorriendo una tupla en un diccionario
costos = {("T1", "Tarea1"): 9, ("T2", "Tarea2"): 7}
print(costos["T1", "Tarea1"])

Trabajador = "T2"
Tarea = "Tarea2"
print(costos[Trabajador, Tarea])

for (i, j), valor in costos.items():
    print(i, j, valor)

trabajadores = ["T6", "T2"]
Tareas = ["Tarea1", "Tarea2"]

# for i in Trabajadores:
#    for j in Tareas:
#        print(i, j, costos[i, j])

t1 = ("T1", "Tarea1")
print(t1)
print(t1[0])
print(t1[1])

# Tupla de 3 elementos
t2 = ("T1", "Tarea1", 10)
print(t2[2])
print(t2[1])
