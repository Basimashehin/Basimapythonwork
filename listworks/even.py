numbers=[12,13,14,15,16,17,18]


# for num in numbers:
#     if num%2==0:
#         print(num)


# printnum+1 ifnum>15  else print num-1 num=15 if num=15

#
# for num in numbers:
#     if num>15 :
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     else:
#         print(num)


# prinnt count of numbers in range 14-18


# for num in numbers:
#     if num>=14 and num<=18:
#         count+=1
#         print(num)

# print(count)
# count=0
# for num in numbers:
#     if num in range(14,19) :
#         count+=1
#
#
# print(count)


numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
neg_count=0
po_count=0
zero_count=0

for num in numbers:
    if num>0:
        po_count+=1
    elif num<0 :
        neg_count+=1
    else:
        zero_count+=1


print(f"positive number count is {po_count}")
print(f"negetive number count is {neg_count}")
print(f"zero number count is {zero_count}")


company="luminar"
location="kakkanad"
status="open"
closes="9"

print(company+" located at "+location+" is "+status+" closes at "+closes)

