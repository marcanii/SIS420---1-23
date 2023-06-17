import numpy as np

import numpy as np

def checkNNGradients(nnCostFunction, lambda_=0.0):
    """
    Verifica los gradientes calculados por backpropagation en una red neuronal.

    Parameters:
    - nnCostFunction: Función de costo de la red neuronal.
    - lambda_: Parámetro de regularización (por defecto es 0.0).

    Returns:
    - diff: Diferencia relativa entre los gradientes numéricos y los gradientes aproximados por backpropagation.
    """

    # Obtén los gradientes por backpropagation
    cost, grad = nnCostFunction()

    # Inicializa los gradientes numéricos
    numgrad = np.zeros_like(grad)

    # Valor pequeño para la aproximación numérica
    epsilon = 1e-4

    # Itera sobre cada parámetro en la red neuronal
    for i in range(len(grad)):
        # Aproximación numérica del gradiente
        theta_plus = np.copy(nnCostFunction.theta)
        theta_plus[i] += epsilon
        theta_minus = np.copy(nnCostFunction.theta)
        theta_minus[i] -= epsilon

        # Cálculo del costo para los parámetros theta_plus y theta_minus
        cost_plus = nnCostFunction(theta_plus, lambda_)
        cost_minus = nnCostFunction(theta_minus, lambda_)

        # Aproximación numérica del gradiente
        numgrad[i] = (cost_plus - cost_minus) / (2 * epsilon)

    # Calcula la diferencia relativa entre los gradientes numéricos y los gradientes por backpropagation
    diff = np.linalg.norm(numgrad - grad) / np.linalg.norm(numgrad + grad)

    return diff


def sigmoid(z):
    """
    Calcula la función sigmoide de un número o una matriz.

    Parameters:
    - z: Número o matriz.

    Returns:
    - result: Resultado de aplicar la función sigmoide a z.
    """
    return 1.0 / (1.0 + np.exp(-z))