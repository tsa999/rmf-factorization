import time
import math

def rmf_factor(n):
    """
    Евристичний алгоритм розкладання числа на множники.
    Пропускає дільники, якщо бачить локальний максимум залишку.
    """
    y_max = math.isqrt(n) + 1
    z_prev = n
    t0 = time.time()
    y = y_max

    while y > 2:
        z = n % y
        y_next = y - 1
        z_next = n % y_next if y_next > 1 else n

        if z == 0:
            print(f"Знайдено дільник: {y}")
            return y, n // y

        # Зменшений і обмежений адаптивний крок
        if z > z_prev and z < z_next:
            skip = 2  # мінімальний, безпечний стрибок
            y -= skip
        else:
            y -= 1

        z_prev = z

    t1 = time.time()
    print(f"Число просте. Час: {t1 - t0:.2f} сек")
    return None

# Тест на складеному числі
n = 10004983 * 10004719
result = rmf_factor(n)
print("Result:", result)
