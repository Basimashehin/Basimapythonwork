# lst=[10,11,11,12,13,14,14,14]
# duplst=[]
# for i in range(0,len(lst)):
#  for j in range(i+1,len(lst)):
#     if(lst[i]==lst[j]):
#      duplst.append(lst[i])
#
# print(duplist)
#

arr=[13,12,14,16,11,10,15]
flag=0
element=15
arr.sort()
low=0
upp=len(arr)-1
while(low<=upp):
  mid=(low+upp)//2
  if element==arr[mid]:
        flag=1
        break
  elif element>arr[mid]:
       low=mid+1
  elif element<arr[mid]:
       upp=mid-1
print("found" if flag>0 else "notfound")