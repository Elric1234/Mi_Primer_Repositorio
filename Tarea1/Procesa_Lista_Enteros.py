def procesar_lista(lista):
    # 1. Eliminar los números negativos
    lista_positivos = [x for x in lista if x >= 0]

    # 2. Eliminar los valores repetidos usando set porque no admite duplicados
    lista_sin_repetidos = list(set(lista_positivos))

    # 3. Ordenar de menor a mayor
    lista_ordenada = sorted(lista_sin_repetidos)

    return lista_ordenada

# Solicitar al usuario que ingrese números separados por espacios
entrada_usuario = input("Introduce números enteros separados por espacios: ")

# Convertir la entrada en una lista de enteros
lista_entrada = [int(x) for x in entrada_usuario.split()]

# Procesar la lista
resultado = procesar_lista(lista_entrada)

# Mostrar el resultado
print("Lista procesada:", resultado)
