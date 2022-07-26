# try
# except
# raise
# finally
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# try:
#     num=num1/num2
#     print(f"result is num {num}")
# except Exception as f:
#     print(f)
# print("file opening")
# print("file operation")
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# try:
#     num=num1/num2
#     print(f"result is num {num}")
# except:
#     print("division by zero error")
# print("file opening")
# print("file operation")

# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# try:
#     num=num1/num2
#     print(f"result is num {num}")
# except Exception as f:
#     num2=int(input("enter num2"))
#     num=num1/num2
#     print(f"result is num {num}")
#
#
# finally:
#     print("file opening")
#     print("file operation")
#
#
# age=int(input("enter age"))
# if(age<18):
#     raise Exception("not eligible for taking booster dose")
# else:
#     print("eligible for booster dose")
#
phone_number=input("enter phone number")
if len(phone_number)!=10 :
    raise Exception ("not a valid phone number")
else:
    print("valid")
