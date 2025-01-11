# Решение дифференциального уравнения
from math import cos, sin

def func(x, y):
    return sin(2 * x) * cos(7 * y) ** 2

def euler(x0, y0, h, k):
    xx = [0] * (k + 1)
    yy = [0] * (k + 1)
    xx[0] = x0
    yy[0] = y0

    print("Расчет методом Эйлера")
    for n in range(k + 1):
        print("n: " + str(n) + " xn: " + str(round(xx[n], 2)) + " yy: " + str(yy[n]))
        if n < k:
            xx[n + 1] = xx[n] + h
            yy[n + 1] = yy[n] + h * func(xx[n], yy[n])

def euler_mod(x0, y0, h, k):
    xx = [0] * (k + 1)
    yy = [0] * (k + 1)
    xx[0] = x0
    yy[0] = y0

    print("Расчет методом Эйлера (мод)")
    for n in range(k + 1):
        print("n: " + str(n) + " xn: " + str(round(xx[n], 2)) + " yy: " + str(yy[n]))
        if n < k:
            xx[n + 1] = xx[n] + h
            yy[n + 1] = yy[n] + h * func(xx[n] + h / 2, yy[n] + (h / 2) * func(xx[n], yy[n]))

def runge_kutt(x0, y0, h, k):
    xx = [0] * (k + 1)
    yy = [0] * (k + 1)
    xx[0] = x0
    yy[0] = y0

    print("Расчет методом Рунге-Кутта")
    for n in range(k + 1):
        print("n: " + str(n) + " xn: " + str(round(xx[n], 2)) + " yy: " + str(yy[n]))
        if n < k:
            xx[n + 1] = xx[n] + h
            z1 = h * func(xx[n], yy[n])
            z2 = h * func(xx[n] + h / 2, yy[n] + z1 / 2)
            z3 = h * func(xx[n] + h / 2, yy[n] + z2 / 2)
            z4 = h * func(xx[n] + h, yy[n] + z3)
            yy[n + 1] = yy[n] + (z1 + 2 * z2 + 2 * z3 + z4) / 6


x0 = 0
y0 = 0.143
euler(x0, y0, 0.1, 10)
euler_mod(x0, y0, 0.1, 10)
runge_kutt(x0, y0, 0.1, 10)
