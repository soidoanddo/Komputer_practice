from math import sin, cos


def f24(x):
    return 10.8*abs(cos(x**2)/1.13)*sin(x+1.4)


def f25(x):
    return 11.2*cos(2*x-1)+abs(sin(1.5*x))/1.7


def f1(x):
    return 9.2*cos(x**2)-abs(sin(x)/1.1)


def f2(x):
    return 12.4*sin(abs(x/2.1))-8.3*cos(1.2*x)


def f3(x):
    return abs(cos(x/2.7))+9.1*sin(1.2*x+1)


def f4(x):
    return abs(sin(x)/3.12+cos(x**2))-8.3*sin(3*x)


def f5(x):
    return cos(abs(2*x))/1.12-cos(3*x-2) + 6.15


def f6(x):
    return sin(x)*cos(x**2)*sin(x+1.4)+5.14


def f7(x):
    return abs(sin(2*x-1.5)+3*sin(x**2))+2.38
