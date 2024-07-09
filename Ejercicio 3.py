import numpy as np
import matplotlib.pyplot as plt

# Datos
act_scores = [28, 25, 28, 27, 28, 33, 28, 23, 29, 33, 27, 29, 33, 28, 28, 23, 29, 33, 27, 24]
average_scores = [3.84, 3.21, 3.23, 3.63, 3.75, 3.20, 3.41, 2.38, 3.38, 3.53, 2.81, 2.21, 1.66, 3.12, 3.65, 2.96, 3.33, 3.75, 2.92, 2.81]

# Grafica
plt.scatter(act_scores, average_scores, color='blue', label='Datos')


# Calculando los valores medios
mean_act = np.mean(act_scores)
mean_avg = np.mean(average_scores)

# Calculo de la pendiente (slope) y la intersección (intercept) de la recta
numerator = sum((act - mean_act) * (avg - mean_avg) for act, avg in zip(act_scores, average_scores))
denominator = sum((act - mean_act) ** 2 for act in act_scores)
slope = numerator / denominator
intercept = mean_avg - slope * mean_act

# Generacion de línea ajustada
line_x = np.array([min(act_scores), max(act_scores)])
line_y = slope * line_x + intercept

# Resultado
plt.plot(line_x, line_y, color='red', label=f' Ecuación de la recta es: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('Puntuación ACT')
plt.ylabel('Promedio de puntos')
plt.title(' Puntuación ACT y Promedio de Puntos')
plt.legend()
plt.show()