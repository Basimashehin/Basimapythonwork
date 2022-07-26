# map
# filter
# reduce

from functools import reduce
lst=[10,2,30,4]
#
# sq=[num**2 for num in lst]

sq=list(map(lambda n:n**2,lst))
print(sq)
cubes=list(map(lambda n:n**3,lst))
print(cubes)

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)


gt_two=list(filter(lambda n:n>2,lst))
print(gt_two)

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

pro=reduce(lambda n1,n2:n1*n2,lst)
print(pro)

max=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max)

min=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min)