import gurobipy as gp

# Create Model
m = gp.Model("Ejemplo")

# Variables
x = m.addVar(name="x")
y = m.addVar(name="y")

# Restriction
m.addConstr(x + y <= 10, "c1")
m.addConstr(x - y >= 3, "c2")

# Function Objective
m.setObjective(2 * x + y, gp.GRB.MAXIMIZE)

# Optimize
m.optimize()

# Result
for v in m.getVars():
    print(f"{v.varName} = {v.x}")
print(f"Obj: {m.objVal}")
