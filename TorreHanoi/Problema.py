def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    filas = string_.strip().split('\n')
    estado = [[pieza.strip() for pieza in fila.split('-')] for fila in filas]
    return estado

class HanoiProblem(object):
    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo

    def acciones(self, estado):
        '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
        filas = string_to_list(estado)
        # Obtine la ubicacion de todas las piezas
        ub = {}
        for i,f in enumerate(filas):
            ubf = {c:[i,j] for j,c in enumerate(f) if c != '0'}
            ub = ub | ubf
        # Obtine todas las piezas que pueden moverse
        posibles = []
        for i in range(len(filas[0])):
            for j in filas:
                if j[i] != '0':
                    posibles.append(j[i])
                    break
        # Obtinen los posibles movimientos de las piezas que pueden moverse
        acciones = []
        for p in posibles:
            posicion = ub[p]
            for i in range(len(filas[0])):
                if i == int(posicion[1]):
                    continue
                for it,j in enumerate(filas):
                    if int(p) < int(j[i]):
                        acciones.append([it-1,i]+posicion+[p])
                        break
                    if j[i] == '0' and it==len(filas)-1:
                        acciones.append([it,i]+posicion+[p])
                    if j[i] != '0':
                        break
        return acciones


    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        posicion = accion[2:4]
        movimiento = accion[0:2]
        filas[posicion[0]][posicion[1]] = '0'
        filas[movimiento[0]][movimiento[1]] = accion[4]
        return list_to_string(filas)

    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == self.estado_objetivo

    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion.
        '''
        return 1
