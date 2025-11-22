### Cómo descargar Gurobi
1. Ve a la web oficial: https://www.gurobi.com/downloads/
2. Crea una cuenta gratuita de usuario.
3. Descarga el instalador correspondiente a tu sistema operativo:
* Windows (.exe)
* macOS (.pkg)
* Linux (.tar.gz)
4. Instala Gurobi siguiendo las instrucciones del instalador.

### Licencias de Gurobi

Tienes varias opciones:
#### Licencia Académica (gratuita)
Si eres estudiante o investigador:adaadad
* Es gratis para uso académico.
* Solo necesitas una dirección de correo institucional (.edu, .univ, etc.)

**Pasos**
* Regístrate con tu correo institucional en: https://www.gurobi.com/academia/academic-program-and-licenses/
* Solicita una **Academic License** (puede ser local o en la nube).
* Te enviarán un license key (archivo gurobi.lic o clave).

Instalas la licencia con:
```
grbgetkey X-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```
### Instalación del paquete Python
```py
pip install gurobipy

# Verifica la instalación
import gurobipy
print(gurobipy.gurobi.version())
```