import random
import math

numero_genes = 9  # La longitud del material genetico de cada individuo
tamano_poblacion = 100  # La cantidad de individuos que habra en la poblacion
precision = 30  # Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
probabilidad_mutacion = 0.4  # La probabilidad de que un individuo mute
valor_minimo_gen = 1
valor_maximo_gen = 9

def crear_individuo(min, max):
    # Crea un individuo
    cromosoma = []
    for i in range(numero_genes):
        while True:
            num = random.randint(min, max)
            if num not in cromosoma:
                break
        cromosoma.append(num)

    return cromosoma

def crear_poblacion(numero_individuos):
    # Crea una poblacion nueva de individuos
    return [crear_individuo(valor_minimo_gen, valor_maximo_gen) for i in range(numero_individuos)]

def calcular_fitness(individuo):
    fitness = 0
    for i in range(0 ,numero_genes -1):
        if (individuo[i] + individuo[ i +1]) != 10:
            fitness += 1

    return fitness

# funcion empleada para ordenar la poblacion
def ordenar_por_segundo_elemento(elem):
    return elem[1]

def seleccion_y_reproduccion(poblacion):
    # Puntua todos los elementos de la poblacion (population) y se queda con los mejores guardandolos dentro de 'seleccionados'.
    # Despues mezcla el material genetico de los elegidos para crear nuevos individuos y llenar la poblacion
    # (guardando tambien una copia de los individuos seleccionados sin modificar).
    # Por ultimo se aplica la mutacion a los individuos.
    poblacion_evaluada = [(indiv, calcular_fitness(indiv)) for indiv in poblacion ]  # Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma ([1,2,1,1,4,1,8,9,4,1], 5)
    poblacion_ordenada  = [indiv[0] for indiv in sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)]  # Ordena los pares ordenados y se queda solo con el array de valores

    poblacion = poblacion_ordenada
    # poblacion_seleccionada = poblacion_ordenada[(len(poblacion_ordenada) - precision):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'precision'
    poblacion_seleccionada = poblacion_ordenada[precision:]  # Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'precision'
    # Se mezcla el material genetico para crear nuevos individuos
    for i in range(precision, len(poblacion)):
        punto_cruce = random.randint(1, numero_genes - 1)  # Se elige un punto para hacer el intercambio
        padre = random.sample(poblacion_seleccionada, 2)

        if padre[0][:punto_cruce] not in poblacion[i][punto_cruce:]:  # Se eligen dos padres
            poblacion[i][:punto_cruce] = padre[0][:punto_cruce]
        if padre[1][punto_cruce:] not in poblacion[i][:punto_cruce]:  # Se mezcla el material genetico de los padres en cada nuevo individuo
            poblacion[i][punto_cruce:] = padre[1][punto_cruce:]

    return poblacion  # El array 'poblacion' tiene ahora una nueva poblacion de individuos, que se devuelven

def generar_nuevos_individuos(mejores_individuos):
    nuevos_individuos =[]
    # if mejores_individuos[[0][4:]] not in nuevos_individuos[[-1][:4]]:
    #   hijo_1 = [mejores_individuos[0][0], mejores_individuos[0][1], mejores_individuos[0][2], mejores_individuos[0][3], mejores_individuos[0][4], mejores_individuos[len(mejores_individuos)-1][5], mejores_individuos[len(mejores_individuos)-1][6], mejores_individuos[len(mejores_individuos)-1][7], mejores_individuos[len(mejores_individuos)-1][8]]
    #   nuevos_individuos.append(hijo_1)
    # if mejores_individuos[[-1][:4]] not in nuevos_individuos[[0][4:]]:
    #   hijo_2 = [mejores_individuos[len(mejores_individuos)-1][0], mejores_individuos[len(mejores_individuos)-1][1], mejores_individuos[len(mejores_individuos)-1][2], mejores_individuos[len(mejores_individuos)-1][3], mejores_individuos[len(mejores_individuos)-1][4], mejores_individuos[0][5], mejores_individuos[0][6],mejores_individuos[0][7], mejores_individuos[0][8]]
    #   nuevos_individuos.append(hijo_2)

    hijo_1 = [mejores_individuos[0][0], mejores_individuos[0][1], mejores_individuos[0][2], mejores_individuos[0][3],
              mejores_individuos[0][4], mejores_individuos[len(mejores_individuos) - 1][5],
              mejores_individuos[len(mejores_individuos) - 1][6], mejores_individuos[len(mejores_individuos) - 1][7],
              mejores_individuos[len(mejores_individuos) - 1][8]]
    nuevos_individuos.append(hijo_1)

    hijo_2 = [mejores_individuos[len(mejores_individuos) - 1][0], mejores_individuos[len(mejores_individuos) - 1][1],
              mejores_individuos[len(mejores_individuos) - 1][2], mejores_individuos[len(mejores_individuos) - 1][3],
              mejores_individuos[len(mejores_individuos) - 1][4], mejores_individuos[0][5], mejores_individuos[0][6],
              mejores_individuos[0][7], mejores_individuos[0][8]]
    nuevos_individuos.append(hijo_2)

    for numero_individuo in range(1, len(mejores_individuos)):
        hijo_1 = [mejores_individuos[numero_individuo - 1][0], mejores_individuos[numero_individuo - 1][1],
                  mejores_individuos[numero_individuo - 1][2], mejores_individuos[numero_individuo - 1][3],
                  mejores_individuos[numero_individuo - 1][4], mejores_individuos[numero_individuo][5],
                  mejores_individuos[numero_individuo][6], mejores_individuos[numero_individuo][7],
                  mejores_individuos[numero_individuo][8]]
        nuevos_individuos.append(hijo_1)

        hijo_2 = [mejores_individuos[numero_individuo][0], mejores_individuos[numero_individuo][1],
                  mejores_individuos[numero_individuo][2], mejores_individuos[numero_individuo][3],
                  mejores_individuos[numero_individuo][4], mejores_individuos[numero_individuo - 1][5],
                  mejores_individuos[numero_individuo - 1][6], mejores_individuos[numero_individuo - 1][7],
                  mejores_individuos[numero_individuo - 1][8]]
        nuevos_individuos.append(hijo_2)

        poblacion_evaluada = [(indiv, calcular_fitness(indiv)) for indiv in nuevos_individuos]
        poblacion_ordenada = [indiv[0] for indiv in sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)]

        poblacion_ordenada = poblacion_ordenada[:100]

    return poblacion_ordenada

def mutacion(poblacion):
    # Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podriavalcanzarse la solucion.
    for i in range(precision, len(poblacion)):
        if random.random() <= probabilidad_mutacion:  # Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0, numero_genes - 1)  # Se elgie un punto al azar
            nuevo_valor = random.randint(valor_minimo_gen, valor_maximo_gen)  # y un nuevo valor para este punto

            # Es importante mirar que el nuevo valor no sea igual al viejo
            if nuevo_valor not in poblacion[i]:
                while nuevo_valor == poblacion[i][punto]:
                    nuevo_valor = random.randint(valor_minimo_gen, valor_maximo_gen)
                poblacion[i][punto] = nuevo_valor

            # Se aplica la mutacion

    return poblacion


poblacion = crear_poblacion(tamano_poblacion)  # Inicializar una poblacion
print("Poblacion Inicial:")  # Se muestra la poblacion inicial
poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion]
poblacion_ordenada = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)

for ind in poblacion_ordenada:
    print(f"individuo: {ind[0]} fitness: {ind[1]}")

numero_generaciones = 1000
mejor_fitness = math.inf
numero_generacion = 0
break_out_flag = False
# Se evoluciona la poblacion
for i in range(numero_generaciones):
    puntuados = [(ind, calcular_fitness(ind)) for ind in poblacion]
    numero_generacion = numero_generacion + 1
    for indPun in puntuados:
        if indPun[1] < mejor_fitness:
            mejor_fitness = indPun[1]
        if indPun[1] == 0:
            break_out_flag = True
            break

    if break_out_flag:
        break

    poblacion = seleccion_y_reproduccion(poblacion)
    # poblacion = generar_nuevos_individuos(poblacion)
    poblacion = mutacion(poblacion)

    poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion]
    poblacion_ordenada = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)

    print(f"generacion no: {numero_generacion}")
    for ind in poblacion_ordenada:
        print(f"individuo: {ind[0]} fitness: {ind[1]}")

print("Poblacion final:")

poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion]
poblacion_ordenada = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)

for ind in poblacion_ordenada:
    print(f"individuo: {ind[0]} fitness: {ind[1]}")

if mejor_fitness == 0:
    individuo = poblacion_ordenada[0][0]
    print(f"El mejor fenotipo que resuelve la ecuacion es:{individuo}")
    print(f"la solucion se encontro en la {numero_generacion} generación")
else:
    individuo = poblacion_ordenada[0][0]
    print(f"Se encuentra en la {numero_generacion} generación")
    print(f"La mejor opción que se encontró fue: {individuo}")

# individuo: [1, 9, 7, 3, 2, 8, 5, 6, 4] fitness: 4
# La mejor opción que se encontró fue: [7, 3, 1, 9, 4, 6, 5, 2, 8]