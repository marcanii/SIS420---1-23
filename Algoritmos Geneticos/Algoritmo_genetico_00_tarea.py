from math import inf as infinity
from random import choice
import platform
import time
from os import system
import random

# Que valores debe tener X1, X2, X3, ..., x10 para que y = 6
y_buscada = 6
# Ecuacion: y = x1 - 2 * X2 + 3 * X3 - 5 * x4 + 1 * x5 - 12 * x6 - 4 * x7 + 2 * x8 - x9 + 3 * x10

def funcion_adaptacion(individuo):
  y = 6
  # y_hat = 3 * individuo[0]  - 2 * individuo[1] + 4 * individuo[2]
  y_hat = individuo[0] - 2 * individuo[1] + 3 * individuo[2] - 5 * individuo[3] + 1 * individuo[4] - 12 * individuo[5]
  - 4 * individuo[6] + 2 * individuo[7] - individuo[8] + 3 * individuo[9]
  return abs(y_hat - y)

# print(funcion_adaptacion([3,4,3,2,3,4,5,6,2,1]))

def obtener_mejores_individuos(poblacion, numero_individuos):
    individuos_fitness = []
    mejor_fitness = infinity;
    for individuo in poblacion:
        fitness_individuo = funcion_adaptacion(individuo)
        individuos_fitness.append(
            [individuo[0], individuo[1], individuo[2], individuo[3], individuo[4], individuo[5], individuo[6],
             individuo[7], individuo[8], individuo[9], fitness_individuo])

    print(individuos_fitness)
    individuos_fitness.sort(key=lambda x: x[10])

    return individuos_fitness[:numero_individuos]

def generar_individuos(numero_individuos, numero_genes):
  # Crear una lista vacía para almacenar todas las listas
  individuos = []

  # Crear 20 listas con 3 números aleatorios cada una
  for i in range(numero_individuos):
      cromosomas = []
      for j in range(numero_genes):
          nuevo_gen = random.randint(0, 9)
          cromosomas.append(nuevo_gen)
      individuos.append(cromosomas)

  return individuos

def mostrar_individuos(poblacion):
  # Imprimir todas las listas generadas
  print(f"numero de individuos: {len(poblacion)}")
  for individuo in poblacion:
    print(individuo)


def generar_nuevos_individuos(mejores_individuos):
  nuevos_individuos =[]
  hijo_1 = [mejores_individuos[0][0], mejores_individuos[0][1], mejores_individuos[0][2], mejores_individuos[0][3], mejores_individuos[0][4], mejores_individuos[len(mejores_individuos)-1][5], mejores_individuos[len(mejores_individuos)-1][6], mejores_individuos[len(mejores_individuos)-1][7], mejores_individuos[len(mejores_individuos)-1][8], mejores_individuos[len(mejores_individuos)-1][9]]
  nuevos_individuos.append(hijo_1)
  hijo_2 = [mejores_individuos[len(mejores_individuos)-1][0], mejores_individuos[len(mejores_individuos)-1][1], mejores_individuos[len(mejores_individuos)-1][2], mejores_individuos[len(mejores_individuos)-1][3], mejores_individuos[len(mejores_individuos)-1][4], mejores_individuos[0][5], mejores_individuos[0][6],mejores_individuos[0][7], mejores_individuos[0][8], mejores_individuos[0][9]]
  nuevos_individuos.append(hijo_2)

  for numero_individuo in range(1, len(mejores_individuos)):
    hijo_1 = [mejores_individuos[numero_individuo - 1][0], mejores_individuos[numero_individuo - 1][1], mejores_individuos[numero_individuo - 1][2], mejores_individuos[numero_individuo - 1][3], mejores_individuos[numero_individuo - 1][4], mejores_individuos[numero_individuo][5], mejores_individuos[numero_individuo][6], mejores_individuos[numero_individuo][7], mejores_individuos[numero_individuo][8], mejores_individuos[numero_individuo][9]]
    nuevos_individuos.append(hijo_1)
    hijo_2 = [mejores_individuos[numero_individuo][0], mejores_individuos[numero_individuo][1], mejores_individuos[numero_individuo][2], mejores_individuos[numero_individuo][3], mejores_individuos[numero_individuo][4], mejores_individuos[numero_individuo - 1][5], mejores_individuos[numero_individuo - 1][6], mejores_individuos[numero_individuo - 1][7], mejores_individuos[numero_individuo - 1][8], mejores_individuos[numero_individuo - 1][9]]
    nuevos_individuos.append(hijo_2)

  return nuevos_individuos


def main():
    poblacion = generar_individuos(100, 10)
    print('Poblacion inicial...')
    mostrar_individuos(poblacion)
    value = True
    while value:
        mejores_individuos = obtener_mejores_individuos(poblacion, 50)
        mostrar_individuos(mejores_individuos)
        mejores_individuos_sin_fitness = [fila[:10] for fila in mejores_individuos]
        print('Poblacion sin Fitness...')
        mostrar_individuos(mejores_individuos_sin_fitness)
        nueva_poblacion = generar_nuevos_individuos(mejores_individuos_sin_fitness)
        poblacion = nueva_poblacion
        #mostrar_individuos(poblacion)
        individuo = mejores_individuos[0];
        if individuo[10] == 0:
            value = False
            print('\nSolucion encontrada...')
            solucion = mejores_individuos_sin_fitness[0]
            print(solucion)

if __name__ == '__main__':
    main()