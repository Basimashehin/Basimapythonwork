from functools import reduce

num=[2,39,9,78]

str_lst=[str(n) for n in num]
str_lst=sorted(str_lst,reverse=True)
mx_num=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_lst)
print(mx_num)
