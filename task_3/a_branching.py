from math import tan, log, exp
from library_11 import f24, f25


x = float(input('x = '))

# if abs(x) < 10:
#     a = float(input('a = '))
#     b = float(input('b = '))
#     f = tan(x+a)-log(abs(b+7), 22)
#     print(f24(f))
# else:
#     if abs(x) >= 10:
#         c = float(input('c = '))
#         d = float(input('d = '))
#         f = c**5*(x**2 + d*exp(1.3))**0.5
#         print(f25(f))
#     else:
#         pass


if abs(x) < 10:
    a = float(input('a = '))
    b = float(input('b = '))
    f = tan(x+a)-log(abs(b+7), 22)
    print(f24(f))
else:
    c = float(input('c = '))
    d = float(input('d = '))
    f = c**5*(x**2 + d*exp(1.3))**0.5
    print(f25(f))


input()
