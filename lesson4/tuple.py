print("************ example 1 (create tuple) ************")
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 9)          # кортеж с числами
my_tuple = ([1, 2, 3], ['a', 'b', 'c'])           # кортеж со списками внутри
print(numbers_tuple)                               # выводит кортеж с числами
print(my_tuple)                                    # выводит кортеж со списками
print()

print("************ example 2 (get element by index) ************")
first_element = numbers_tuple[0]                   # получает первый элемент по индексу 0
print(first_element)                               # выводит первый элемент
print()

print("************ example 3 (nested tuple) ************")
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])                             # выводит вложенный кортеж (3, 4)
print(nested_tuple[2][1])                          # выводит элемент 4 из вложенного кортежа
print()

print("************ example 4 (compare tuples) ************")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (4, 5, 3)
print(tuple1 == tuple2)                            # сравнивает кортежи, выводит True
print(tuple1 == tuple3)                            # сравнивает кортежи, выводит False
print()

print("************ example 5 (in operator) ************")
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)                               # проверяет наличие элемента 3, выводит True
print()

print("************ example 6 (for loop) ************")
for el in my_tuple:
    print(el)                                      # по очереди выводит каждый элемент кортежа
print()

print("************ example 7 (while loop) ************")
i = 0
while i < len(my_tuple):
    print(my_tuple[i])                             # выводит элемент по текущему индексу
    i += 1                                         # увеличивает индекс на 1
print()

print("************ example 8 (delete tuple) ************")
# del my_tuple                                     # полностью удаляет переменную с кортежем
# print(my_tuple)                                  # вызовет ошибку, так как переменная удалена
print()

print("************ example 9 (combine tuples) ************")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
conc_tuple = tuple1 + tuple2                       # объединяет два кортежа
print(conc_tuple)                                  # выводит объединённый кортеж
print()

print("************ example 10 (len) ************")
my_tuple = (1, 2, 3, 4, 5)
length_of_tuple = len(my_tuple)                    # считает количество элементов
print(length_of_tuple)                             # выводит длину кортежа
print()

print("************ example 11 (sum) ************")
sum_of_elements = sum(my_tuple)                    # считает сумму всех элементов
print(sum_of_elements)                             # выводит сумму элементов
print()

print("************ example 12 (max and min) ************")
max_element = max(my_tuple)                        # находит максимальный элемент
min_element = min(my_tuple)                        # находит минимальный элемент
print(max_element)                                 # выводит максимальный элемент
print(min_element)                                 # выводит минимальный элемент
print()

print("************ example 13 (empty tuple) ************")
my_tuple1 = ()
print(len(my_tuple1))                              # выводит длину пустого кортежа: 0
print(sum(my_tuple1))                              # выводит сумму пустого кортежа: 0
# print(max(my_tuple1))                            # ошибка: нельзя найти max в пустом кортеже
# print(min(my_tuple1))                            # ошибка: нельзя найти min в пустом кортеже
print()


print("************ example 14 (sort tuple) ************")
original_tuple = (3, 1, 4, 5, 9, 2, 6, 5, 5, 3)
sorted_tuple = tuple(sorted(original_tuple))       # сортирует элементы и преобразует результат обратно в кортеж
print("original: ", original_tuple)                # выводит исходный кортеж
print("sorted: ", sorted_tuple)                    # выводит отсортированный кортеж
print()

print("************ example 15 (tuple slicing) ************")
sub_tuple = original_tuple[3:7]                    # берет элементы с индекса 3 до 6
print(sub_tuple)                                   # выводит часть кортежа
print()

print("************ example 16 (tuple to list) ************")
my_tuple = list(original_tuple)                    # преобразует кортеж в список
print(my_tuple)                                    # выводит список
print()

print("************ example 17 (tuple to string) ************")
my_string = ''.join(map(str, original_tuple))      # преобразует числа в строки и соединяет их
print(my_string)                                   # выводит строку из элементов кортежа
print()

print("************ example 18 (change tuple through list) ************")
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)                           # преобразует кортеж в список
my_list[2] = 10                                    # изменяет элемент по индексу 2
updated_tuple = tuple(my_list)                     # преобразует список обратно в кортеж
print("original_tuple: ", my_tuple)                # выводит исходный кортеж
print("updated_tuple: ", updated_tuple)            # выводит обновлённый кортеж
print()







