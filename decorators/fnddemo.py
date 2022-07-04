# def sub(n1,n2):
#     if(n2>n1):
#         return n2-n1
#     else:
#         return n1-n2
#
#
# def div(n1,n2):
#     if n2>n1:
#         return n2/n1
#     else:
#         return n1/n2
#
# print(sub(10,20))
# print(div(10,20))
def smart_operation(fn):
    def inner_fun(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fun

@smart_operation
def sub(n1,n2):
        return n1-n2

@smart_operation
def div(n1,n2):
        return n1/n2

print(sub(20,10))
print(div(20,10))