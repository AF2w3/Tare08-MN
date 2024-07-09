import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos
xi = np.array([0.2, 0.3, 0.6, 0.9, 1.1, 1.3, 1.4, 1.6])
yi = np.array([0.050446, 0.098426, 0.33277, 0.72660, 1.0972, 1.5697, 1.8487, 2.5015])

# Función modelo de potencia
def modelo_potencia(x, a, b):
    return b * x ** a

# Función para calcular el error
def calcular_error(y_real, y_pred):
    return np.mean((y_real - y_pred) ** 2)

# Ajuste de la función de potencia
parametros, _ = curve_fit(modelo_potencia, xi, yi, p0=(1, 1))
a, b = parametros

# Predicción y cálculo del error
y_pred = modelo_potencia(xi, a, b)
error_potencia = calcular_error(yi, y_pred)

# Grafica de los puntos y la curva ajustada
plt.figure('Polinomio por mínimos cuadrados de la forma 𝑏𝑥^a')
plt.scatter(xi, yi, color='red', label='Datos')
plt.plot(xi, y_pred, label=f'Potencia: y = {b:.2f}x^{a:.2f} , Error: {error_potencia:.2f}')
plt.title('Ajuste de Potencia')
plt.xlabel('Datos en xi')
plt.ylabel('Datos en yi')
plt.legend()
plt.show()

print(f"Error ajuste potencia: {error_potencia:.2f}")