#file = open(.........)
#file.close()

# 'r'-> read
# 'w' -> write
# 'a' -> append
# 'r +' read and write
# 'rb','wb'->pdf, screenshots

print("************ example 1 (open and close file) ************")
file = open("test.txt", "r")                      # открывает файл для чтения
file.close()                                      # закрывает файл
print()

print("************ example 2 (read mode - r) ************")
file = open("test.txt", "r")                      # открывает существующий файл для чтения
content = file.read()                             # читает всё содержимое файла
print(content)                                    # выводит текст из файла
file.close()                                      # закрывает файл
print()

print("************ example 3 (write mode - w) ************")
file = open("test.txt", "w")                      # открывает файл для записи
file.write("Hello Python")                        # записывает текст в файл
file.close()                                      # закрывает файл
# если файл уже существовал, старое содержимое будет удалено
print()

print("************ example 4 (append mode - a) ************")
file = open("test.txt", "a")                      # открывает файл для добавления текста
file.write("\nNew line")                          # добавляет текст в конец файла
file.close()                                      # закрывает файл
# старое содержимое файла сохраняется
print()

print("************ example 5 (read and write mode - r+) ************")
file = open("test.txt", "r+")                     # открывает файл для чтения и записи
content = file.read()                             # читает содержимое файла
print(content)                                    # выводит содержимое
file.write("\nAdded text")                        # добавляет новый текст
file.close()                                      # закрывает файл
print()

print("************ example 6 (binary read mode - rb) ************")
file = open("document.pdf", "rb")                 # открывает бинарный файл для чтения
data = file.read()                                # читает файл как набор байтов
file.close()                                      # закрывает файл
# используется для PDF, изображений и других бинарных файлов
print()

print("************ example 7 (binary write mode - wb) ************")
file = open("copy.pdf", "wb")                     # открывает бинарный файл для записи
file.write(data)                                  # записывает байты в новый файл
file.close()                                      # закрывает файл
# используется для PDF, изображений, скриншотов и других бинарных файлов
print()