# 22.  Обчислити середні арифметичні всіх прибутків і збитків фірми.

from library_11 import f6
from prettytable import PrettyTable


arr = []
table = PrettyTable()
table.field_names = ['рік', 'величина доходу', 'Доход/збиток']
for x in range(1991, 2002):
    y = round(100 * f6(x), 2)
    arr.append(y)
    stat = "Доход" if y >= 0 else "Збиток"
    table.add_row([x, y, stat])
print(table, end="\n\n")

income_arr = [x for x in arr if x >= 0]
loss_arr = [x for x in arr if x < 0]

try:
    income_middle = round(sum(income_arr)/len(income_arr), 2)
    print("Середня арифметична прибутків =", income_middle)
except ZeroDivisionError:
    print("Компанія не мала прибутків")

try:
    loss_middle = round(sum(loss_arr)/len(loss_arr), 2)
    print("Середня арифметична збитків =", loss_middle)
except ZeroDivisionError:
    print("Компанія не мала збитків")


input()
