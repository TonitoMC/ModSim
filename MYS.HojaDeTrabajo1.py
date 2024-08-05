import math
import random

import matplotlib.pyplot as plt
import numpy as np

# 1. Definicion de Funcion Objetivo

# Funcion a maximizar
def fx(x:float) -> float:
    return x * math.sin(10 * math.pi * x) + 1

# Mapeo de numeros enteros representados por cadenas de 32 bits a reales en [0,1]
def mapTo0_1(x):
    number = int(x,2)
    return (1 / ((2**32) - 1)) * number

# 2. Inicializacion de poblacion inicial respecto a los parametros
def generate_random(count):
    u32_min = 0
    u32_max = 2**32 - 1
    u32_numbers_binary = [
        format(random.randint(u32_min, u32_max), '032b') for _ in range(count)
    ]
    return u32_numbers_binary

# 3. Evalua la aptitud de la funcion
def fitness(pop):
    fit_dict = {}
    for s in pop:
        fit_dict.update({s: fx(mapTo0_1(s))})
    return fit_dict

# 4. Seleccion proporcional a la aptitud
def roulette_wheel(fit_dict):
    total_fit = sum(fit_dict.values())
    pick = random.uniform(0, total_fit)
    current = 0
    for key, value in fit_dict.items():
        current += value
        if current > pick:
            return key

# 5. Crossover, divide las cadenas de bits en 4 segmentos y selecciona aleatoriamente un segmento para agregar al hijo 

def crossover(parent1, parent2):
    arrayp1 = [parent1[:8], parent1[8:16], parent1[16:24], parent1[24:32]]
    arrayp2 = [parent2[:8], parent2[8:16], parent2[16:24], parent2[24:32]]
    output = ""
    for i in range(4):
        select = random.choice([1, 2])
        if select == 1:
            output += arrayp1[i]
        else:
            output += arrayp2[i]
    return output

# 6. Mutacion, 0.2 de probabilidad que se de vuelta un bit
def mutacion(binario):

    if random.uniform(0,1) > 0.8:
        return binario
    
    bit_a_mutar = random.randint(0, len(binario) - 1)

    binario_list = list(binario)

    if binario_list[bit_a_mutar] == "0":
        binario_list[bit_a_mutar] = "1"

    else:
        binario_list[bit_a_mutar] = "0"

    binario_mutado = "".join(binario_list)

    return binario_mutado

# 7-10, funcion principal genetic_algo
def genetic_algo(iterations, pop_size, elitism_rate):
    # Inicializa Poblacion
    current_gen = generate_random(pop_size)
    best_fitness = []
    for i in range(iterations):
        # Evalua la aptitud
        fit_dict = fitness(current_gen)
        # Elitismo, mantiene los mejores candidatos
        sorted_pop = sorted(
            current_gen, key=lambda x: fit_dict[x], reverse=True)
        num_elites = int(pop_size * elitism_rate)
        elites = sorted_pop[:num_elites]
        best_candidate = elites[0]
        highest_fitness = fit_dict[best_candidate]
        best_fitness.append(highest_fitness)
        print(
            f"Iteracion: {i}, Candidato: {
                best_candidate}, Fitness: {highest_fitness}"
        )
        new_gen = elites[:]
        while len(new_gen) < pop_size:
            parent1 = roulette_wheel(fit_dict)
            parent2 = roulette_wheel(fit_dict)
            offspring = crossover(parent1, parent2)
            mutated_offspring = mutacion(offspring)
            new_gen.append(mutated_offspring)
        current_gen = new_gen
    # Plot
    plt.figure()
    plt.plot(range(iterations), best_fitness, marker=".", linestyle="-")
    plt.title("Evolucion de Fitness")
    plt.xlabel("Numero de Iteracion")
    plt.ylabel("Mejor Fitness")
    plt.grid(True)
    plt.show()

genetic_algo(500,1000,0.6)