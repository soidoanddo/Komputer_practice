# 22.  Створити масив, значення якого знаходяться між значенням третього елемента заданого масиву і максимальним значенням.

from library_11 import f7

arr = []
for k in range(1, 8):
    y = f7(k)
    arr.append(y)
print("Масив у: ", arr)

max_index = arr.index(max(arr))

if max_index < 2:
    task_arr = arr[max_index:3]
elif max_index > 2:
    task_arr = arr[2:max_index+1]
else:
    task_arr = [arr[max_index]]

print("Масив значень від 3-го до максимального значення: ", task_arr)


input()
