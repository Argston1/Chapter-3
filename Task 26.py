iterations = int(input("Введите количество итераций для вычисления числа π: "))
product = 1.0

for n in range(1, iterations + 1):
    product *= (2 * n) ** 2 / ((2 * n - 1) * (2 * n + 1))

pi_approximation = product * 2
print(f"Приблизительное значение числа π: {pi_approximation:.10f}")