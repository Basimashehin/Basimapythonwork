arr=[1,2,3,13,14,15,16,65,78,89]
element=14
# print(element in arr)
flag=0

for num in arr:
    if(num==element):
        flag=1
        break


print("true" if flag==1 else "false")




numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
neg_count_sum=0
po_count_sum=0
zero_count_sum=0

for num in numbers:
    if num>0:
        po_count_sum+=num
    elif num<0 :
        neg_count_sum+=num
    else:
        zero_count_sum+=num


print(f"positive number sum is {po_count_sum}")
print(f"negetive number sum is {neg_count_sum}")
print(f"zero number sum is {zero_count_sum}")

