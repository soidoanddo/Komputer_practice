# 22. Знайти мінімальне значення функції, а також визначити значення аргументу, при якому воно досягається.

from library_11 import f5
from prettytable import PrettyTable


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


table = PrettyTable()
table.field_names = ['x', 'y']

i = 0
arr = {}
while i <= 22:
    y = f5(i)
    arr[i] = y
    table.add_row([round(i, 1), y])
    i = i+2.2

print(table, end="\n\n")

min_y = min([y for y in arr.values()])
print("Мінімальне значення у =", min_y,
      "\nАргумент (х) цього значення =", get_key(arr, min_y))


input()
