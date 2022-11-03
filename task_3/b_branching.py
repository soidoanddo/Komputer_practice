from library_11 import f24, f25, f1


work = input("Тип роботи = ")

if work == "А":
    money = round(100*abs(f24(22)+50), 2)
    tax = round(money*0.1, 2)
elif work == "Б":
    money = round(150*abs(f25(22)+100), 2)
    tax = round(money*0.15, 2)
elif work == "В":
    money = round(200*abs(f1(22)+135), 2)
    tax = round(money*0.2, 2)

for_issue = round(money-tax, 2)

print("Нарахована сума =", money, "\nПодаток =",
      tax, "\nДо видачі =", for_issue)

input()
