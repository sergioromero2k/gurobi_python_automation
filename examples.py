import gurobipy as gp
from gurobipy import GRB

m = gp.Model("Ejemplo_addVar")

# Formas de definir variables en gurobi
# Variables individuales
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2")
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3")

print("Tipo de x1: ", type(x1))  # Tipo de x1: <class 'gurobi.Var'>

N = [1, 2, 3]  # Índices

# Crea las variables x[1], x[2], x[3]
y = m.addVars(N, vtype=GRB.CONTINUOUS, name="y")
print("Tipo de y: ", type(y))
print("Acceso a y_1:", y[1])

# Crear un vector de 3 variables: x[0], x[1], x[2]
x_m = m.addMVar(shape=3, vtype=GRB.CONTINUOUS, name="x")
print("Tipo de x_m:", type(x_m))
print("Acceso a x_m:", x_m)

# Formas de definir Función Objectivo en gurobi


