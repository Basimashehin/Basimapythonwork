num=1234
res=""

# while (num != 0):
#      last_digit=num%10
#      print(last_digit,end="")
#      num=num//10

# while (num != 0):
#      last_digit=num%10
#      res=(res*10)+last_digit
#      num=num//10
#
# print(res)


while (num != 0):
     last_digit=num%10
     res=res+str(last_digit)
     num=num//10
print(res)
