# Gurobi and Python
Este documento resume cómo formular y resolver problemas clásicos de Investigación Operativa utilizando Gurobi y Python, tal como se enseña en cursos universitarios de Optimización, Programación Lineal y Programación Entera. Incluye ejemplos, sintaxis básica, fragmentos de código y problemas típicos.

## 1. Instalación y configuración
```bash
pip install gurobipy
```
En Python:
```py
import gurobipy as gp
from gurobipy import GRB
```
**Asegúrate de tener tu licencia académica**, gratuita para estudiantes.

## 2. Estructura general de un modelo en Gurobi
```py
model = gp.Model("nombre_del_modelo")

# 1. Crear variables
x = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="x")

# 2. Crear restricciones
model.addConstr(x <= 10, "restriccion1")

# 3. Función objetivo
model.setObjective(5 * x, GRB.MAXIMIZE)

# 4. Optimizar
model.optimize()
```
## 3. Variables en Gurobi
#### Tipos de variable:
| Tipo             | Descripción            |
| ---------------- | ---------------------- |
| `GRB.CONTINUOUS` | Variable continua      |
| `GRB.INTEGER`    | Variable entera        |
| `GRB.BINARY`     | Variable binaria (0/1) |

```py
x = model.addVar(vtype=GRB.INTEGER, name="x")
y = model.addVar(vtype=GRB.BINARY, name="y")
```

## 4. Restricciones
Forma general:
```py
model.addConstr(expr, name)
```
Ejemplos:
```py
model.addConstr(2*x + 3*y <= 40, "capacidad")
model.addConstr(x - y >= 0, "relacion")
```
## 5. Función Objetivo
```py
model.setObjective(3*x + 4*y, GRB.MAXIMIZE)
# o minimización:
model.setObjective(2*x + y, GRB.MINIMIZE)
```

## 6. Obtener resultados
```py
model.optimize()

print("Valor óptimo:", model.objVal)
print("x =", x.X)
print("y =", y.X)
```