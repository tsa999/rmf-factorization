import time
import math
def factor(n):
    zp = 0
    y_max = math.isqrt(n) + 1
    t0 = time.time()
    for y in range(y_max, 1, -1):
        z = n % y
        if z == 0:
             print(f"Знайдено дільник: {y}")
             zp = 1
        y -= 1
    t1 = time.time()
    if zp == 0:
        return f"Число просте. Час факторизації: {t1 - t0:.2f} сек"
# Тест
n = 9361973132609
result = factor(n)
print("Result:",n, result)
