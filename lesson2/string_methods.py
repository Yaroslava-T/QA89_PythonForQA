name = 'Alice'
age = 30

formatted_string = f" Hello my name is {name} and I am {age} years old"
print(formatted_string)

print("************** find **************")
#find() ищет Частичное совпадение
s = 'AbrakadabraAbrakadabra'
str = 'bra'
print(s.find(str)) #первое совпадение, выводит индекс первой буквы искомого запроса
print(s.rfind(str)) #последнее совпадение, выводит индекс
print(s.find('add')) #выводит индекс -1, если значение не найдено

print("************* count *************")
#count(sub[str,start,end])
print(s.count(str))
print(s.count(str,4))
print(s.count(str,4,16))

print("********** letter case (регистр) **********")
#str.upper()
#str.lower()
s = 'AbrakaDaBraAbrakaBabra'
print(s.lower())
print(s.upper())
print(s)

print("********** split (разделение) **********")
#split()
#Contact was added: egdfukw3574632483pjfskjdfj;sldlfg'd
s = 'Cat, Dog,Monster Rabbit, Pig'
print(s.split())
print(s.split(','))
print(s.split(',',2))

print("********** rjust() & ljust() (выравнивание строки до заданной длины, заполняя пустое место указанным символом) **********")
#rjust() & ljust()
s = 'Hi!'
print(s.rjust(10,'*'))
print(s.ljust(10,'#'))

test = ["Login","Cart","API"]
for t in test:
    print(t.ljust(10),"OK")

order = "125"
print(order.rjust(8,"0"))

print("********** isalpha/isdigit (проверка вида запроса -только из букв/цифр-) **************")
s = 'AbrakaDaAbrakaDabra'
u = '076921123943251'
print(s.isalpha()) #метод для определения, состоит ли запрос только из букв
print(u.isdigit()) #метод для определения, состоит ли запрос только из цифр
print(u.isnumeric()) #метод для определения, состоит ли запрос только из чисел

print("************ index ************")
#index()
text = "QA automation with Python"
pos  = text.index("automation")
print(pos)
# pos  = text.index("automation",10)

print("************ replace ************")
#replace()
text1 = "I like Python"
print(text1.replace("Python","Python and Coffee"))
print("************ пример 2 ************")
text  = "2026-07-03"
new_text = text.replace("-","/")
print(new_text)

print("************  ************")






