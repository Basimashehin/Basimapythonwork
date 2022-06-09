# 1234
# 1234
# 1234

#
# num=4
# pattern=""
# for row in range(1,num):
#     for col in range(1,num+1):
#         print(col,end="")
#     print()


# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
#
# num=4
# for row in range(1,num+1):
#     for col in range(1,num):
#         print(row,end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
num=4

# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()

#
# 1
# 2 2
# 3 3 3
# 4 4 4 4

# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

# numbers= range(5,0,-1)
# for i in numbers:
#     print(i)

# # # # #
# # # #
# # #
# #
#
# num=5
# for row in range(1,num):
#     for col in range(num,row,-1):
#         print("#",end=" ")
#     print()


for row in range(1,5):
    for space in range(1,5-row):
        print(" ",end=" ")
    for col in range(1,row+1):
        print("*",end="    ")
    print()


#
# for row in range(1,5):
#     for col in range(1,8):
#         if(row==4 or row+col==5 or col-row==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()