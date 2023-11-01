def fib_eo(n):
    return "even" if n % 3 == 0 else "odd"


n = 658480
print("n =", n, "is", fib_eo(n))  # выводит "odd" или "even"