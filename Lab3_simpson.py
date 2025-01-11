# Расчет интеграла методом Симпсона
from math import cos

def func(x):
    return cos(x ** 2 - 1) / (x ** 2 + 2)

n = 4
m = n // 2
a = 1.2
b = 2.0
h = (b - a) / n
s1 = 0

for k in range(1, m + 1):
    s1 += func(a + (2 * k - 1) * h)

s2 = 0

for k in range (1, m):
    s2 += func(a + 2 * k * h)

s = (h / 3) * (func(a) + func(b) + 4 * s1 + 2 * s2)

print("Интеграл: " + str(s))
