from random import random
from math import factorial
from library_11 import f4


def precision(x):
    s = str(x)
    return (abs(s.find('.') - len(s)) - 1) >= 3


k = 1
ak = f4(k)/k
arr = [ak]
while True:
    k += 1
    ak = f4(k)/k
    arr.append(ak)
    q = arr[-2]/arr[-1]
    summa = arr[-1]/(1-q)
    if precision(summa):
        break

print("Перші елементи нескінченної послідовності: ", arr, "\nСума =",
      summa, "\nДодатків для досягнення заданої точності =", k, "\n")


k = 1
x = random()
while x == 0:
    x = random()
ak = (-1)**k*(f4(k)*x**k)/factorial(k)
arr = [ak]
while True:
    k += 1
    ak = (-1)**k*(f4(k)*x**k)/factorial(k)
    arr.append(ak)
    q = arr[-2]/arr[-1]
    summa = arr[-1]/(1-q)
    if precision(summa):
        break

print("Перші елементи нескінченної послідовності: ", arr, "\nСума =",
      summa, "\nДодатків для досягнення заданої точності =", k, "\n")

input()
