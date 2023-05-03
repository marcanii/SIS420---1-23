import random

# Definir una lista con las teclas disponibles
teclas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Definir la longitud de la contraseña
longitud = 9
# Función de valuación para determinar la calidad de cada contraseña
def evaluar_contraseña(contraseña):
    distancia_total = 0
    for i in range(1, len(contraseña)):
        distancia_total += abs(contraseña[i] - contraseña[i - 1])
    return distancia_total
# Función para generar una contraseña aleatoria
def generar_contraseña():
    contraseña = random.sample(teclas, longitud)
    return contraseña

# Función de cruce para combinar dos contraseñas
def cruzar_contraseñas(contraseña1, contraseña2):
    punto_corte = random.randint(1, longitud - 1)
    nueva_contraseña = contraseña1[:punto_corte] + contraseña2[punto_corte:]
    return nueva_contraseña

# Función de mutación para cambiar aleatoriamente una tecla en la contraseña
def mutar_contraseña(contraseña):
    indice = random.randint(0, longitud - 1)
    nueva_tecla = random.choice(teclas)
    nueva_contraseña = contraseña.copy()
    nueva_contraseña[indice] = nueva_tecla
    return nueva_contraseña

# Configuración del algoritmo genético
tamano_poblacion = 50
probabilidad_cruce = 0.8
probabilidad_mutacion = 0.1
num_generaciones = 100

# Generar la población inicial
poblacion = [generar_contraseña() for _ in range(tamano_poblacion)]

# Ejecutar el algoritmo genético
for generacion in range(num_generaciones):
    # Evaluar la calidad de cada contraseña en la población
    evaluaciones = [evaluar_contraseña(contraseña) for contraseña in poblacion]

    # Seleccionar las mejores contraseñas para el cruce
    mejor_contraseña = poblacion[evaluaciones.index(min(evaluaciones))]
    poblacion_cruzada = [mejor_contraseña] + random.sample(poblacion, tamano_poblacion - 1)

    # Realizar el cruce entre parejas de contraseñas seleccionadas aleatoriamente
    for i in range(0, tamano_poblacion, 2):
        if random.random() < probabilidad_cruce:
            poblacion_cruzada[i] = cruzar_contraseñas(poblacion_cruzada[i], poblacion_cruzada[i + 1])
            poblacion_cruzada[i + 1] = cruzar_contraseñas(poblacion_cruzada[i + 1], poblacion_cruzada[i])

    # Realizar la mutación en cada contraseña de la población
    for i in range(tamano_poblacion):
        if random.random() < probabilidad_mutacion:
            poblacion_cruzada[i] = mutar_contraseña(poblacion_cruzada[i])

    # Actualizar la población con las nuevas contraseñas generadas
    poblacion = poblacion_cruzada

# Evaluar la calidad de cada contraseña en la población final
evaluaciones = [evaluar_contraseña(contraseña) for contraseña in poblacion]

#Obtener la mejor contraseña generada
mejor_contraseña = poblacion[evaluaciones.index(min(evaluaciones))]

#Imprimir la mejor contraseña generada y su distancia total

print("La mejor contraseña generada es:", mejor_contraseña)
print("La distancia total de la contraseña es:", evaluar_contraseña(mejor_contraseña))