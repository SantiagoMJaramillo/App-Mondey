# Aplicación de Registro de Ingresos y Gastos
# Momento 1 - Nuevas Tecnologías

movimientos = []

def mostrar_menu():
    print("\n== APP DE INGRESOS Y GASTOS ==")
    print("1. Registrar ingresos")
    print("2. Registrar gasto")
    print("3. Ver Historial de movimientos")
    print("4. Ver saldo actual")
    print("5. Salir")

def pedir_monto():
    while True:
        entrada = input("Ingrese el monto")
        try:
            monto = float(entrada)
            if monto <= 0:
                print("El monto debe ser mayor a 0. Intente de nuevo.")
                continue
            return monto
        except ValueError:
            print("Debe ingresar una cantidad valido. Intente de nuevo.")

def registrar_ingreso():
    print("\n- Registrar Ingreso-")
    monto = pedir_monto()
    categoria = input("Indique la categoría (ej: salario, ventas, otro): ")
    descripcion = input("Indique una descripcion del ingreso: ")
    movimiento = {
        "tipo": "ingreso",
        "monto": monto,
        "categoria": categoria,
        "descripcion": descripcion,
    }
    movimientos.append(movimiento)
    print(f"Ingreso de ${monto:.2f} registrado con éxito.")


def registrar_gasto():
    
    print("\n-Registrar Gasto-")
    monto = pedir_monto()
    categoria = input("Categoría (ej: comida, transporte, otro): ")
    descripcion = input("Indique una descripcion del gasto: ")

    movimiento = {
        "tipo": "gasto",
        "monto": monto,
        "categoria": categoria,
        "descripcion": descripcion,
    }
    movimientos.append(movimiento)
    print(f"Gasto de ${monto:.2f} registrado con éxito.")