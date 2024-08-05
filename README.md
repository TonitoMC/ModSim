# Laboratorio 2. Método de Euler para EDOs
## 23 de Julio 2024
### Instrucciones
Mediante el uso del Método de Euler resuelva los siguientes ejercicios

2.1 Crecimiento poblacional

Considere el siguiente modelo de crecimiento poblacional

𝑑𝑦/𝑑𝑥 = 𝑘 (1 − 𝑦/𝑁 ) 𝑦

Después de 4 días, una población inicial de mariposas de 15 crece a 56. Si el ecosistema restringido alberga 300
mariposas, ¿cuántas mariposas habrá en 12 días? Suponiendo que la población de mariposas crece más rápido
cuando hay 150 mariposas, ¿cuándo sucede esto?

2.2 Crecimiento Epidemiológico

En un pueblo aislado se propaga una enfermedad según el modelo SIR. Inicialmente hay 990 individuos
susceptibles (S), 10 individuos infectados (I) y 0 individuos recuperados (R). La tasa de infección (𝛽) es 0.3 y la tasa
de recuperación (𝛾) es 0.1. Utilizando el método de Euler, estime el número de individuos susceptibles, infectados y
recuperados durante un período de 50 días. Utilice un tamaño de paso (Δt) de 0.1 días.

Nota: Asegúrese de que las poblaciones nunca sean cero. Además, calcule las derivadas adecuadamente dentro
del ciclo.

### Resultados
Crecimiento Poblacional

![image](https://github.com/user-attachments/assets/60020328-4cb7-49d4-9089-e75a4d40dabb)

Valor más apropiado de k: 0.368

Población luego de 12 días: 243.933

Días transcurridos cuando la población alcanza 150: 8.02

Modelo SIR

![image](https://github.com/user-attachments/assets/24f08e5b-c9ab-48e0-9118-1ed93671fb0a)
