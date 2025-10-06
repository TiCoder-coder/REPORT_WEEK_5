import functools
import time
def timeit(fn):
    functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            end = time.perf_counter() - start
            print(f"\nTime: {end:.4f} seconds.")
    return wrapper
@timeit
def fibonacci(numberOfFIbonacci):
    fibo = [0, 1]
    for i in range(numberOfFIbonacci - 2):
        fibo.append(fibo[i] + fibo[i+1])
    for i in fibo:
        print(i, end = " ")
print(fibonacci(10))
