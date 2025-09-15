import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4 * x ** 2 - 2 * x - 5


def golden_section_search(f, xl, xu, tol=1e-5):
    phi = (1 + np.sqrt(5)) / 2  # Altın oran
    resphi = 2 - phi

    x1 = xl + resphi * (xu - xl)
    x2 = xu - resphi * (xu - xl)
    f1, f2 = f(x1), f(x2)

    while abs(xu - xl) > tol:
        if f1 < f2:
            xu, x2, f2 = x2, x1, f1
            x1 = xl + resphi * (xu - xl)
            f1 = f(x1)
        else:
            xl, x1, f1 = x1, x2, f2
            x2 = xu - resphi * (xu - xl)
            f2 = f(x2)

    return (xl + xu) / 2


# Başlangıç aralığı
xl, xu = 1, 3
minimum_x = golden_section_search(f, xl, xu)
minimum_y = f(minimum_x)

# Fonksiyon grafiği çizme
x = np.linspace(0, 4, 100)
y = f(x)
plt.plot(x, y, label='f(x) = 4x² - 2x - 5')
plt.scatter(minimum_x, minimum_y, color='red', zorder=3, label=f'Minimum: ({minimum_x:.4f}, {minimum_y:.4f})')
plt.axvline(minimum_x, linestyle='dashed', color='gray', alpha=0.6)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Altın Bölme ile Minimum Noktanın Bulunması')
plt.legend()
plt.grid()
plt.show()

print(f"Minimum nokta: x = {minimum_x:.6f}, f(x) = {minimum_y:.6f}")
