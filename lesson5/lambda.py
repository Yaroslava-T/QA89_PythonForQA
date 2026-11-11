# lambda — это короткая анонимная функция. Здесь она полностью заменяет обычную функцию double().

print("************ example 5 (lambda function) ************")
def double(x):
    return x * 2                                   # обычная функция: умножает x на 2
double_lambda = lambda x: x * 2                   # lambda-функция делает то же самое в одну строку
print(double(5))                                  # 10
print(double_lambda(5))                           # 10
print()