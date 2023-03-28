# declarando matriz
matrix = [[1,1,1,1,1,1,1,1,1,1],
          [2,0,0,0,1,1,0,0,0,1],
          [1,1,1,0,0,0,0,1,0,1],
          [1,0,0,0,1,1,0,1,0,1],
          [1,0,1,0,1,1,0,0,0,1],
          [1,1,1,0,0,1,1,0,1,1],
          [1,0,0,0,0,1,0,0,0,1],
          [1,1,0,1,1,1,0,1,1,1],
          [1,0,0,0,0,0,0,0,0,3],
          [1,1,1,1,1,1,1,1,1,1]]

# dibujando el laberito
def dibujar():
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 1:
        print('#',end='')
      elif matrix[i][j] == 0:
        print(' ',end='')
      elif matrix[i][j] == 2:
        print('*',end='')
      else:
        print('+',end='')
    print()

dibujar()


# definir la posición inicial del jugador
fila_actual = 1
col_actual = 0

# var auxiliares
aux1 = 1
aux2 = 0

dibujar()

while True:
  # pedir al usuario que ingrese una dirección
  direccion = input("Ingrese una dirección (arriba, abajo, izquierda o derecha): ")

  # actualizar la posición del jugador según la dirección ingresada
  if direccion == "arriba":
      fila_actual -= 1
      aux1 = fila_actual + 1
  elif direccion == "abajo":
      fila_actual += 1
      aux1 = fila_actual - 1
  elif direccion == "izquierda":
      col_actual -= 1
      ax2 = col_actual + 1
  elif direccion == "derecha":
      col_actual += 1
      ax2 = col_actual - 1

  # actualizar la matriz para reflejar la nueva posición del jugador
  matrix[fila_actual][col_actual] = 2
  matrix[aux1][aux2] = 0

  # actualizando las var auxs
  aux1 = fila_actual
  aux2 = col_actual

  # limpiar la pantalla


  # dibujar el laberinto actualizado
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 1:
        print('#',end='')
      elif matrix[i][j] == 0:
        print(' ',end='')
      elif matrix[i][j] == 2:
        print('*',end='')
      else:
        print('+',end='')
    print()