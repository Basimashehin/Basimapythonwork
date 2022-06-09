# 123
# 1**3+2**3+3**3

num=123
p=0
cube=0
sum=0
while(num!=0):
    p=num%10
    num=num//10
    cube=p**3
    sum+=cube

print (sum)