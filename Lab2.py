from math import sin, pi

def func(x):
    return 2 * sin(x)

m1 = m2 = 2
x0 = pi / 4
eps = 0.001

print("По первой формуле верхний порог для h = " + str((6 * eps / m1) ** 0.5))
h1 = float(input("Введите желаемое h: "))
diff1 = (func(x0 + h1) - func(x0 - h1)) / (2 * h1)
print("Производная, вычисленная по первой формуле: " + str(diff1) + "\n")

print("По второй формуле верхний порог для h = " + str((30 * eps / m2) ** 0.25))
h2 = float(input("Введите желаемое h: "))
diff2 = (func(x0 - 2 * h2) - 8 * func(x0 - h2) + 8 * func(x0 + h2) - func(x0 + 2 * h2)) / (12 * h2)
print("Производная, вычисленная по второй формуле: " + str(diff2) + "\n")
