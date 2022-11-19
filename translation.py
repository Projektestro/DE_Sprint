# 3. Перевод арабского числа в римское

# -*- coding:utf-8 -*-

roman = {"1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}

arabic = int(input("Введите целое положительное число от 1 до 2000: "))
print("Введенное вами число в римской записи: ", end="")

if arabic // 1000 > 0:
    print(arabic // 1000 * "M", end="")

if arabic % 1000 >= 900:
    print("CM", end="")

elif 900 > arabic % 1000 >= 500:
    print("D", end="")
    print(((arabic % 500) // 100) * "C", end="")

elif arabic % 1000 >= 500:
    print("D", end="")

elif arabic % 1000 >= 400:
    print("CD", end="")

else:
    print((arabic % 100) // 100 * "C", end="")

if arabic % 100 >= 90:
    print("XC", end="")

elif 90 > arabic % 100 >= 50:
    print("L", end="")
    print(((arabic % 50) // 10) * "X", end="")

elif arabic % 100 >= 50:
    print("L", end="")

elif arabic % 100 >= 40:
    print("XL", end="")

else:
    print((arabic % 100) // 10 * "X", end="")

if arabic % 10 > 0:
    print(roman[str(arabic % 10)])