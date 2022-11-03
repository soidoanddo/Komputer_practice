# 22.1 кабельт Брит. =0. 183 км = 680 футів;

from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ["кабельт Брит.", "км", "фут"]

first_value = int(input("Початкове значення міри - "))
step = int(input("крок зміни цього значення - "))
strings = int(input("кількість рядків у таблиці - "))

for i in range(first_value, strings*step+1, step):
    table.add_row([i, round(i*0.183, 3), i*680])

print(table)

input()
