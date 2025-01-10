from math import sqrt

def func(x):
    return 1 / sqrt(2 * x ** 2 + 8)

n = 20
a = 0.5
b = 1.5
h = (b - a) / n
s = 0

for k in range(n):
    s = s + func(a + k * h)

s = (h / 2) * (func(a) + func(b) + 2 * s)

print("Интеграл: " + str(s))