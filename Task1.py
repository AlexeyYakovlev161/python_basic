'''
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните
в переменные, выведите на экран.
'''

a = 10
b = 15
print("Переменные a и b - ", a, b)
string1 = input("Введите первую строку ")
number1 = int(input("Введите первое число "))
string2 = input("Введите вторую строку ")
number2 = int(input("Введите второе число "))
print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))

n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
x = int(input())
if x == 0:
count_zero += 1
else:
count_one += 1
if count_one > count_zero:
print(count_zero)
else:
print(count_one