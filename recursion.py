import time

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    n = 21    # Здесь можно изменить значение n на любое другое
    start_time = time.time()  # Замер времени начала выполнения
    result = fib(n)
    end_time = time.time()  # Замер времени окончания выполнения

    duration = (end_time - start_time) * 1000  # Преобразование времени в миллисекунды

    print(f"fib({n}) = {result}")
    print(f"Время выполнения: {duration:.6f} миллисекунд")

if __name__ == "__main__":
    main()