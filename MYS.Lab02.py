import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Ejercicio 1.

# Parametros del modelo
N = 300 # Poblacion maxima
y0 = 15 # Valor inicial de la poblacion
obj_y = 56 # Valor objetivo de la poblacion
obj_x = 4 # Valor objetivo de dias transcurridos

# Retorna el valor de Dy/Dx segun la ecuacion diferencial
def pop_growth(k, y, N):
    return k * (1 - y / N) * y

# Metodo de Euler que retorna la poblacion estimada luego de una cantidad de tiempo especifica
def euler_x(k, y0, obj_x, h):
    # Tiempo transcurrido inicia en 0 y la poblacion inicial es la establecida
    x = 0
    y = y0
    # Actualiza usando y = y + h * pendiente, para a una iteracion de alcanzar el limite en X
    while x < obj_x:
        slope = pop_growth(k, y, N)
        y += slope * h
        x += h
    return y

# Metodo de Euler que retorna la cantidad de tiempo transcurrida para una poblacion especifica
def euler_y(k, y0, obj_y, h):
    # Tiempo transcurrido inicia en 0 y la poblacion inicial es la establecida
    x = 0
    y = y0
    # Actualiza usando y = y + h * pendiente, para a una iteracion de alcanzar el limite en Y
    while y < obj_y:
        slope = pop_growth(k, y, N)
        y += slope * h
        x += h
    return x

# Evalua el fitness de un valor k basado en la poblacion esperada luego de 4 dias transcurridos
def k_test(k):
    return euler_x(k, y0, obj_x, 0.01) - obj_y

# Utiliza fsolve para encontrar el valor óptimo de k
best_k = fsolve(k_test, 0.1)[0]
print(f"Valor más apropiado de k: {best_k}")

# Calcula la cantidad de mariposas luego de 12 días
pop_12days = euler_x(best_k, y0, 12, 0.01)

# Calcula la cantidad de mariposas luego de 12 dias
pop_12days = euler_x(best_k, y0, 12, 0.01)
print(f"Poblacion luego de 12 dias: {pop_12days}")

# Calcula el tiempo transcurrido cuando la poblacion alcanza 150
pop_150 = euler_y(best_k, y0, 150, 0.01)
print(f"Dias transcurridos cuando la poblacion alcanza 150: {pop_150}")

# Grafica de los resultados
times = np.arange(0, 15 + 0.01, 0.01)
populations = [euler_x(best_k, y0, t, 0.01) for t in times]
plt.plot(times, populations)
plt.scatter([12], pop_12days, color='red', label='Poblacion a los 12 Dias')
plt.scatter(pop_150, 150, color='green', label='Tiempo en Alcanzar 150')
plt.xlabel('Tiempo (dias)')
plt.ylabel('Poblacion')
plt.legend()
plt.title('Crecimiento Poblacional - Euler')
plt.show()


# Ejercicio 2.

# Parametros del modelo ISR
b = 0.3 # Tasa de infeccion
g = 0.1 # Tasa de recuperacion
s0 = 990 # Población inicial de susceptibles
i0 = 10  # Población inicial de infectados
r0 = 0 # Población inicial de recuperados
dt = 0.1 # Tamaño de paso
N = 1000 # Tamaño de paso
t_final = 50 # Duracion del periodo en días

# Calcula la siguiente poblacion de susceptibles
def s_next(s, dt, b, i):
    return s + dt * (-b * s * i) / N

# Calcula la siguiente poblacion de infectados
def i_next(i, dt, b, s, g):
    return i + dt * (b * s * i / N - g * i)

# Calcula la siguiente poblacion de recuperados
def r_next(r, dt, i, g):
    return r + dt * (g * i)

# Corre la simulacion del modelo ISR y retorna informacion sobre la poblacion conforme cada paso
def euler_SIR(b, g, s0, i0, r0, dt, t_final):
    # Listas para almacenar valores
    time_points = []
    s_points = []
    i_points = []
    r_points = []
    #Parametros iniciales
    t = 0
    s = s0
    i = i0
    r = r0
    # Mientras el tiempo sea menor o igual al tiempo final
    while t <= t_final:
        # Almacena la información para poder graficarlo
        time_points.append(t)
        s_points.append(s)
        i_points.append(i)
        r_points.append(r)
        # Se crean valores temporales para asegurarnos que se calculen de manera apropiada los valores
        s_temp = s_next(s, dt, b, i)
        i_temp = i_next(i, dt, b, s, g)
        r_temp = r_next(r, dt, i, g)
        # Asegura que las poblaciones nunca sean negativas
        s = max(s_temp, 0)
        i = max(i_temp, 0)
        r = max(r_temp, 0)
        t += dt
    return time_points, s_points, i_points, r_points

time_points, s_points, i_points, r_points = euler_SIR(b, g, s0, i0, r0, dt, t_final)

# Graficar los resultados
plt.plot(time_points, s_points, label='Susceptibles')
plt.plot(time_points, i_points, label='Infectados')
plt.plot(time_points, r_points, label='Recuperados')
plt.xlabel('Días')
plt.ylabel('Número de personas')
plt.title('Modelo SIR - Euler')
plt.legend()
plt.grid(True)
plt.show()