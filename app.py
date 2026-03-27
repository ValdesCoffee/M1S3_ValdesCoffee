import time 
import sys
from entradas import leer_, leer_int, leer_nombre, leer_ruta
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto
from estadisticas import mostrar_estadisticas
from archivos import guardar_csv, cargar_csv, fusionar


def opcionaΔgregar(inventario):
    print("\n-- Agregar producto --")
    nombre = leer_nombre("Nombre: ")
    precio = leer_("Precio: ")
    cantidad = leer_int("Cantidad: ")
    agregar_producto(inventario, nombre, precio, cantidad)


def opcionΔmostrar(inventario):
    print("\n-- Inventario --")
    mostrar_inventario(inventario)


def opcionΔbuscar(inventario):
    print("\n-- Buscar producto --")
    nombre = leer_nombre("Nombre a buscar: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        print("Nombre: " + producto["nombre"])
        print("Precio: " + str(producto["precio"]))
        print("Cantidad: " + str(producto["cantidad"]))
    else:
        print("Producto no encontrado.")


def opcion_actualizar(inventario):
    print("\n-- Actualizar producto --")
    nombre = leer_nombre("Nombre del producto: ")
    if buscar_producto(inventario, nombre) is None:
        print("Producto no encontrado.")
        return
    print("Deje en blanco para no cambiar ese campo.")
    nuevo_precio = leer_("Nuevo precio: ", permitir_none=True)
    nueva_cantidad = leer_int("Nueva cantidad: ", permitir_none=True)
    if nuevo_precio is None and nueva_cantidad is None:
        print("No se realizaron cambios.")
    else:
        actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)


def opcion_eliminar(inventario):
    print("Iniciando eliminacion de producto ᓚᘏᗢ")
    print("\n-- Eliminar producto --")
    nombre = leer_nombre("Nombre a eliminar: ")
    if buscar_producto(inventario, nombre) is None:
        print("Producto no encontrado.")
        return
    confirmar = input("Confirmar eliminacion de " + nombre + " (si/no): ").strip()
    if confirmar == "si" or confirmar == "Si":
        eliminar_producto(inventario, nombre)
    else:
        print("Operacion cancelada.")


def opcion_estadisticas(inventario):
    mostrar_estadisticas(inventario)


def opcion_guardar(inventario):
    print("\n-- Guardar CSV --")
    ruta = leer_ruta("Ruta del archivo (ej. inventario.csv): ")
    guardar_csv(inventario, ruta)


def opcion_cargar(inventario):
    time.sleep(0.3) 
    print("→")
    sys.stdout.flush()
    time.sleep(0.3)
    print("←") 
    sys.stdout.flush()
    time.sleep(0.3)
    print("↝"*10) 
    sys.stdout.flush()
    print("\n-- Cargar CSV --")
    ruta = leer_ruta("Ruta del archivo a cargar: ")
    nuevos, filas_invalidas = cargar_csv(ruta)

    if not nuevos:
        if filas_invalidas > 0:
            print("No se cargo ningun producto. Filas invalidas: " + str(filas_invalidas))
        return

    print("Productos validos encontrados: " + str(len(nuevos)))
    if filas_invalidas > 0:
        print("Filas invalidas omitidas: " + str(filas_invalidas))

    accion = input("Sobrescribir inventario actual? (si/no): ").strip()

    if accion == "si" or accion == "Si":
        inventario.clear()
        inventario.extend(nuevos)
        print("Inventario reemplazado.")
    else:
        resumen = fusionar(inventario, nuevos)
        print("Agregados: " + str(resumen["agregados"]))
        print("Actualizados: " + str(resumen["actualizados"]))

    mostrar_inventario(inventario)


def mostrar_menu():
    ama = "\033[33m"
    time.sleep(0.4)
    print(ama+"Bienvenido al sistema de inventario")
    sys.stdout.flush()

    print("\nSISTEMA DE INVENTARIO (❁´◡`❁)")
    print("1. Agregar producto ⁕")
    print("2. Mostrar inventario []")
    print("3. Buscar producto ⁐")
    print("4. Actualizar producto ↜↝")
    print("5. Eliminar producto ✕")
    print("6. Estadisticas")
    print("7. Guardar CSV ✓")
    print("8. Cargar CSV ✓")
    print("9. Salir")


def main():
    inventario = []
    print("Bienvenido al Sistema de Inventario")
    time.sleep(0.3) 
    print("→")
    sys.stdout.flush()
    time.sleep(0.3)
    print("←") 
    sys.stdout.flush()
    time.sleep(0.3)
    print("↝"*10) 
    ejecutar = True

    while ejecutar:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-9): ").strip()

        if opcion == "1":
            opcionaΔgregar(inventario)
        elif opcion == "2":
            opcionΔmostrar(inventario)
        elif opcion == "3":
            opcionΔbuscar(inventario)
        elif opcion == "4":
            opcion_actualizar(inventario)
        elif opcion == "5":
            opcion_eliminar(inventario)
        elif opcion == "6":
            opcion_estadisticas(inventario)
        elif opcion == "7":
            opcion_guardar(inventario)
        elif opcion == "8":
            opcion_cargar(inventario)
        elif opcion == "9":
            print("Hasta luego.")
            ejecutar = False
        else:
            print("Opcion invalida. Ingrese un numero del 1 al 9.")


if __name__ == "__main__":
    main()
