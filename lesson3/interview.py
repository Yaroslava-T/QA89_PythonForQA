print("************ example 1 ************")
def print_string_reverse(s):
    if s is None or s.strip() == "":
        print("Wrong String")
        return
    #else:
       #print (s[::-1]) #как вариант
    reversed_s = s[::-1]
    print(reversed_s)

print_string_reverse("Hello")
print_string_reverse(None)
print_string_reverse("")
print_string_reverse(" ")

print("************ example 2 ************")
def is_isr_phone_number(phone):
    if phone is None or phone == "":
        return None
    if len(phone) != 10:
        return False
    if phone[0] != "0":
        return False
    if not phone.isdigit():
        return False
    return True

# test_input = input("Enter a phone number: ")
# print(is_isr_phone_number(test_input))

print(is_isr_phone_number("0521234567"))
print(is_isr_phone_number("521234567"))
print(is_isr_phone_number("05212345a7"))
print(is_isr_phone_number(""))

print("************ example 3 ************")
def print_substring_reverse(s, start, finish):
    if s is None or s.strip() == "":
        print("Wrong args")
        return
    if start<0 or finish>=len(s) or start>finish:
        print("Wrong args")
        return
    beginning = s[:start]
    middle_reverse = s[start:finish+1][::-1]
    end_reverse = s[finish+1:]
    print(beginning+middle_reverse+end_reverse)

print_substring_reverse("Morning",1,3)
print_substring_reverse(None,1,3)
print_substring_reverse("Hi",1,5)
print_substring_reverse("Hi",3,1)
print()

print("************ example 4 ************")
def get_words_reverse(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(get_words_reverse("Hello my nice world"))

print("************ example 4 (Advanced) ************")
def print_words_reverse_in_column(s):
    words = s.split()
    for word in words:
        print(word[::-1])
print_words_reverse_in_column("Hello my nice world")








