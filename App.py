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
        entrada = input("Ingrese el monto: ")
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

def ver_historial():
    print("\n-- Historial de Movimientos --")
    if not movimientos:
        print("Aún no hay movimientos.")
        return
    for i, mov in enumerate(movimientos, start=1):
        signo = "+" if mov["tipo"] == "ingreso" else "-"
        print(
            f"{i}. [{mov['tipo'].upper()}] {signo}${mov['monto']:.2f} "
            f"| Categoría: {mov['categoria']} | {mov['descripcion']}"
        )

def ver_balance():
    """Calcula y muestra el balance total (ingresos - gastos)."""
    total_ingresos = sum(m["monto"] for m in movimientos if m["tipo"] == "ingreso")
    total_gastos = sum(m["monto"] for m in movimientos if m["tipo"] == "gasto")
    balance = total_ingresos - total_gastos
    print("\n-- Balance Actual --")
    print(f"Total ingresos: ${total_ingresos:.2f}")
    print(f"Total gastos:   ${total_gastos:.2f}")
    print(f"Balance:        ${balance:.2f}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción del 1 al 5: ")
        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            registrar_gasto()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            ver_balance()
        elif opcion == "5":
            print("Fin de la operacion")
            break
        else:
            print("Opción no válida. Elija un número del 1 al 5.")

if __name__ == "__main__": main()