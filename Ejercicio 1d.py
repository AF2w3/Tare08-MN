import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos
xi = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
yi = np.array([102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72])

# Función modelo exponencial
def modelo_exponencial(x, a, b):
    return b * np.exp(a * x)

# Función para calcular el error
def calcular_error(y_real, y_pred):
    return np.mean((y_real - y_pred) ** 2)

# Ajuste de la función exponencial
parametros, _ = curve_fit(modelo_exponencial, xi, yi, p0=(0.1, 1))
a, b = parametros

# Predicción y cálculo del error
y_pred = modelo_exponencial(xi, a, b)
error_exponencial = calcular_error(yi, y_pred)

# Grafica de los puntos y la curva ajustada
plt.figure('Polinomio por mínimos cuadrados de la forma 𝑏𝑒^ax')
plt.scatter(xi, yi, color='red', label='Datos')
plt.plot(xi, y_pred, label=f'Exponencial: y = {b:.2f}e^({a:.2f}x),  Error: {error_exponencial:.2f}')
plt.title('Ajuste Exponencial')
plt.xlabel('Datos en xi')
plt.ylabel('Datos en yi')
plt.legend()
plt.show()


print(f"Error ajuste exponencial: {error_exponencial:.2f}")