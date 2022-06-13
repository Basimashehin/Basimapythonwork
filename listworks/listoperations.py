lst=[10,11,12,13,14,15,16,17,12,12,12,12,100]


# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# lst.append(10)
# print(lst)
#
# lst.pop()
# print(lst)
#
# lst.reverse()
# # print(lst)
# oddlist=[]
# evenlist=[]
# for num in lst:
#     if num%2!=0:
#         oddlist.append(num)
#     else:
#         evenlist.append(num)
# print(oddlist)
# print(evenlist)
# oddlist.sort(reverse=True)
# evenlist.sort(reverse=True)
# print(oddlist)
# print(evenlist)
#
#
# print(lst.count(12))



lst1=[10,11,11,12,13,14]
lst2=[11,14,15,16,17]

print(dir(list))
# for num in lst1:
#     for n in lst2:
#         if(n==num):
#             print(num)

duplist=list()
for num in lst1:
     if num in lst2:
         duplist.append(num)

print(set(duplist))


