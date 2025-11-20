## Gurobi

### Conceptos Clave de Gurobi
| Concepto                         | Descripción                                            | Cómo se usa en Gurobi                              |
| -------------------------------- | ------------------------------------------------------ | -------------------------------------------------- |
| **Modelo (Model)**               | El contenedor principal del problema de optimización.  | `Model()` o `grb.Model()`                          |
| **Variables (Variables)**        | Las incógnitas que Gurobi debe determinar.             | `model.addVar()` o `model.addVars()`               |
| **Restricciones (Constraints)**  | Reglas o limitaciones que deben cumplir las variables. | `model.addConstr()` o `model.addConstrs()`         |
| **Función Objetivo (Objective)** | Expresión matemática a minimizar o maximizar.          | `model.setObjective()`                             |
| **Optimizar (Optimize)**         | Método que resuelve el modelo.                         | `model.optimize()`                                 |
| **Atributos (.X, .ObjVal)**      | Propiedades de variables y modelo tras optimizar.      | `.X` (valor variable), `.ObjVal` (valor óptimo FO) |

### Chuleta Rápida para Automatización (Python)
Aquí se asume que has importado la librería Gurobi: ``import gurobipy as grb``.

#### 1. Inicialización y Variables

| Tarea                         | Código Gurobi                                                   | Notas                                                                                 |
|------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **Inicializar Modelo**           | `m = grb.Model("MiModelo")`                                      | Es el primer paso.                                                                    |
| **Añadir una Variable**          | `x = m.addVar(vtype=grb.GRB.CONTINUOUS, name="x")`               | Tipos: `CONTINUOUS`, `BINARY`, `INTEGER`.                                             |
| **Añadir Múltiples Variables**   | `y = m.addVars(3, vtype=grb.GRB.INTEGER, name="y")`              | Crea `y_0, y_1, y_2`. Para indexación compleja se usa diccionario: `m.addVars(items, name="z")`. |

#### 2. Restricciones y Objetivo

| Tarea                                   | Código Gurobi                                                          | Notas                                                             |
|-----------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| **Añadir una Restricción**                  | `m.addConstr(x + 2*y[0] <= 10, name="R1")`                              | Se usa la sintaxis de Python para desigualdades/igualdades.       |
| **Añadir Múltiples Restricciones (auto)**   | `m.addConstrs((x + y[i] >= 2 for i in range(3)), name="Minimo")`        | Útil para generar conjuntos de restricciones.                     |
| **Definir Objetivo**                        | `m.setObjective(3*x + y[1], grb.GRB.MAXIMIZE)`                          | Tipos: `MAXIMIZE` o `MINIMIZE`.                                   |

#### 3. Solución

| Tarea                 | Código Gurobi                                                   | Notas                                   |
|----------------------|------------------------------------------------------------------|------------------------------------------|
| **Optimizar**            | `m.optimize()`                                                   | Resuelve el modelo.                      |
| **Verificar Solución**   | `if m.status == grb.GRB.OPTIMAL: print("Solución Óptima encontrada.")` | Usa el atributo `.status`.               |
| **Obtener Valor**        | `print(f"x = {x.X}")`                                            | Usa el atributo `.X` para el valor.      |
| **Valor de la FO**       | `print(f"Objetivo = {m.ObjVal}")`                                | Valor óptimo de la función objetivo.     |
