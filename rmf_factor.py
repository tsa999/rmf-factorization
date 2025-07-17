import time
import math
def rmf_factor(n):
    y_max = math.isqrt(n) + 1
    z_prev = n
    checked, skipped = 0, 0
    t0 = time.time()
    for y in range(y_max, 1, -1):
        z = n % y
        if z < z_prev:
            checked += 1
            if z == 0:
                print(f"Знайдено дільник: {y}")
                return y, n // y
        else:
            skipped += 1
        z_prev = z
    t1 = time.time()
    print(f"Checked: {checked}, Skipped: {skipped}, Time: {t1 - t0:.2f} sec")
    return None
# Приклад використання
n=100000000000031 # число яке треба розкласти
y = rmf_factor(n)
print("Result:", y)
