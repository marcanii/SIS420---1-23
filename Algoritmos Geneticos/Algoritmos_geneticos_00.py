from math import inf as infinity
from random import choice
import platform
import time
from os import system
import random


# Que valores debe tener X1, X2 y X3 para que y = 4
y_buscada = 7
# Ecuacion: y = x1 - 2 * X2 + 3 * X3


diferencia_minima_identificada = 10000
x1 = 0
x2 = 0
x3 = 0

for i in range(0, 100):
  for j in range(0, 100):
    for k in range(0, 100):
      y_hat = i - 2 * j + 3 * k
      if (abs(y_hat - y_buscada) < diferencia_minima_identificada):
        print (f"x1: {i}, x2: {j}, x3: {k}, y_hat: {y_hat}, y_buscada: {y_buscada}, diferencia:{abs(y_hat - y_buscada)}")
        diferencia_minima_identificada = abs(y_hat - y_buscada)
        x1 = i
        x2 = j
        x3 = k
        if diferencia_minima_identificada == 0:
          break

print(f"La diferencia minima encontrada es: {diferencia_minima_identificada}")
print(f"con los valores de x1={x1}, x2={x2}, x3={x3}")


def funcion_adaptacion(individuo):
  y = 7
  y_hat = individuo[0] - 2 * individuo[1] + 3 * individuo[2]
  return abs(y_hat - y)


def obtener_mejores_individuos(poblacion, numero_individuos):
    individuos_fitness = []
    mejor_fitness = infinity;
    for individuo in poblacion:
        fitness_individuo = funcion_adaptacion(individuo)
        individuos_fitness.append([individuo[0], individuo[1], individuo[2], fitness_individuo])

    individuos_fitness.sort(key=lambda x: x[3])

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

def mostrar_individuos(individuos):
  # Imprimir todas las listas generadas
  print(f"numero de individuos: {len(individuos)}")
  for individuo in individuos:
    print(individuo)


def generar_nuevos_individuos(mejores_individuos):
  nuevos_individuos =[]
  hijo_1 = [mejores_individuos[0][0], mejores_individuos[0][1], mejores_individuos[len(mejores_individuos)-1][2]]
  nuevos_individuos.append(hijo_1)
  hijo_2 = [mejores_individuos[len(mejores_individuos)-1][0], mejores_individuos[len(mejores_individuos)-1][1], mejores_individuos[0][2]]
  nuevos_individuos.append(hijo_2)

  for numero_individuo in range(1, len(mejores_individuos)):
    hijo_1 = [mejores_individuos[numero_individuo - 1][0], mejores_individuos[numero_individuo - 1][1], mejores_individuos[numero_individuo][2]]
    nuevos_individuos.append(hijo_1)
    hijo_2 = [mejores_individuos[numero_individuo][0], mejores_individuos[numero_individuo][1], mejores_individuos[numero_individuo - 1][2]]
    nuevos_individuos.append(hijo_2)

  return nuevos_individuos


def main():
  poblacion = generar_individuos(10, 3)
  mostrar_individuos(poblacion)
  numero_individuos = len(poblacion) / 2
  mejores_individuos = obtener_mejores_individuos(poblacion, 5)
  mostrar_individuos(mejores_individuos)
  mejores_individuos_sin_fitness = [fila[:3] for fila in mejores_individuos]
  nueva_poblacion = generar_nuevos_individuos(mejores_individuos_sin_fitness)
  poblacion = nueva_poblacion
  mostrar_individuos(poblacion)
  numero_individuos = len(poblacion) / 2
  mejores_individuos = obtener_mejores_individuos(poblacion, 5)
  mostrar_individuos(mejores_individuos)


if __name__ == '__main__':
    main()