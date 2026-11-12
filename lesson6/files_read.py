print("************ example 1 (write and read whole file) ************")
with open("users.txt", "w", encoding="utf-8") as file:
    file.write("Lora\n")                           # записывает первую строку
    file.write("Ivan\n")                           # записывает вторую строку
    file.write("Kris\n")                           # записывает третью строку

# read() -> читает весь файл одной строкой
with open("users.txt", "r", encoding="utf-8") as file:
    content = file.read()                          # считывает всё содержимое файла

print(content)                                     # выводит весь текст из файла
print(len(content))                                # выводит количество символов в тексте
print()

print("************ example 2 (readlines - список строк) ************")
with open("users.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()                       # читает все строки и возвращает список
    # lines2 = [line.strip() for line in file.readlines()]  # читает все строки и возвращает список без пробелов
    # и \n в начале и конце строк
    lines3 = [line.strip() for line in lines]

print(lines)                                       # ['Lora\n', 'Ivan\n', 'Kris\n']
# print(lines2)                                       # ['Lora', 'Ivan', 'Kris']
print(lines3)                                       # ['Lora', 'Ivan', 'Kris']
#read() возвращает весь файл как одну строку, а readlines() — список строк.
print(lines[0])  # Lora
print()

print("************ example 3 ************")
for line in lines:                 # по очереди перебирает каждую строку из списка lines
    print(line.strip())            # убирает пробелы и \n по краям строки и выводит её
print()

print("************ example 4 (for, read file with for loop) ************")
with open("users.txt", "r", encoding="utf-8") as file:   # открывает файл для чтения
    for line in file:                                    # по очереди читает каждую строку файла
        print(line.strip())                              # убирает пробелы и \n по краям и выводит каждую строку
print()

#for line in lines → перебирает уже готовый список
# for line in file → читает файл построчно напрямую


