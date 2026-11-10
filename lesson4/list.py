print("************ example 1 (append) ************")
fruits = ['orange', 'strawberry', 'mango']
fruits.append('orange')        # добавляет элемент в конец списка
print(fruits)                  # выводит обновлённый список
print()

print("************ example 2 (insert) ************")
fruits.insert(1, 'banana')     # добавляет banana на позицию с индексом 1
print(fruits)                  # выводит список с добавленным banana
print()

print("************ example 3 (find index) ************")
first_banana_index = fruits.index('banana')   # находит индекс первого banana
print(f"The banana was added to position {first_banana_index}") # выводит индекс banana в списке
print()

print("************ example 4 (remove) ************")
fruits.remove('orange')   # удаляет первое найденное значение 'orange'
print(fruits)             # выводит список после удаления
print()

print("************ example 5 (pop) ************")
fruits.pop(2)             # удаляет элемент по индексу 2
print(fruits)             # выводит список после удаления
print()


print("************ example 6 (pop and save deleted item) ************")
numbers = [10, 20, 30]
deleted = numbers.pop(1)      # удаляет элемент по индексу 1 и сохраняет его в переменную
print(deleted)                # выводит удалённый элемент
print(numbers)                # выводит список после удаления
print()

print("************ example 7 (clear) ************")
numbers.clear()               # удаляет все элементы из списка
print(numbers)                # выводит пустой список []
print()






