# Laboratorio 3. Método de Runge-Kutta para EDOs
## 30 de Juliio 2024
### Instrucciones
Mediante el uso del Método de Runge-Kutta resuelva los siguientes ejercicios

2.1 Crecimiento poblacional

Considere el modelo de crecimiento logístico dado por la ecuación diferencial:

𝑑𝑃/𝑑𝑡 = 𝑟𝑃 (1 − 𝑃/𝐾 )

Donde: P es la población en el tiempo, r es el ratio de crecimiento y K es la capacidad de carga

Dado:

● Población inicial P0 = 10

● Ratio de crecimiento r = 0.1

● Capacidad de carga K = 1,000

● Paso del tiempo h = 0.1

● Tiempo total T = 20

Use el método de 4to orden de Runge-Kutta para estimar la población sobre el tiempo y grafique los resultados. Interprete la gráfica y responda **¿cuál es el estimado de la población en tiempo T = 20?**

2.2 Depredador - Presa

Considere el modelo de depredador-presa de Lotka-Volterra, dado por las siguientes ecuaciones diferenciales

𝑑𝑅/𝑑𝑡 = ɑ𝑅 − β𝑅𝑃

𝑑𝑃/𝑑𝑡 = δ𝑅𝑃 − γ𝑃

Donde: R = es la población de la presa, P es la población de los depredadores, ɑ es el ratio de crecimiento natural de
la presa, β es el coeficiente del ratio de depredación, δ es ratio de reproducción de los depredadores por presa
comida, γ es el ratio de muerte de los depredadores

Dado:

● R0 = 40

● P0 = 9

● ɑ = 0.1

● β = 0.02

● δ = 0.01

● γ = 0.1

● Paso de tiempo h = 0.1

● Tiempo total T = 50

Utilice el método de cuarto orden de Runge-Kutta para estimar las poblaciones a lo largo del tiempo y trazar el
resultado. Interprete las gráficas y responda ¿cuál es el estimado de las poblaciones en tiempo T = 50?

### Resultados
Crecimiento Poblacional

![image](https://github.com/user-attachments/assets/685991ac-c46c-4237-ab64-63c70db2805b)

68.80 individuos estimados en T = 20

Depredador - Presa

![image](https://github.com/user-attachments/assets/1a4a780b-d1ca-40a0-bcce-7d3b2c87e1a3)

3.039 presas y 0.542 depredadores estimados en T = 50
