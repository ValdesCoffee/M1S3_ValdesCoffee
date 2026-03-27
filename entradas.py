def leer_(mensaje, permitir_none=False):
    valor = None
    valido = False
    while not valido:
        entrada = input(mensaje).strip()
        if permitir_none and entrada == "":
            return None
        try:
            valor = float(entrada)
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                valido = True
        except ValueError:
            print("Ingrese un numero valido.")
    return valor


def leer_int(mensaje, permitir_none=False):
    valor = None
    valido = False
    while not valido:
        entrada = input(mensaje).strip()
        if permitir_none and entrada == "":
            return None
        try:
            valor = int(entrada)
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                valido = True
        except ValueError:
            print("Ingrese un numero entero valido.")
    return valor


def leer_nombre(mensaje):
    nombre = ""
    valido = False
    while not valido:
        nombre = input(mensaje).strip()
        if nombre:
            valido = True
        else:
            print("El nombre no puede estar vacio.")
    return nombre


def leer_ruta(mensaje):
    ruta = ""
    valido = False
    while not valido:
        ruta = input(mensaje).strip()
        if ruta:
            valido = True
        else:
            print("La ruta no puede estar vacia.")
    return ruta
