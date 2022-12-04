import math
import numpy as np

# fungsi
def f(x):
    return math.exp(x)

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

# INISIASI
# batas bawah dan atas
a = 0
b = 4

# Matriks  
I = np.zeros((10, 10))

# Jumlah Trapezoid
i = 1

I[1,1] = trapEq(1, a, b)

# MATRIX I
# (1,1)(1,2)(1,3)(1,4)...
# (2,1)(2,2)(2,3)...
# (3,1)(3,2)...
# (4,1)...

# PERHITUNGAN
for _ in range(8):
    # menambah jumlah trapezoid
    n = 2 ** i

    # perkiraan/approx. integasi berikutnya
    # disimpan di kolom pertama baris baru
    I[i + 1, 1] = trapEq(n, a, b)

    # Integrasi Romberg
    for k in range(2, i + 2):
        j = 2 + i - k
        # mendapatkan nilai untuk kolom terkanan(terbaru)-baris pertama
        # dengan menggunakan nilai pada kolom-baris sebelumnya
        I[j, k] = (4 ** (k - 1) * I[j + 1, k - 1] - I[j, k - 1]) / (4 ** (k - 1) - 1)

    i += 1


print(I)
print("hasil akhir :", I[1, i])