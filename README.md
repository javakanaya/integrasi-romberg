# Integrasi Romberg

> Praktikum 2 Komputasi Numerik

## **Kelompok 9**
- Java Kanaya Prada - 5025211112
- Adrian Ismu Arifianto - 5025211116
- Afiq Fawwaz Haidar - 5025211246

## Penjelasan Integrasi Romberg

![image](https://user-images.githubusercontent.com/70834506/208913594-adb379b9-5a81-47f5-903c-a6391ff532c9.png)

Function diatas berfungsi untuk mendapatkan nilai dari `F(x)` yang digunakan dalam Integrasi Romberg. Dalam demo praktikum ini, kami menggunakan fungsi `F(x) = e^x` sebagai contoh yang akan diimplementasikan ke dalam Integrasi Romberg

![image](https://user-images.githubusercontent.com/70834506/208913942-67267733-e1d3-4eb9-b5cc-ea6e8fafb46e.png)

Function diatas berfungsi untuk mendapatkan nilai dari Metode Trapezoida dengan :
>`n` sebagai jumlah pias yang digunakan\
`a` sebagai slope bawah\
`b` sebagai slope atas\
`h` sebagai lebar pias

Yang mengimplementasikan rumus berikut

![image](https://user-images.githubusercontent.com/70834506/208916277-00cff3a3-32d2-4ac9-99f4-6f1f906f2f03.png)

![image](https://user-images.githubusercontent.com/70834506/208916693-7522093d-c409-4ac0-956b-c2532b6dd219.png)

Function diatas berfungsi untuk mendapatkan nilai dari Integrasi Romberg. Iterasi dalam Integrasi Romberg dinyatakan dalam Matrix `j x k` dimana `j = k = i`, dengan `i` adalah jumlah iterasi yang dilakukan pada Integrasi Romberg

>(1,1) (1,2) (1,3) … (1,i)\
(2,1) (2,2) … (2,i-1)\
...\
(i,1)

Lalu carilah nilai integral Trapezoida pada masing-masing index matrix dengan rumus berikut

![image](https://user-images.githubusercontent.com/70834506/208927463-504ad6d3-cb3a-4422-ba0d-0f0215937280.png)

Iterasi dilakukan sebagai berikut

> Iterasi 1 : `I(1,1)`\
Iterasi 2 : `I(1,1)` & `I(2,1)` → `(1,2)`\
Iterasi 3 :`I(2,1)` & `I(3,1)` → `I(1,2)` & `I(2,2)` → `I(3,1)`\
...\
Iterasi i :`I(i-1,1)` & `I(i,1)` → `I(i-2,2)` & `I(i-1,2)` → ⋯ → `I(1,i)`

Sehingga didapatkan hasil Integrasi dengan tingkat error paling kecil pada `I(1,i)`
