lst=[2,3,4,6]
element=7
lst.sort()
low=0
upp=len(lst)-1
count=1

# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if(lst[i]+lst[j]==sum):
#             print(f"pairs {lst[i]},{lst[j]}")

while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==element:
        print(f"pairs {lst[low]},{lst[upp]}")
        break
    elif cur_sum>element:
        upp-=1
    elif cur_sum<element:
        low+=1
