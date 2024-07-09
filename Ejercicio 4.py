import numpy as np
import matplotlib.pyplot as plt

#  Datos
pesos_promedios = [4800, 3700, 3400, 2800, 1900]
porcentajes_presentacion = [3.1, 4.0, 5.2, 6.4, 9.6]

# Determinación de las sumas requeridas para aplicar mínimos cuadrados
suma_pesos = sum(pesos_promedios)
suma_porcentajes = sum(porcentajes_presentacion)
suma_pesos_porcentajes = sum(p * p_p for p, p_p in zip(pesos_promedios, porcentajes_presentacion))
suma_pesos_cuadrado = sum(p * p for p in pesos_promedios)
n = len(pesos_promedios)

# Calculo de coeficientes de la recta y = mx + b
m = (n * suma_pesos_porcentajes - suma_pesos * suma_porcentajes) / (n * suma_pesos_cuadrado - suma_pesos * suma_pesos)
b = (suma_porcentajes - m * suma_pesos) / n



# Grafica de los puntos y la línea ajustada
plt.figure('Subcomité Antimonopolio del Senado')
plt.scatter(pesos_promedios, porcentajes_presentacion, color='blue', label='Datos')
line_x = np.array([min(pesos_promedios), max(pesos_promedios)])
line_y = m * line_x + b
plt.plot(line_x, line_y, color='red', label=f' Ecuación de la recta y = {m:.2f}x + {b:.2f}')
plt.xlabel('Pesos promedios')
plt.ylabel('Porcentajes de presentación')
plt.title('Vehículos que participaron en un accidente')
plt.legend()
plt.show()