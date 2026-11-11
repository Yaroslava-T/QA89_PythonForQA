print("************ example 1 (function with parameter) ************")
def greet(name):
    return f"Hi, {name}!"                          # возвращает строку с приветствием

result = greet("Kristina")                         # вызывает функцию и сохраняет результат
print(result)                                      # выводит: Hi, Kristina!
print()

print("************ example 2 (default parameter) ************")
def create_user(name, role="user"):
    return {
        "name": name,
        "role": role
    }                                              # возвращает словарь с данными пользователя

print(create_user("Kristina"))                     # role не указан → используется "user"
print(create_user("Kristina", "admin"))            # role указан вручную → "admin"
print()

print("************ example 3 (default discount) ************")
def calculate_discount(price, discount=10):
    return price - (price * discount / 100)         # рассчитывает цену после скидки

print(calculate_discount(100))                      # скидка по умолчанию 10% → 90.0
print(calculate_discount(100, 20))                  # скидка 20% → 80.0
print(calculate_discount(1000, 25))                  # скидка 25% → 750.0
print()


print("************ example 4 (default parameter order) ************")
def foo(b, a=1):  #сначала идут обязательные параметры, потом параметры со значением по умолчанию.
    return a + b                                   # складывает a и b

print(foo(5))                                      # b = 5, a = 1 → 6
print()

print("************ example 5 (default None for list) ************")
def add_test_res(name, results=None):
    if results is None:
        results = []                                # создаёт новый пустой список при каждом вызове
    results.append(name)                            # добавляет название теста в список
    return results                                  # возвращает обновлённый список

print(add_test_res("test_login"))                   # ['test_login']
print(add_test_res("test_logout"))                  # ['test_logout']
print()

print("************ example 6 (mutable default argument) ************")
def add_test_res(name, results=[]):
    results.append(name)                            # добавляет новое значение в тот же список
    return results                                  # возвращает список со всеми добавленными значениями

print(add_test_res("test_login"))                   # ['test_login']
print(add_test_res("test_logout"))                  # ['test_login', 'test_logout']
print()


print("************ example 7 (positional and named arguments) ************")
def create_user1(username, email, role):
    return f"{username} {email} {role}"            # возвращает данные пользователя одной строкой

# позиционный вызов
print(create_user1("Kris", "kris@gm.com", "admin"))   # аргументы передаются по порядку

# именованный вызов
print(create_user1(role="admin", username="Kristina", email="kris@gm.com"))   # порядок не важен

# смешанный вызов: сначала позиционный, потом именованные
print(create_user1("Kristina", role="admin", email="kris@gm.com"))   # позиционный аргумент должен идти первым
print()