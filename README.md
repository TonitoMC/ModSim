# Laboratorio 1. Enjambres de Partículas
## 16 de Julio 2024
### Instrucciones
Mediante el uso de algoritmos de enjambre de partículas, resuelva el siguiente ejercicio.
Implemente un algoritmo de optimización de enjambre de partículas (PSO) para encontrar el mínimo de la función
𝑓(𝑥, 𝑦) = (𝑥 − 3) ** 2 + (𝑦 − 2) ** 2

Para ello considere lo siguiente:
1. Inicialice el enjambre con N = 40 partículas
2. Cada posición de partículas estará dentro del rango [-10, 10] tanto para x como y.
3. La velocidad deberá estar en el rango [-1, 1]
4. Establezca la mejor posición personal inicial de cada partícula en su posición inicial y la mejor posición
global en la mejor posición inicial de partícula.
5. Para cada partícula
a. Actualice su velocidad según lo visto en clase
b. Actualice su posición según lo visto en clase
6. Use inicialmente w=0.5, c1 = 1.5, c2 = 1.5
7. r1 y r2 son valores aleatorios entre 0 y 1 (recuerde usar seed)
8. Actualice la mejor posición personal si la nueva posición tiene un valor de función más bajo que la mejor
posición personal anterior,
9. Actualice la mejor posición global si la nueva posición tiene un valor de función más bajo que la mejor
posición global anterior.
10. Repita este proceso a lo sumo 100 veces o hasta que el cambio en el global sea menor a un threshold
definido por usted.
Recuerde graficar el contour plot de la función y mostrar la evolución de las partículas sobre este. Es decir, deberá
mostrar al menos 3 gráficas del inicio, algún punto medio y el final de su iteración para encontrar la solución. Nota,
la solución para esta función está en (3,2).

### Resultados
Luego de correr 20 iteraciones se encontró la partícula más apta en (2.999, 1.999),
mientras más iteraciones se toman se aproximan a (3,2) pero es más difícil observar las
partículas. Al establecer un threshold de 1e-10 para una cada coordenada con una población
de 40 partículas, tomó 76 iteraciones llegar a la aproximación.

Estado Inicial

![image](https://github.com/user-attachments/assets/c5cbe103-9f49-483e-8e23-9ef7b670b4ae)

Luego de 10 Iteraciones

![image](https://github.com/user-attachments/assets/4dfe290d-3600-4765-9bb5-65a9fc2a018d)

Luego de 20 Iteraciones

![image](https://github.com/user-attachments/assets/37794443-89da-4631-aa1c-1c73e3cec790)

