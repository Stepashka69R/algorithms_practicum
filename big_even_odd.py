def fib_eo(n):
    if n == 0:
        return "even"
    elif n == 1:
        return "odd"
    else:
        a, b = 0, 1  # Начальные значения F0 и F1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % 10  # Вычисляем следующую последнюю цифру Fn
        return "even" if b % 2 == 0 else "odd"

# Использование
n = 8424
result = fib_eo(n)
print(f"fib_eo({n}) = {result}")