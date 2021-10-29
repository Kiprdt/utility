import math


def sh():
    print("Вычисление средней информации на знак.")
    print("Введите число, либо '1', чтобы закончить ввод.")
    a = float(input("Ввод:"))
    b = 0
    while a != 1:
        b += -a * math.log2(a)
        a = float(input("Ввод:"))
    print(b)


sh()
