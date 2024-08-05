import matplotlib.pyplot as plt

# Ejercicio 1.

# Parametros del modelo
p0 = 10  # Poblacion inicial
r = 0.1  # Ratio de crecimiento
k = 1000  # Capacidad de carga
h = 0.1  # Paso en el tiempo
t_max = 20  # Tiempo total


# Retorna el valor de dp/dt segun la ecuacion diferencial
def pop_growth(p, r, k):
    return r * p * (1 - p / k)


# Retorna listas con valores de tiempo y poblaciones estimados utilizando RK4
def rk4_pop_growth(r, k, p0, h, t_max):
    # Variables iniciales
    t = 0
    p = p0
    time_points = []
    populations = []
    while t < t_max:
        time_points.append(t)
        populations.append(p)

        # Se estiman k1, k2, k3 y k4.
        k1 = h * pop_growth(p, r, k)
        k2 = h * pop_growth(p + k1 / 2, r, k)
        k3 = h * pop_growth(p + k2 / 2, r, k)
        k4 = h * pop_growth(p + k3, r, k)

        # Se actualiza la poblacion y el tiempo
        p += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h

    return time_points, populations


# Llama la funcion, imprime poblacion final y crea grafica
time_points, populations = rk4_pop_growth(r, k, p0, h, t_max)

print(f"La poblacion en el tiempo T = 20 es aproximadamente: {populations[-1]}")

plt.plot(time_points, populations)
plt.xlabel('Tiempo')
plt.ylabel('Poblacion')
plt.title('Crecimiento Poblacional - RK4')
plt.show()

# Ejercicio 2.

# Parametros del modelo
r0 = 40  # Poblacion inicial presa
p0 = 9  # Poblacion inicial depredador
a = 0.1  # Ratio de crecimiento natural de la presa
b = 0.02  # Ratio de depredacion
d = 0.01  # Ratio de reproduccion de depredadores por presa comida
g = 0.1  # Ratio de muerte de los depredadores
h = 0.1  # Paso en el tiempo
t_max = 50  # Tiempo final


# Ecuaciones diferenciales Lotka-Volterra

# Retorna el valor de dr/dt segun la ecuacion diferencial
def dr_dt(r, p, a, b):
    return a * r - b * r * p


# Retorna el valor de dp/dt segun la ecuacion diferencial
def dp_dt(r, p, g, d):
    return d * r * p - g * p


# Retorna listas con valores de tiempo y poblaciones estimados utilizando RK4
def rk4_lv(r0, p0, h, t_max, a, b, d, g):
    # Variables iniciales
    t = 0
    r = r0
    p = p0
    time_points = []
    prey_populations = []
    predator_populations = []
    while t < t_max:
        time_points.append(t)
        prey_populations.append(r)
        predator_populations.append(p)

        # Ya que dr/dt y dp/dt ambos dependen de "r" y "t", se calcula cada "paso" respectivamente para utilizar
        # en la siguiente iteracion como establece el metodo RK4
        k1_r = h * dr_dt(r, p, a, b)
        k1_p = h * dp_dt(r, p, g, d)

        k2_r = h * dr_dt(r + k1_r / 2, p + k1_p / 2, a, b)
        k2_p = h * dp_dt(r + k1_r / 2, p + k1_p / 2, g, d)

        k3_r = h * dr_dt(r + k2_r / 2, p + k2_p / 2, a, b)
        k3_p = h * dp_dt(r + k2_r / 2, p + k2_p / 2, g, d)

        k4_r = h * dr_dt(r + k3_r, p + k3_p, a, b)
        k4_p = h * dp_dt(r + k3_r, p + k3_p, g, d)

        # Se actualizan los valores de r, p, t
        r += (k1_r + k2_r * 2 + k3_r * 2 + k4_r) / 6
        p += (k1_p + k2_p * 2 + k3_p * 2 + k4_p) / 6
        t += h
    return time_points, prey_populations, predator_populations


# Llama la funcion, imprime las poblaciones finales y grafica los resultados
time_points, prey_populations, predator_populations = rk4_lv(r0, p0, h, t_max, a, b, d, g)

print(f"En T = 50 hay {prey_populations[-1]} presas y {predator_populations[-1]} depredadores")

plt.figure(figsize=(12, 6))
plt.plot(time_points, prey_populations, label='Poblacion de Presas')
plt.plot(time_points, predator_populations, label='Poblacion de Depredadores')
plt.xlabel('Tiempo')
plt.ylabel('Poblacion')
plt.title('Lotka-Volterra RK4')
plt.legend()
plt.show()
