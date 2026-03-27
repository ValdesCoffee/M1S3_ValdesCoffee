def calcular_estadisticas(inventario):
    if not inventario:
        return None

    unidades_totales = 0
    valor_total = 0
    mas_caro = inventario[0]
    mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales = unidades_totales + producto["cantidad"]
        valor_total = valor_total + producto["precio"] * producto["cantidad"]
        if producto["precio"] > mas_caro["precio"]:
            mas_caro = producto
        if producto["cantidad"] > mayor_stock["cantidad"]:
            mayor_stock = producto

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (mas_caro["nombre"], mas_caro["precio"]),
        "producto_mayor_stock": (mayor_stock["nombre"], mayor_stock["cantidad"]),
    }


def mostrar_estadisticas(inventario):
    stats = calcular_estadisticas(inventario)
    if stats is None:
        print("El inventario esta vacio, no hay estadisticas.")
        return

    nombre_caro, precio_caro = stats["producto_mas_caro"]
    nombre_stock, cant_stock = stats["producto_mayor_stock"]

    print("\nEstadisticas del inventario:")
    print("Unidades totales: " + str(stats["unidades_totales"]))
    print("Valor total: " + str(round(stats["valor_total"], 2)))
    print("Producto mas caro: " + nombre_caro + " (" + str(precio_caro) + ")")
    print("Mayor stock: " + nombre_stock + " (" + str(cant_stock) + " unidades)")

    print("\nSubtotales por producto:")
    for producto in inventario:
        subtotal = producto["precio"] * producto["cantidad"]
        print(producto["nombre"] + ": " + str(round(subtotal, 2)))
