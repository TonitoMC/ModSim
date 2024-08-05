import math
import random
import matplotlib.pyplot as plt
import numpy as np
# Variables globales (Parametros de la simulacion, modificables)
w = 0.5
c1 = 0.1
c2 = 1.5
random.seed(2024)


# Clase particula
class Particle:
    def __init__(self):
    # Genera aleatoriamente la posicion y velocidades iniciales
        self.x = random.uniform(-10, 10)
        self.y = random.uniform(-10, 10)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.best = (self.x, self.y)


    # Mide el fitness
    def fitness(self):
        return f(self.x, self.y)

    # Actualiza los valores necesarios, se repite cada "ciclo" antes de moverse
    def update(self, best_x, best_y):

        # Actualiza las velocidades
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        updated_xv = w * self.vx + c1 * r1 * (self.best[0] - self.x) + c2 * r2 * (best_x - self.x)
        updated_yv = w * self.vy + c1 * r1 * (self.best[1] - self.y) + c2 * r2 * (best_y - self.y)

        # Setea las velocidades
        self.vx = updated_xv
        self.vy = updated_yv

        # Actualiza las posiciones
        self.x += updated_xv
        self.y += updated_yv

        # Actualiza la mejor posicion de ser necesario
        if f(self.x, self.y) < f(self.best[0], self.best[1]):
            self.best = (self.x, self.y)


# Retorna el valor de la funcion de la que buscamos encontrar el minimo
def f(x, y):
    return (x - 3) ** 2 + (y - 2) ** 2

def plot(particles, first):
    # Crea cuadrícula de puntos
    if first:
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        xlim = (-10, 10)
        ylim = (-10, 10)
    else:
        x = np.linspace(1, 5, 100)
        y = np.linspace(0, 4, 100)
        xlim = (1, 5)
        ylim = (0, 4)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Plotear curvas de nivel
    plt.contour(X, Y, Z, levels=50, cmap='viridis')

    # Plotear partículas
    xlist = []
    ylist = []

    for p in particles:
        xlist.append(p.x)
        ylist.append(p.y)

    plt.plot(xlist, ylist, marker='.', linestyle='', color='b')

    plt.xlim(xlim) # Limitar ejes
    plt.ylim(ylim)

    # Agregar etiquetas y título
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Enjambre de partículas')
    plt.show()

#Llama la funcion swarm con plots en la 1ra y 10ma iteracion
def swarm(size, iterations):
    particles = []
    best_fitness = float('inf')
    best_coords = (None, None)
    # Crear partículas y tomar el mejor fitness
    for i in range(size):
        p = Particle()
        current_fitness = p.fitness()
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            best_coords = (p.x, p.y)
        particles.append(p)
    plot(particles, True)
    # Calculo inicial de los fitness, etc.
    for i in range(iterations):
        for p in particles:
            p.update(best_coords[0], best_coords[1])
            current_fitness = p.fitness()
            if current_fitness < best_fitness:
                best_fitness = current_fitness
                best_coords = (p.x, p.y)
        if i == 10:
            plot(particles, False)
    print(best_coords)
    plot(particles, False)

# Llama la funcion swarm y retorna la iteracion en la que se llega a un 1e-10 de aproximacion, se asume
# un maximo de 1000000 iteraciones para alcanzar el threshold
def swarm_threshold(size):
    particles = []
    best_fitness = float('inf')
    best_coords = (None, None)
    # Crear partículas y tomar el mejor fitness
    for i in range(size):
        p = Particle()
        current_fitness = p.fitness()
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            best_coords = (p.x, p.y)
        particles.append(p)
    # Calculo inicial de los fitness, etc.
    for i in range(1000000):
        for p in particles:
            p.update(best_coords[0], best_coords[1])
            current_fitness = p.fitness()
            if current_fitness < best_fitness:
                best_fitness = current_fitness
                best_coords = (p.x, p.y)
        if abs(best_coords[0] - 3) < 1e-10 and abs(best_coords[1] - 2) < 1e-10:
            return i

swarm(40,20)
print(f"Iteracion: {swarm_threshold(40)}")