print("************ example 1 (variables and data types) ************")
age = 25                                          # int - целое число
name = "Yaroslava"                                # str - строка
# int   - целые числа
# float - дробные числа
# str   - строки
# bool  - логический тип True / False
print()

print("************ example 2 (quotes inside string) ************")
said = "She said 'Hello'"                         # строка с одинарными кавычками внутри
print(said)                                       # She said 'Hello'
print()

print("************ example 3 (multiline string) ************")
my_string = '''This is a multy-line string.
We've wrapped the text to the next line'''        # многострочная строка
print(my_string)                                  # выводит текст в несколько строк
print()

print("************ example 4 (raw string) ************")
raw_string = r"C:\Program Files\Yaroslava\Python" # raw-строка: \ не обрабатывается как спецсимвол
print(raw_string)                                 # выводит путь как есть
print()

print("************ example 5 (type) ************")
s1 = "Hello Yaroslava"
print(type(s1))                                   # тип str
s2 = 5
print(type(s2))                                   # тип int
s3 = True
print(type(s3))                                   # тип bool
s4 = 2.0
print(type(s4))                                   # тип float
print()

print("************ example 6 (string concatenation) ************")
s5 = 'Zeleno'
s6 = 'glazka'
s7 = s5 + s6                                      # объединяет две строки
print(s7)                                         # Zelenoglazka
print()

print("************ example 7 (join) ************")
words = ["Hello", "World", "and", "Python"]
res = ",".join(words)                             # соединяет элементы списка через запятую
print(res)                                        # Hello,World,and,Python
print()

print("************ example 8 (string multiplication) ************")
st = "ab" * 7                                     # повторяет строку 7 раз
print(st)                                         # ababababababab
print()

print("************ example 9 (repeat symbol) ************")
st1 = 35 * '*'                                    # повторяет символ * 35 раз
print(st1)                                        # выводит 35 звёздочек
print()

print("************ example 10 (in operator with string) ************")
s1 = 'Kris Tomash'
s2 = 'Kristina'

if s2 in s1:
    print("User Kristina is in a DB")              # если строка найдена внутри s1
else:
    print("User Kristina is not in a DB")          # если строка не найдена
print()

print("************ example 11 (multiple comparisons with or) ************")
st = 'a'
if st == 'a' or st == 'b' or st == 'c' or st == 'd':
    print("Yes")                                   # проверяет несколько вариантов через or
print()

print("************ example 12 (in instead of multiple or) ************")
if st in 'abcd':
    print("Yes")                                   # проверяет наличие символа в строке
print()

print("************ example 13 (len) ************")
ln = len('Zelenoglazka')                          # считает количество символов
print(ln)                                         # 12

s1 = 'Zelenoglazka'
print(len(s1))                                    # 12
print()

print("************ example 14 (positive indexes) ************")
# 0 1 2 3 4 5
# P Y T H O N
st = 'Python'
print(st[0])                                      # P
print(st[1])                                      # y
print(st[2])                                      # t
print(st[3])                                      # h
print(st[4])                                      # o
print(st[5])                                      # n
# print(st[6])                                    # ошибка: такого индекса нет
print()

print("************ example 15 (negative indexes) ************")
# -6 -5 -4 -3 -2 -1
#  P  y  t  h  o  n
st = 'Python'

print(st[-1])                                     # n
print(st[-2])                                     # o
print(st[-3])                                     # h
print(st[-6])                                     # P
print()

print("************ example 16 (string slicing) ************")
st = 'Python'

print(st[0:3])                                    # Pyt
print(st[2:5])                                    # tho
print(st[4:6])                                    # on
print()

print("************ example 17 (slice with step) ************")
my_string = "Hello world"
every_second_char = my_string[::2]                # берет каждый второй символ
print(every_second_char)                          # Hlowrd
print()

print("************ example 18 (reverse string) ************")
reversed_string = my_string[::-1]                 # переворачивает строку, шаг -1
print(reversed_string)                            # dlrow olleH
print()

print("************ example 19 (slice from second character) ************")
from_second = my_string[1::2]                     # с индекса 1 берет каждый второй символ
print(from_second)                                # el ol
print()

print("************ example 20 (slice start stop step) ************")
my_substring = my_string[1:10:3]                  # start=1, stop=10, step=3
print(my_substring)                               # eoo
print()