# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini

print("Menghitung Rata-Rata")

a = eval(input("Masukan data ke-1: "))
b = eval(input("Masukan data ke-2: "))
c = eval(input("Masukan data ke-3: "))
d = eval(input("Masukan data ke-4: "))
e = eval(input("Masukan data ke-5: "))
jum = (a + b + c + d + e) / 5
print("rata-rata dari", a, ",", b, ",", c, ",", d, ",", "dan", e, "adalah",
      jum)
print("====================================================")

# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini

print("Kelipatan Bilangan")

a = int(input("masukan sebuah bilangan bulat: "))
b = 10
for i in range(a, b * a + 1, b):
    print(i, end="--")
print(" ")
print("====================================================")
