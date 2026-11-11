print("************ example 1 (unpacking list with *) ************")
def login(username, password):
    print(username, password)                      # выводит username и password

data = ['admin', '123456']                        # список с данными для входа
login(data[0], data[1])                           # передаёт элементы списка по индексам
login(*data)                                      # распаковывает список и передаёт элементы как отдельные аргументы
print()

print("************ example 2 (unpacking dictionary with **) ************")
user = {
    "username": "admin",
    "password": "A12345"
}                                                   # словарь с данными пользователя

login(**user)                                      # распаковывает словарь и передаёт значения по именам параметров
# **user == login(username="admin", password="A12345")
# print()

print("************ example 3 (extra key error) ************")
user = {
    "username": "admin",
    "password": "B12345",
    "remember_me": True
}
login(**user)   # ошибка: лишний аргумент remember_me
print()