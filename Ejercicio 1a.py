import numpy as np
import matplotlib.pyplot as plt

# Datos
xi = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
yi = np.array([102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72])

# Función para ajuste de polinomio
def ajuste_polinomio(x, y, grado):
    return np.polyfit(x, y, grado)

# Función para calcular el error
def calcular_error(polinomio, x, y):
    p = np.poly1d(polinomio)
    y_pred = p(x)
    return np.mean((y - y_pred) ** 2)

# Ajuste de polinomio
polinomio_grado_1 = ajuste_polinomio(xi, yi, grado=1)

# Cálculo del error
error_grado_1 = calcular_error(polinomio_grado_1, xi, yi)

# Grafica de los puntos y la línea ajustada
plt.figure('Polinomio por mínimos cuadrados de grado 1  ')
plt.scatter(xi, yi, color='red', label='Datos')
plt.plot(xi, np.poly1d(polinomio_grado_1)(xi), label=f'Polinomio grado 1\nError: {error_grado_1:.2f}')
plt.title('Ajuste de Polinomio de Grado 1')
plt.xlabel('Datos en xi')
plt.ylabel('Datos en yi')
plt.legend()
plt.show()


print(f"Error polinomio grado 1: {error_grado_1:.2f}")