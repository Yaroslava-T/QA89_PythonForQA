print("************ exercise 1 (reverse list) ************")
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")                        # выводит ошибку, если передан не список или пустой список
        return
    reversed_lst = lst[::-1]                       # создаёт список в обратном порядке
    print(reversed_lst)                            # выводит перевёрнутый список

print_list_reverse([1, 2, 3, 4, 5])                # [5, 4, 3, 2, 1]
print_list_reverse([])
print()


print("************ exercise 2 (validate point) ************")
def is_valid_point(point):
    if point is None:
        return None                                 # если значение None
    if isinstance(point, tuple) and len(point) == 0:
        return None                                 # если передан пустой кортеж
    if not isinstance(point, tuple) or len(point) != 2:
        return False                                # должен быть кортеж ровно из двух элементов
    x, y = point
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return False                                # x и y должны быть числами
    return True                                     # точка корректная
print(is_valid_point((3, 5)))                       # True
print(is_valid_point((3, "5")))                     # False
print(is_valid_point([3, 5]))                       # False
print(is_valid_point((1, 2, 3)))                    # False
print(is_valid_point(()))                           # None
print(is_valid_point(None))                         # None
print()


print("************ exercise 3 (reverse part of list) ************")
def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong args")                         # проверяет, что lst — непустой список
        return

    if (
        not isinstance(start, int)
        or not isinstance(finish, int)
    ):
        print("Wrong args")                         # проверяет, что start и finish — целые числа
        return

    if (
        start < 0
        or finish < 0
        or start >= len(lst)
        or finish >= len(lst)
        or start > finish
    ):
        print("Wrong args")                         # проверяет корректность индексов
        return

    beginning = lst[:start]                         # часть списка до start
    middle = lst[start:finish + 1]                  # часть списка от start до finish включительно
    end = lst[finish + 1:]                          # часть списка после finish

    middle.reverse()                                # переворачивает выбранную часть списка

    result = beginning + middle + end               # соединяет все части обратно
    print(result)                                   # выводит итоговый список

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)   # [10, 40, 30, 20, 50, 60]
print_sublist_reverse([1, 2, 3], "0", 2)                 # Wrong args
print()




















