# def add(*args):
#     return sum(args)
#
# def max_fun(*args):
#     return max(args)
#
# def min_fun(*args):
#     return  min(args)
#
# print(add(10,20))
# print(add(10,20,30,40))
#
# print(max(20,70,30,24,50))
# print(max(30,20))
#
# print(min(20,60,40))
# print(min(50,20,12,45,57,60))
#
def prnt_nums(**kwargs):
    print(kwargs)

prnt_nums(n1=20,n2=50,n3=60)
prnt_nums(name="luminar",place="kochi",amt=30000,course="py")

def add_nums(**kwargs):
    print(sum(v for k,v in kwargs.items()))

add_nums(n1=20,n2=10,n3=40)
