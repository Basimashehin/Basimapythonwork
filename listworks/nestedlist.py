lst=[
    [10,15],
    [13,45],
    [50,15],
    [60,16]
]

# print all numbers>16
flt_lst=[num for slst in lst for num in slst]
print(flt_lst)
num_gt_sixt=[num for num in flt_lst if num>16]
print(num_gt_sixt)


odd_number=[num for num in flt_lst if num%2!=0]
print(odd_number)

even=[num for num in flt_lst if num%2==0]
print(even)
print(sum(even))

# num>25 num+1 else num-1

mp=[num+1 if num>25 else num-1 for num in flt_lst]

print(mp)
















# for sub_lst in lst:
#     for num in sub_lst:
#         if num > 16:
#             print(num)
#
#
# print(lst)
# flattenlst=[]
#
# for sub_lst in lst:
#     for num in sub_lst:
#           flattenlst.append(num)
#
# print(max(flattenlst))
# print(min(flattenlst))

