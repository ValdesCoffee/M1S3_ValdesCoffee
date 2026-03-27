import csv

MAINTITLE = ["nombre", "precio", "cantidad"]


def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario esta vacio. No hay nada que guardar.")
        return False

    try:
        archivo = open(ruta, "w", newline="", encoding="utf-8")
        escritor = csv.DictWriter(archivo, fieldnames=MAINTITLE)
        if incluir_header:
            escritor.writeheader()
        for producto in inventario:
            escritor.writerow({
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": producto["cantidad"],
            })
        archivo.close()
        print("Inventario guardado en: " + ruta)
        return True

    except PermissionError:
        print("Sin permisos para escribir en " + ruta)
    except OSError as e:
        print("Error al guardar el archivo: " + str(e))
    except Exception as e:
        print("Error inesperado al guardar: " + str(e))

    return False


def cargar_csv(ruta):
    productos = []
    filas_invalidas = 0

    try:
        archivo = open(ruta, "r", newline="", encoding="utf-8")
        lector = csv.reader(archivo)

        encabezado = next(lector)
        encabezado_norm = []
        for col in encabezado:
            encabezado_norm.append(col.strip().lower())

        if encabezado_norm != MAINTITLE:
            print("Encabezado invalido. Se esperaba: nombre,precio,cantidad")
            archivo.close()
            return [], 0

        num_fila = 2
        for fila in lector:
            if len(fila) != 3:
                print("Fila " + str(num_fila) + ": columnas incorrectas. Omitida.")
                filas_invalidas = filas_invalidas + 1
                num_fila = num_fila + 1
                continue

            nombre_val = fila[0].strip()
            precio_val = fila[1]
            cantidad_val = fila[2]

            if not nombre_val:
                print("Fila " + str(num_fila) + ": nombre vacio. Omitida.")
                filas_invalidas = filas_invalidas + 1
                num_fila = num_fila + 1
                continue

            try:
                precio_num = float(precio_val)
                if precio_num < 0:
                    print("Fila " + str(num_fila) + ": precio negativo. Omitida.")
                    filas_invalidas = filas_invalidas + 1
                    num_fila = num_fila + 1
                    continue
            except ValueError:
                print("Fila " + str(num_fila) + ": precio invalido. Omitida.")
                filas_invalidas = filas_invalidas + 1
                num_fila = num_fila + 1
                continue

            try:
                cantidad_num = int(float(cantidad_val))
                if cantidad_num < 0:
                    print("Fila " + str(num_fila) + ": cantidad negativa. Omitida.")
                    filas_invalidas = filas_invalidas + 1
                    num_fila = num_fila + 1
                    continue
            except ValueError:
                print("Fila " + str(num_fila) + ": cantidad invalida. Omitida.")
                filas_invalidas = filas_invalidas + 1
                num_fila = num_fila + 1
                continue

            producto = {"nombre": nombre_val, "precio": precio_num, "cantidad": cantidad_num}
            productos.append(producto)
            num_fila = num_fila + 1

        archivo.close()

    except FileNotFoundError:
        print("Archivo no encontrado: " + ruta)
        return [], 0
    except UnicodeDecodeError:
        print("El archivo tiene caracteres no compatibles.")
        return [], 0
    except Exception as e:
        print("Error inesperado al cargar: " + str(e))
        return [], 0

    return productos, filas_invalidas


def fusionar(inventario_actual, nuevos_productos):
    print("Politica de fusion:")
    print("  - Nombre nuevo: se agrega al inventario.")
    print("  - Nombre existente: se suma cantidad y se actualiza precio si difiere.")

    agregados = 0
    actualizados = 0

    for nuevo in nuevos_productos:
        encontrado = None
        for producto in inventario_actual:
            if producto["nombre"].lower() == nuevo["nombre"].lower():
                encontrado = producto
        if encontrado is None:
            inventario_actual.append(nuevo)
            agregados = agregados + 1
        else:
            encontrado["cantidad"] = encontrado["cantidad"] + nuevo["cantidad"]
            if encontrado["precio"] != nuevo["precio"]:
                encontrado["precio"] = nuevo["precio"]
            actualizados = actualizados + 1

    return {"agregados": agregados, "actualizados": actualizados}
