# 5. Умножить два бинарных числа в формате строк

'''
На вход подаются две строки X1 и X2, содержащие бинарные числа.
Необходимо вывести их бинарное произведение в формате строки.
Пример 1:
Ввод: x1 = ‘’111” и x2= “101”
Вывод: “100011”
Пояснение: “111” - это 7; “101” - это 5; 7*5 = 35; 35 в двоичной системе 100011
Гарантируется, что введенная строка X будет содержать только числа 1 и 0.
'''

binary1 = input("Введите первое число в двоичной системе: ")
binary2 = input("Введите второе число в двоичной системе: ")

binary1Reversed = binary1[::-1]
binary2Reversed = binary2[::-1]

decimal1 = 0
decimal2 = 0

for i in range(len(binary1Reversed)):
    decimal1 += (int(binary1Reversed[i]) * (2 ** i))

for i in range(len(binary2Reversed)):
    decimal2 += (int(binary2Reversed[i]) * (2 ** i))

multiply = bin(decimal1 * decimal2)

multiplyList = list()
for item in multiply:
    multiplyList.append(item)

for i in range(2, len(multiplyList)):
    print(multiplyList[i], end="")