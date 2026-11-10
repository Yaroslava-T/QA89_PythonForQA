print("************ example 1 (dictionary) ************")
books = {
    'Harry Potter and .....': 'J.K.Rowling',
    'To kill a mockingbird': 'Harper Lee'
}                                                   # словарь: ключ = название книги, значение = автор
print(books)                                        # выводит весь словарь
print()

print("************ example 2 (set) ************")
books1 = {
    'Harry Potter and .....',
    'To kill a mockingbird'
}                                                   # множество: хранит только уникальные значения без ключей
print(books1)                                       # выводит элементы множества
print()

print("************ example 3 (nested dictionary) ************")
response = {
    'statusCode': 'success',
    'user': {
        'id': 1,
        'name': 'Kris'
    }
}                                                   # словарь содержит вложенный словарь user
print(response['user']['name'])                     # выводит значение name из вложенного словаря
print()




#API

print("************ additional example (check required fields) ************")
contact = {
    "id": 12,
    "name": "Anna",
    "email": "anna@gm.com"
}                                                   # словарь с данными контакта

req_field = {
    "id",
    "name",
    "email"
}                                                   # множество обязательных полей

for field in req_field:
    assert field in contact, f"В ответе отсутствует поле {field}"
                                                    # проверяет наличие каждого обязательного поля в словаре
print()





