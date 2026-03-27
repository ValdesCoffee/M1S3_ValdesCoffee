def agregar_producto(inventario, nombre, precio, cantidad):
    if buscar_producto(inventario, nombre) is not None:
        print("El producto " + nombre + " ya existe.")
        return False
    producto = {"nombre": nombre.strip(), "precio": float(precio), "cantidad": int(cantidad)}
    inventario.append(producto)
    print("Producto " + nombre + " agregado correctamente.")
    return True


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario esta vacio.")
        return
    print("\nNombre |⁕| Precio |⁕| Cantidad")
    print("-" * 35)
    for producto in inventario:
        print(producto["nombre"] + " | " + str(producto["precio"]) + " | " + str(producto["cantidad"]))
    print("-" * 35)
    print("Total de productos: " + str(len(inventario)))


def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.strip().lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print("Producto " + nombre + " no encontrado.")
        return False
    if nuevo_precio is not None:
        producto["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        producto["cantidad"] = int(nueva_cantidad)
    print("Producto " + nombre + " actualizado.")
    return True


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print("Producto " + nombre + " no encontrado.")
        return False
    inventario.remove(producto)
    print("Producto " + nombre + " eliminado.")
    return True
