# 4. Валидность скобок

# -*- coding:utf-8 -*-

string = list(input('Введите строку, содержащую символы “{“, “}”, “[“, “]”, “(“, “)”: '))

a1 = 0
a2 = 0
b1 = 0
b2 = 0
c1 = 0
c2 = 0

for item in string:
    if item == "{":
        a1 += 1
    if item == "{":
        a2 += 1
    if item == "[":
        b1 += 1
    if item == "]":
        b2 += 1
    if item == "(":
        c1 += 1
    if item == ")":
        c2 += 1

if a1 == a2 and b1 == b2 and c1 == c2:
    print("True")
else:
    print("False")