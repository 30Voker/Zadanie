
import time
from functools import wraps

def measure_time(func):
    func
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Функция {func.__name__} выполнялась {end - start:.100f} секунд")

        return result

    return wrapper

@measure_time
def hello():
    return "Привет"

@measure_time
def calculate(a, b):
    return a + b

print(hello())
print(calculate(10, 20))
