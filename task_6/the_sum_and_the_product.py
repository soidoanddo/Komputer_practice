# 22) z = 2х - у;

from library_11 import f2, f3

x, y = 0, 1
for k in range(1, 28):
    x += f2(k)
    y *= f3(k)

z = 2*x-y

print("x =", x, "\ny =", y, "\nz =", z)

input()
