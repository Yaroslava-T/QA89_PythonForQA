#args (arguments) позволяет передать в функцию любое количество позиционных аргументов.
# То есть args внутри функции — это кортеж со всеми переданными позиционными значениями.

print("************ example 1 (*args) ************")
def total(*args):
    print(type(args), args)                        # собирает все переданные аргументы в кортеж
    return sum(args)                               # считает сумму всех элементов кортежа

print(total(1, 2, 3))                              # args = (1, 2, 3), результат 6
print(total(10, 20))                               # args = (10, 20), результат 30
print(total(10, 20, 40, 80, 90))                  # args = (10, 20, 40, 80, 90), результат 240
print(total())                                     # args = (), сумма пустого кортежа = 0
print()

print("************ example 2 (*args with regular parameter) ************")
def print_scores(students, *scores):
    print(f"Student: {students}")                  # обычный параметр: имя студента
    print("Scores: ", scores)                      # *scores собирает все оценки в кортеж

print_scores("Anna", 90, 87, 100)                  # students = "Anna", scores = (90, 87, 100)
print_scores("Bob", 70)                            # students = "Bob", scores = (70,)
print()

print("************ example 3 (*args with assert) ************")
def check_status_codes(*codes):
    for code in codes:
        assert code == 200                         # проверяет, что каждый код равен 200

print(check_status_codes(200, 200, 200))            # все коды 200 → функция завершится без ошибки и вернёт None
print(check_status_codes(200, 404, 201))            # на 404 возникнет AssertionError
print()
#Важно: функция ничего не return, поэтому первый print(...) выведет: None
# А второй вызов остановится на 404, потому что условие: assert code == 200 будет False.