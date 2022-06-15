arr1=[10,11,12,13,14]

arr2=[9,10,12,14,20]

#
# for num1 in arr1:
#     for num2 in arr2:
#         if num1==num2:
#             print(f"common {num1}")

p1=0
p2=0
arr1.sort()
arr2.sort()
while(p1<len(arr1)and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"common element {arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
