import time
import math

def factor(n):
    found = False
    y_max = math.isqrt(n) + 1
    t0 = time.time()
    for y in range(y_max, 1, -1):
        if n % y == 0:
            print(f"Знайдено дільник: {y}, другий: {n // y}")
            found = True
    t1 = time.time()
    if not found:
        return f"Число просте. Час факторизації: {t1 - t0:.2f} сек"
    else:
        return f"Час факторизації: {t1 - t0:.2f} сек"

# Тест
n = 9361973132609 
result = factor(n)
print("Result:", n, result)
