# print()
# range()
# type()
# total=0
# total=sum(range(1,11))
# print(total)

def add_numbers(num1,num2):
    return num1+num2
print(add_numbers(2,3))

def sub_numbers(num1,num2):
    return num1-num2
print(sub_numbers(10,5))


def smart_sub(num1,num2):
    return num1-num2 if num1>num2 else num2-num1
print(smart_sub(5,10))

def num_chk(num):
    return "even" if num%2==0 else "odd"

print(num_chk(13))


def is_startswitha(name):
    return name.startswith("a")
def is_endswithlab(name):
    return name.endswith("lab")

print(is_startswitha("astric"))
print(is_endswithlab("technolab"))

def validate_gmail(email):
    return email.endswith("@gmail.com")


print("valid" if validate_gmail("basi@gmail.com")==1 else "notvalid")