print("************ example 1 ************")
empty_list = []
mixed_list = [2,'orange',4.22,True]

fruits = ['orange', 'strawberry', 'mango']
print(fruits)
print(fruits[0])

print("************ example 2 (change list item) ************")
fruits[1] = 'lemon'
print(fruits)
print(fruits[1])

print("************ example 3 (combine two lists) ************")
list1 = ['orange','lemon']
list2 = ['shampoo','soap']
combo_list = list1 + list2
print(combo_list)

print("************ example 4 (unpacking list) ************")
fruits = ['orange', 'strawberry', 'mango', 'apple']
first, second, third, *rest = fruits
print(first)
print(second)
print(third)
print(rest)

print("************ example 5 (loop through list) ************")
fruits = ['orange', 'strawberry', 'mango']
for item in fruits:
    print(f"item in fruits: {item}")
    # Result:
    # item in fruits: orange
    # item in fruits: strawberry
    # item in fruits: mango

print("************ example 6 (normalize and compare lists) ************")
correct_answers = ['orange', 'strawberry', 'mango']
user_answers = ['orange', 'strawberry', 'apple']

if correct_answers == user_answers:
    print("Correct answers")
else:
    print("Incorrect answers")

print(len(fruits)) #list length
max(fruits)
print(max(fruits)) #maximum value
print()

print("************ example 7 (max and min) ************")
numbers = [12,56,94,6]
print(max(numbers))
print(min(numbers))

print("************ example 8 (sorted) ************")
res = sorted(numbers)
print(res)  # отсортированный список по возрастанию
print(numbers)  # исходный список без изменений

print(sorted(numbers, reverse=True)) # список в обратном порядке
print(sorted(fruits))  # список слов в алфавитном порядке
print(sorted(fruits, reverse=True))  # список слов в обратном алфавитном порядке

print("************ example 9 (sorted string) ************")
word = 'python'
print(sorted(word))  # список букв в алфавитном порядке
result= ''.join(sorted(word))
print(result)  # строка из отсортированных букв

print("************ example 10 (sort and sorted names) ************")
names = ['Alex', 'Kristina','Bob', 'Tim']
print(names, 'исходный список') #исходный список
print(sorted(names)) # новый список в алфавитном порядке
print(sorted(names,key=len)) # новый список по длине слов

names.sort()
print(names)  # исходный список отсортирован по алфавиту

names.sort(key=len)
print(names)  # исходный список отсортирован по длине слов









