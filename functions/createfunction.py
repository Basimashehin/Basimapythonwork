def fact(num):
    f=1
    i=1
    while(i<=num):
        f*=i
        i+=1
    return f
print(fact(3))


def is_prime(num):
    flag=1
    for i in range(2,num):
        if(num%i==0):
            flag=0
            break
    return flag
print(is_prime(8))



def prime_range(low,upp):
    for i in range(low,upp+1):
        if is_prime(i)==1 :
            print(i)

prime_range(10,50)