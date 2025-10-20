def trabajar_con_conjuntos():
    # Pedimos al usuario la primera lista
    lista1 = input("Introduce los números de la primera lista separados por espacios: ")
    lista1 = [int(x) for x in lista1.split()]  # Convertimos a enteros

    # Pedimos al usuario la segunda lista
    lista2 = input("Introduce los números de la segunda lista separados por espacios: ")
    lista2 = [int(x) for x in lista2.split()]  # Convertimos a enteros

    # Convertimos las listas a conjuntos
    set1 = set(lista1)
    set2 = set(lista2)

    # Calculamos la intersección
    interseccion = set1 & set2

    # Calculamos la unión
    union = set1 | set2

    # Calculamos la diferencia simétrica
    diferencia_simetrica = set1 ^ set2

    # Creamos el diccionario con los resultados
    resultado = {
        "interseccion": interseccion,
        "union": union,
        "diferencia_simetrica": diferencia_simetrica
    }

    return resultado


# Llamamos a la función y mostramos el resultado
resultado = trabajar_con_conjuntos()
print("Resultado:")
print(f"Intersección: {resultado['interseccion']}")
print(f"Unión: {resultado['union']}")
print(f"Diferencia simétrica: {resultado['diferencia_simetrica']}")