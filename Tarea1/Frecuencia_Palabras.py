import string

def contar_frecuencia(palabras, ruta_fichero):
    # Inicializamos el diccionario con las palabras y frecuencia 0
    frecuencia = {palabra.lower(): 0 for palabra in palabras}

    # Abrimos el fichero
    with open(ruta_fichero, 'r', encoding='latin-1') as f:

        for linea in f:
            # Convertir a minúsculas y eliminar puntuación
            linea = linea.lower().translate(str.maketrans('', '', string.punctuation))
            # Separar en palabras
            palabras_linea = linea.split()
            # Contar frecuencia de cada palabra
            for palabra in palabras:
                frecuencia[palabra.lower()] += palabras_linea.count(palabra.lower())

    # Devolver diccionario ordenado por palabra
    return dict(sorted(frecuencia.items()))

# ---------------------------
# Programa de prueba
# ---------------------------
palabras_a_buscar = ['enteros', 'texto', 'mariposa', 'repositorio', 'lista']
ruta = './texto_para_problema_2.txt'

resultado = contar_frecuencia(palabras_a_buscar, ruta)

# Mostrar el resultado
print("Frecuencia de palabras:")
for palabra, freq in resultado.items():
    print(f"{palabra}: {freq}")
