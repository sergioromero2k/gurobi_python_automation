## Chuleta de Comandos Esenciales de **Gurobi**

Esta guía cubre los pasos básicos para construir y resolver un modelo de **Programación Lineal (PL)** o **Programación Entera Mixta (PEM)**.

---

### 1.  Inicialización y Setup

| Comando | Descripción |
|----------|--------------|
| `import gurobipy as gp` | Importa la librería con el alias común `gp`. |
| `from gurobipy import GRB` | Importa las constantes clave (tipos, estados). |
| `m = gp.Model("Nombre_Modelo")` | Crea el objeto modelo. |

---

### 2. Definición de Variables

| Tipo de Variable | Dominio | Sintaxis |
|------------------|----------|-----------|
| **Continua (por defecto)** | $\mathbb{R}$ | `x = m.addVar(name="x")` |
| **Binaria** | $\{0, 1\}$ | `y = m.addVar(vtype=GRB.BINARY, name="y")` |
| **Entera** | $\mathbb{Z}$ | `z = m.addVar(vtype=GRB.INTEGER, name="z")` |
| **Múltiples (usando índices)** | $\mathbb{R}^N$ | `x = m.addVars(3, name="x_")` |
| **Múltiples (con claves)** | $\mathbb{R}^I$ | `y = m.addVars(['A', 'B'], vtype=GRB.BINARY, name="y")` |

---

### 3.  Función Objetivo

| Comando | Descripción |
|----------|-------------|
| `m.setObjective(expresión, GRB.MAXIMIZE)` | Maximiza la expresión lineal. |
| `m.setObjective(expresión, GRB.MINIMIZE)` | Minimiza la expresión lineal. |

> **Tip:** Usa `gp.quicksum()` para sumas grandes — es más eficiente que `sum()` de Python.  
> Ejemplo: `gp.quicksum(x[i] for i in range(3))`

---

### 4.  Definición de Restricciones

| Comando | Operador | Descripción |
|----------|-----------|-------------|
| `m.addConstr(expresión <= valor, "c1")` | ≤ | Restricción de menor o igual. |
| `m.addConstr(expresión >= valor, "c2")` | ≥ | Restricción de mayor o igual. |
| `m.addConstr(expresión == valor, "c3")` | = | Restricción de igualdad. |
| `m.addConstrs(...)` | - | Añade múltiples restricciones de golpe. |

📘 **Ejemplo:**
```python
m.addConstrs(gp.quicksum(x[i] for i in range(3)) <= 10 for j in range(5))
```