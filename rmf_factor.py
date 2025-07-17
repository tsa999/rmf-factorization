import time
import math
def rmf_factor(n):
    """
    RMF (Remainder-Minimum Factorization) — евристичний метод пошуку дільників великих чисел.
    Працює на основі аналізу спадання залишку при зворотному русі по y.
    """
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
if __name__ == "__main__":
    n = 100000000000031
    y = rmf_factor(n)
    print("Result:", y)
