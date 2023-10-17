def fib(n):
    fib_array = [0, 1] + [None] * (n - 1)
    for i in range(2, n + 1):
        if fib_array[i] is None:
            fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
    return fib_array[:n+1]

def main():
    n = 21  # Здесь можно изменить значение n на любое другое
    fib_result = fib(n)
    print(fib_result)

if __name__ == "__main__":
    main()