add=lambda n1,n2:n1+n2

sub=lambda n1,n2:n1-n2

cube=lambda n:n**3

div=lambda n1,n2:n1/n2

mul=lambda n1,n2:n1*n2


print(add(2,3))
print(sub(7,2))
print(cube(3))


max_two=lambda n1,n2:n1 if(n1>n2) else n2

print(max_two(5,8))

smart_sub=lambda n1,n2:n1-n2 if(n1>n2) else n2-n1

print(smart_sub(4,9))