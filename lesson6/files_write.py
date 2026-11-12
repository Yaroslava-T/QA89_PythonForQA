print("************ example 1 (with open) ************")
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello auto tests!\n")              # записывает первую строку в файл
    file.write("Second Line!")                     # записывает вторую строку

# with автоматически закрывает файл после завершения блока
# "w" — режим записи, старое содержимое файла удаляется
# encoding="utf-8" — кодировка для корректной работы с текстом
print()


print("************ example 2 (append test results to log file) ************")
def log_test_res(test_name, status):
    with open("test_run.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")   # добавляет результат теста в конец файла

log_test_res("test_login", "Passed")                # записывает test_login:Passed
log_test_res("test_registration", "Failed")         # записывает test_registration:Failed
log_test_res("test_logout", "Failed")               # записывает test_logout:Failed
print()










