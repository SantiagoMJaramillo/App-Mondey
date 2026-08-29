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

## Cómo ejecutar el proyecto

Requisitos: tener Python 3 instalado.

```bash
python app.py
```

Luego sigue las instrucciones del menú en pantalla.

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

