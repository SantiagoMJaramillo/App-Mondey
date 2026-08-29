# App de Registro de Ingresos y Gastos

Aplicación de consola en Python que permite llevar un control simple de
ingresos y gastos personales.

## Requisito - Momento 1: Nuevas Tecnologías

Este proyecto fue desarrollado como entrega del Momento 1, evidenciando:

- Menú interactivo controlado con un ciclo `while`.
- Uso de **listas** y **diccionarios** para almacenar los movimientos.
- Uso de **funciones** para separar la lógica del programa.
- Control de versiones con Git (ramas `main`, `develop`,
  `feature/registro`, `feature/balance`).

## Funcionalidades

1. **Registrar Ingreso**: agrega un ingreso con monto, categoría y descripción.
2. **Registrar Gasto**: agrega un gasto con monto, categoría y descripción.
3. **Ver Historial**: muestra todos los movimientos registrados en la sesión.
4. **Ver Balance**: calcula el total de ingresos, total de gastos y el saldo.
5. **Salir**: termina la ejecución del programa.

## Cómo instalar y ejecutar el proyecto (desde Visual Studio Code)

Requisitos: tener instalados Visual Studio Code, Python 3, Git, y la
extensión oficial de Python en VS Code.

1. **Clona el repositorio**: abre VS Code → `Ctrl+Shift+P` → escribe y
   selecciona `Git: Clone` → pega la URL
   `https://github.com/SantiagoMJaramillo/App-Mondey.git` → elige una
   carpeta destino → cuando termine, clic en "Open" para abrir el proyecto.

2. **Crea el entorno virtual**: `Ctrl+Shift+P` → escribe y selecciona
   `Python: Create Environment` → elige `Venv` → selecciona el intérprete
   de Python que tengas instalado. VS Code crea la carpeta `.venv`
   automáticamente (no viene incluida en el repositorio, se genera local
   en cada equipo).

3. **Selecciona el intérprete**: si no se activó solo, `Ctrl+Shift+P` →
   `Python: Select Interpreter` → elige el que dice `.venv`.

4. **Ejecuta el programa**: abre `App.py` en el editor y presiona el botón
   ▶ (Run Python File) arriba a la derecha, o clic derecho dentro del
   archivo → "Run Python File in Terminal". Este proyecto no usa
   librerías externas, así que no necesitas instalar nada adicional.

## Cómo ver y subir cambios (control de versiones)

Todo se hace desde el panel **Source Control** (ícono de la ramita en la
barra lateral izquierda, `Ctrl+Shift+G`):

- Los archivos modificados aparecen listados ahí.
- Clic en el `+` junto a cada archivo para agregarlos (equivalente a `git add`).
- Escribe un mensaje en el cuadro de texto superior y presiona el ✓ para
  confirmar el cambio (equivalente a `git commit`).
- Usa el botón "Sync Changes" o el menú `...` → "Push" para subir los
  cambios a GitHub (equivalente a `git push`).
- Para cambiar de rama, haz clic en el nombre de la rama actual, abajo a
  la izquierda de la ventana, y elige la rama a la que quieres moverte.

## Estructura de datos

Cada movimiento se guarda como un diccionario dentro de una lista:

```python
{
    "tipo": "ingreso",       # o "gasto"
    "monto": 5000.0,
    "categoria": "salario",
    "descripcion": "pago quincena"
}
```

## Estructura del proyecto