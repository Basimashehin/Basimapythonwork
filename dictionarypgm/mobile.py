# mobile={
#     "mobile_name":"redminote12pro",
#     "display":"led",
#     "price":45000,
#     "ram":"6gb",
#     "memory":"64gb",
# }
#
#
# # print(mobile["mobile_name"])
# print(mobile.get("mobile_name"))
# print(mobile["ram"])
# print(mobile.get("memory"))
#
#
# # if "band" in mobile:
# #     mobile["band"]="5g"
# # else:
# #     mobile["band"]="4g"
# mobile["band"]="5g" if "band" in mobile else "4g"
# print(mobile)
#
# if mobile["price"]>40000:
#     mobile["price"]-=1000
# else:
#     mobile["price"]-=500
#
# print(mobile)



account={"accno":1000,
         "opening_date":"12-01-2019",
         "type":"savings",
         "pname":"ram"
         }
print(account["accno"])
print("balance" in account)
account["balance"]=5000
print(account)


account["balance"]+=1000
print(account)

