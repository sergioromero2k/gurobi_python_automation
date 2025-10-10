import gurobipy as gp

# Crear Modelo
m = gp.Model("Ejemplo")

# Variables
x = m.addVar(name="x")
y = m.addVar(name="y")

# Restricciones
m.addConstr(x + y <= 10, "c1")
m.addConstr(x - y >= 3, "c2")

# Función objetivo
m.setObjective(2 * x + y, gp.GRB.MAXIMIZE)

# Optimizar
m.optimize()

# Resultado
for v in m.getVars():
    print(f"{v.varName} = {v.x}")
print(f"Obj: {m.objVal}")
