import random


# ================================================
# Implementación clase abstracta algoritmo genético
# ================================================
# Definir clase abstracta Problema_Genetico
# Propiedades:
# - genes: lista de genes usados en el genotipo de los estados.
# - longitud_individuos: longitud de los cromosomas
# Métodos:
# - decodifica: función de obtiene el fenotipo a partir del genotipo.
# - fitness: función de valoración.
# - muta: mutación de un cromosoma
# - cruza: cruce de un par de cromosomas
# En la definición de clase no se especifica si el problema es
# de maximización o de minimización, esto se hace con el
# parámetro en el algoritmo genético que se implemente.

class Problema_Genetico(object):
    # Constructor
    def __init__(self, genes, fun_decodificar, fun_cruzar, fun_mutar, fun_fitness, longitud_individuos):
        self.genes = genes
        self.fun_decodificar = fun_decodificar
        self.fun_cruzar = fun_cruzar
        self.fun_mutar = fun_mutar
        self.fun_fitness = fun_fitness
        self.longitud_individuos = longitud_individuos

    def decodificar(self, genotipo):
        # Devuelve el fenotipo a partir del genotipo
        fenotipo = self.fun_decodificar(genotipo)
        return fenotipo

    def cruzar(self, cromosoma1, cromosoma2):
        # Devuelve el cruce de un par de cromosomas
        cruce = self.fun_cruzar(cromosoma1, cromosoma2)
        return cruce

    def mutar(self, cromosoma, prob):
        # Devuelve el cromosoma mutado
        mutante = self.fun_mutar(cromosoma, prob)
        return mutante

    # Si se quisiera implementar otro mecanismo de cruza
    # def cruza_loca(self, cromosoma1, cromosoma2, cromosoma3, cromosoma4):
    #    cruce = self.fun_cruza(cromosoma1, cromosoma2, cromosoma3, cromosoma4)
    #    return cruce

    def fitness(self, cromosoma):
        # Función de valoración
        valoracion = self.fun_fitness(cromosoma)
        return valoracion

# Función interpreta lista de 0's y 1's como número natural:

def binario_a_decimal(x):
    return sum(b * (2 ** i) for (i, b) in enumerate(x))

# binario_a_decimal([1,0,0,0,1,1,0,0,1,0,1])

def fun_cruzar(cromosoma1, cromosoma2):
    # Cruza los cromosomas por la mitad
    l1 = len(cromosoma1)
    l2 = len(cromosoma2)
    cruce1 = cromosoma1[0:int(l1 / 2)]+cromosoma2[int(l1 / 2):l2]
    cruce2 = cromosoma2[0:int(l2 / 2)]+cromosoma1[int(l2 / 2):l1]
    return [cruce1, cruce2]

def fun_mutar(cromosoma, prob):
    # Elige un elemento al azar del cromosoma y lo modifica con una probabilidad igual a prob
    l = len(cromosoma)
    p = random.randint(0, l - 1)
    if prob > random.uniform(0, 1):
        cromosoma[p] =  (cromosoma[p] + 1) % 2
        #cromosoma[p] = cromosoma[p]*-1
    return cromosoma

#def fun_fitness_cuad(cromosoma):
#    # Función de valoración que eleva al cuadrado el número recibido en binario
#    n = binario_a_decimal(cromosoma)**2
#    return n

# def deco_x(x):
#     return [binario_a_decimal(x[:4]), binario_a_decimal(x[4:])]

# Definir una función poblacion_inicial(problema_genetico, tamaño), para
# definir una población inicial de un tamaño dado, para una instancia dada de
# la clase anterior Problema_Genetico

def poblacion_inicial(problema_genetico, size):
    l = []
    for i in range(size):
        l.append([random.choice(problema_genetico.genes) for i in range(problema_genetico.longitud_individuos)])
    return l

# Definir una función cruza_padres(problema_genetico, padres), que recibiendo
# una instancia de Problema_Genetico y una población de padres (supondremos
# que hay un número par de padres), obtiene la población resultante de
# cruzarlos de dos en dos (en el orden en que aparecen)

def cruza_padres(problema_genetico, padres):
    l = []
    l1 = len(padres)
    while padres != []:
        l.extend(problema_genetico.cruzar(padres[0], padres[1]))
        padres.pop(0)
        padres.pop(0)
    return l

# Ejemplo
# >>>  cruza_padres(cuad_gen, [[1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
# [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
# [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
# [0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
# [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
# [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
# [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
# [1, 1, 0, 1, 0, 1, 1, 0, 0, 1]])

# [[1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
# [0, 1, 1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
# [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 0, 0, 0, 1, 0, 1]]

# Definir una función muta_individuos(problema_genetico, poblacion, prob), que
# recibiendo una instancia de Problema_Genetico, una población y una
# probabilidad de mutación, obtiene la población resultante de aplicar
# operaciones de mutación a cada individuo.

def muta_individuos(problema_genetico, poblacion, prob):
    return [problema_genetico.mutar(x, prob) for x in poblacion]

# Ejemplo
# >>> muta_individuos(cuad_gen,poblacion_inicial(cuad_gen, 4), 0.1)
# [[1, 1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1, 1, 1, 0]]

# Definir una función
# seleccion_por_torneo(problema_genetico,poblacion,n,k,opt)
# que implementa la selección mediante torneo de n individuos de una
# población.  Esta función recibe como entrada una instancia de
# Problema_Genetico, una población, un número natural n (número de individuos
# a seleccionar) un número natural k (número de participantes en el torneo) y
# un valor opt que puede ser o la función max o la función min (dependiendo de
# si el problema es de maximización o de minimización, resp.).

# INDICACIÓN: Usar random.sample

def seleccion_por_torneo(problema_genetico, poblacion, n, k, opt):
    # Selección por torneo de n individuos de una población. Siendo k el nº de participantes
    # y opt la función max o min.
    seleccionados = []
    for i in range(n):
        participantes = random.sample(poblacion, k)
        seleccionado = opt(participantes, key = problema_genetico.fitness)
        #opt(poblacion, key = problema_genetico.fitness)
        seleccionados.append(seleccionado)
        # poblacion.remove(seleccionado)
    return seleccionados

# Ejemplo
# >>> seleccion_por_torneo(cuad_gen, poblacion_inicial(cuad_gen,8),3,6,max)
# [[1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1, 0, 1]]
# seleccion_por_torneo(cuad_gen, poblacion_inicial(cuad_gen,8),3,6,min)
# [[0, 0, 1, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]]
# -----------------------------

# Se pide definir la única función auxiliar que queda por definir en el
# algoritmo anterior; es decir, la función
# nueva_generacion_t(problema_genetico, opt ,poblacion, n_padres, prob_mutar)
# que a partir de una población dada, calcula la siguiente generación.

def nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar):
    padres2 = seleccion_por_torneo(problema_genetico, poblacion, n_directos, k, opt)
    padres1 = seleccion_por_torneo(problema_genetico, poblacion, n_padres , k, opt)
    cruces =  cruza_padres(problema_genetico,padres1)
    generacion = padres2 + cruces
    resultado_mutaciones = muta_individuos(problema_genetico, generacion, prob_mutar)
    return resultado_mutaciones

# >>> nueva_generacion_t(cuad_gen, 3, max, poblacion_inicial(cuad_gen, 10), 6, 4 , 0.1)
# [[0, 0, 1, 1, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0]]



# La siguiente función algoritmo_genetico_t implementa el primero de los
# algoritmos genéticos (el de selección por torneo)

# Argumentos de entrada:
# * problema_genetico: una instancia de la clase Problema_Genetico, con el
#   problema de optimización que se quiere resolver.
# * k: número de participantes en los torneos de selección.
# * opt: max ó min, dependiendo si el problema es de maximización o de
#   minimización.
# * ngen: número de generaciones (condición de terminación)
# * tamaño (size): número de individuos en cada generación
# * prop_cruces: proporción del total de la población que serán padres.
# * prob_mutar: probabilidad de realizar una mutación de un gen.

def algoritmo_genetico_t(problema_genetico, k, opt, ngen, size, prop_cruces, prob_mutar):
    poblacion = poblacion_inicial(problema_genetico, size)
    print("Poblacion Inicial")
    print(poblacion)
    n_padres = round(size * prop_cruces)
    n_padres = int (n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = size - n_padres
    for _ in range(ngen):
        poblacion = nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar)
        print("Nueva población")
        print(poblacion)
    mejor_cr = opt(poblacion, key = problema_genetico.fitness)
    mejor = problema_genetico.decodificar(mejor_cr)
    return (mejor, problema_genetico.fitness(mejor_cr))


# ===================================================
# Representación del problema de la mochila
# ===================================================

# Problema de la mochila: dados n objetos de pesos p_i y valor v_i
# (i = 1, ..., n), seleccionar cuáles se meten en una mochila que soporta un
# peso P máximo, de manera que se máximice el valor de los objetos
# introducidos.

# Definir función
# decodifica_mochila(cromosoma, n_objetos, pesos, capacidad)
# recibe como entrada:

# - un cromosoma (en este caso, una lista de 0s y 1s, de longitud igual a
#   n_objetos)
# - n_objetos: número total de objetos de la mochila
# - pesos: una lista con los pesos de los objetos
# - capacidad: peso máximo de la mochila.

# La función debe devolver una lista de 0s y 1s que indique qué objetos están en
# la mochila y cuáles no (el objeto i está en la mochila si y sólo si en la
# posción i-ésima de la lista hay un 1). Esta lista se obtendrá a partir del
# cromosoma, pero teniendo en cuenta que a partir del primer objeto que no
# quepa, éste y los siguientes se consideran fuera de la mochila,
# independientemente del valor que haya en su correspondiente posición de
# cromosoma.

def decodifica_mochila(cromosoma, n_objetos, pesos, capacidad):
    peso_en_mochila = 0
    l = []
    for i in range(n_objetos):
        if cromosoma[i] == 1 and peso_en_mochila + pesos[i] <= capacidad:
            l.append(1)
            peso_en_mochila += pesos[i]
        elif cromosoma[i] == 0 or peso_en_mochila + pesos[i] > capacidad:
            l.append(0)
    return l


# decodifica_mochila([1, 1, 0, 1], 4, [18, 2, 8, 1], 20)
# [1, 1, 0, 0]

# Definir función fitness
# fitness_mochila(cromosoma, n_objetos, pesos, capacidad, valores)
# devuelve el valor total de los objetos que están dentro de la mochila
# que representa el cromosoma, según la codificación explicada en el ejercicio
# anterior. Aquí valores es la lista de los valores de cada objeto y el resto
# de argumentos son los mismos que en el ejercicio anterior.

def fitness_mochila(cromosoma, n_objetos, pesos, capacidad, valores):
    objetos_en_mochila = decodifica_mochila(cromosoma, n_objetos, pesos, capacidad)
    valor = 0
    for i in range(n_objetos):
        if objetos_en_mochila[i] == 1:
            valor += valores[i]
    return valor


# >>> fitness_mochila([1,1,1,1],4,[18,2,8,1],20,[3,4,8,1])
# 7

# ============================================================
# Resolviendo instancias del problema de la mochila
# ============================================================

# Damos aquí tres instancias concretas del problema de la mochila. Damos
# también sus soluciones optimas, para que se puedan comparar con los
# resultados obtenidos por el algoritmo genético:

# _______________________________________________________
# Problema de la mochila 1:
# 10 objetos, peso máximo 165
pesos1 = [90, 50, 60, 80, 90, 10, 2, 100, 30, 5]
valores1 = [6, 9, 1, 2, 10, 9, 10, 5, 10, 4]

# OBJETOS["Cuchillo", "Peluche", "Pelota", "Maletin Primero Auxilios", "linterna",
# "Fosforo", "Gaseosa", "Mangera", "Lata de sardina", "Caviar"]
([0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 43)

# Solución óptima= [1,1,1,1,0,1,0,0,0,0], con valor 309
# _______________________________________________________
# Problema de la mochila 2:
# 15 objetos, peso máximo 750

pesos2 = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
valores2 = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]


## Solución óptima= [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1] con valor 1458
## _______________________________________________________
## Problema de la mochila 3:
## 24 objetos, peso máximo 6404180
# pesos3 = [382745,799601,909247,729069,467902, 44328,
#       34610,698150,823460,903959,853665,551830,610856,
#       670702,488960,951111,323046,446298,931161, 31385,496951,264724,224916,169684]
# valores3 = [825594,1677009,1676628,1523970, 943972,  97426,
#       69666,1296457,1679693,1902996,
#       1844992,1049289,1252836,1319836, 953277,2067538, 675367,
#       853655,1826027, 65731, 901489, 577243, 466257, 369261]

# Solución óptima= [1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1] con valoración 13549094
# _______________________________________________________
# Definir variables m1g, m2g y m3g, referenciando a instancias de
# Problema_Genetico que correspondan, respectivamente, a los problemas de la
# mochila anteriores.
# Usar el algoritmo genético anterior para resolver estos problemas.
# Por ejemplo:
# >>> >>> algoritmo_genetico_t(m1g,3,max,100,50,0.8,0.05)
# ([1, 1, 1, 1, 0, 1, 0, 0, 0, 0], 309)
# >>> algoritmo_genetico_t(m2g,3,max,100,50,0.8,0.05)
# ([1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0], 1444)
# >>> algoritmo_genetico_t(m2g,3,max,200,100,0.8,0.05)
# ([0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], 1439)
# >>> algoritmo_genetico_t(m2g,3,max,200,100,0.8,0.05)
# ([1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], 1458)

# >>> algoritmo_genetico_t(m3g,5,max,400,200,0.75,0.1)
# ([1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 13518963)
# >>> algoritmo_genetico_t(m3g,4,max,600,200,0.75,0.1)
# ([1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 13524340)
# >>> algoritmo_genetico_t(m3g,4,max,1000,200,0.75,0.1)
# ([1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 13449995)
# >>> algoritmo_genetico_t(m3g,3,max,1000,100,0.75,0.1)
# ([1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 13412953)
# >>> algoritmo_genetico_t(m3g,3,max,2000,100,0.75,0.1)
# ([0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 13366296)
# >>> algoritmo_genetico_t(m3g,6,max,2000,100,0.75,0.1)
# ([1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1], 13549094)


def fitness_mochila_1(cromosoma):
    v = fitness_mochila(cromosoma, 10, pesos1, 150, valores1)
    return v


def decodifica_mochila_1(cromosoma):
    v = decodifica_mochila(cromosoma, 10, pesos1, 150)
    return v


m1g = Problema_Genetico([0, 1], decodifica_mochila_1, fun_cruzar, fun_mutar, fitness_mochila_1, 10)

# def fitness_mochila_2(cromosoma):
#     v = fitness_mochila(cromosoma, 15, pesos2, 150, valores2)
#     return v

# def decodifica_mochila_2(cromosoma):
#     v = decodifica_mochila(cromosoma, 15, pesos2, 150)
#     return v

# m2g = Problema_Genetico([0,1], decodifica_mochila_2, fun_cruzar, fun_mutar, fitness_mochila_2, 15)

# def fitness_mochila_3(cromosoma):
#    v = fitness_mochilaa(cromosoma, 24, pesos3, 6404180 , valores3)
#    return v

# def decodifica_mochila_3(cromosoma):
#    v = decodifica_mochila(cromosoma, 24, pesos3, 6404180)
#    return v
# m3g = Problema_Genetico([0,1], decodifica_mochila_3, fun_cruzar,  fun_mutar, fitness_mochila_3,24)


print(algoritmo_genetico_t(m1g, 3, max, 100, 50, 0.8, 0.05))

