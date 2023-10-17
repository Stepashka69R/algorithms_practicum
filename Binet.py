import math

def fib(n):
    if n <= 1:
        return n

    # Используем формулу Бине для вычисления n-го числа Фибоначчи
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2

    fib_n = (math.pow(phi, n) - math.pow(psi, n)) / sqrt_5

    # Округляем результат до ближайшего целого числа
    return round(fib_n)

# Пример использования
n = 32
result = fib(n)
print(f"fib({n}) = {result}")