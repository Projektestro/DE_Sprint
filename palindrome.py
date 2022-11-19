# 2. Палиндром строки

# -*- coding:utf-8 -*-

string = input("Ведите строку: ")
reversedString = string[::-1]
if string == reversedString:
    print("Строка",string, "является палиндромом")
else:
    print("Строка", string, "не является палиндромом")
