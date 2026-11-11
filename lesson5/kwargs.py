#keywords argument — это именованный аргумент: при вызове функции ты явно пишешь имя параметра и его значение.

print("************ example 1 (**kwargs) ************")
def print_config(**kwargs):
    print(type(kwargs), kwargs)                    # собирает все именованные аргументы в словарь

print_config(browser="chrome", headless=True, timeout=30)   # kwargs = {'browser': 'chrome', 'headless': True, 'timeout': 30}
print_config()                                     # kwargs = {}
print()


print("************ example 2 (**kwargs return dictionary) ************")
def create_user(**data):
    return data                                    # возвращает словарь со всеми переданными именованными аргументами

user = create_user(name="Anna", role="user")       # data = {'name': 'Anna', 'role': 'user'}
print(user)                                        # выводит словарь пользователя
print()


print("************ example 3 (regular args, *args and **kwargs) ************")
def example(a, b=10, *args, **kwargs):
    print(a)                                       # обычный обязательный параметр
    print(b)                                       # параметр со значением по умолчанию
    print(args)                                    # собирает дополнительные позиционные аргументы в кортеж
    print(kwargs)                                  # собирает именованные аргументы в словарь

example(1, 2, 3, 6, name="Kristina")
# a = 1
# b = 2
# args = (3, 6)
# kwargs = {'name': 'Kristina'}
print()