def func(x):
    return (3 * x ** 2 + 5) / (x ** 2 + 2) # Исходная функция

def deriv(x):
    return (2 * x) / (x ** 4 + 4 * x ** 2 + 4)

def swann(x0, delta):
    print("Расчет по алгоритму Свенна...")
    x1 = x0
    x2 = x1 + delta
    if func(x1) < func(x2):
        delta = -delta
        #x1 = x0
        x2 = x1 + delta

    while func(x2) < func(x1):
        delta *= 2
        x1 = x2
        x2 = x1 + delta
        print("x1: " + str(x1) + " , f(x1): " + str(func(x1)))
        print("x2: " + str(x2) + " , f(x2): " + str(func(x2)) + ' ' + str(func(x2) - func(x1)) + '\n')

    a = x2 - (3 * delta) / 2
    b = x2 - delta / 2

    if a > b: a, b = b, a # Гарантируем меньшее значение в переменной a

    print("a: " + str(a))
    print("b: " + str(b))

    return [a , b]

def dichotomy(a, b, delta):
    print("Расчет по методу дихотомии...")
    
    while ((abs(b) - abs(a)) / 2) > 0.001 and deriv(abs(a) - abs(b) / 2) > 0.01:
        checker = (abs(b) - abs(a)) / 2
        checker2 = 1
        x = (a + b - delta)/2
        y = (a + b + delta)/2
        print("i x: %8.5f, y: %8.5f,  L: %8.5f" % (x, y, abs(b - a)))
        if func(x) < func(y):
            b = y
        else:
            a = x
    print("[%8.5f; %8.5f] = %8.5f" % (a, b, (a + b) / 2))

dichotomy(*swann(-5, 0.1), delta=0.1)