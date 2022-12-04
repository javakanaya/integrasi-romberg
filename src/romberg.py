import math

# fungsi
def f(x):
    return math.exp(x)

# batas bawah dan atas
a = 0
b = 4

# integrasi trapezoid 
def trapEq(n, a, b):
    h = (b - a) / n
    x = a
    sum = f(x)
    for _ in range(1, n):
        x = x + h
        sum = sum + 2 * f(x)
    sum = sum + f(b)
    return (b - a) * sum / (2 * n)
