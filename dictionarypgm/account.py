accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]


# print details of 1002
# for data in accounts:
#     if data["acno"]==1002:
#         data.pop("transactions")
#         print(data)
#
# sv_acc=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
# print(sv_acc)
# sort account based on balance

# print(sorted(accounts,key=lambda i:i["balance"],reverse=True))

# print all phonepay transactions
all_trans=[ac["transactions"] for ac in accounts]
# print(all_trans)

 # for slist in all_trans:
 #    for trans in slist:
 #          if trans["method"] == "phone-pay":
#  #              print(trans)
# phone_pay=[trans for slist in all_trans for trans in slist if trans["method"]=="phone-pay"]
# #
# print(phone_pay)
#  # print all transactions where transaction amount > 500
#
# amt=[trans for slist in all_trans for trans in slist if trans["amount"]>500]
# print(amt)
#
# credit_trans=[trans for slist in all_trans for trans in slist if trans["to"]==1002]
# print(credit_trans)

# {"gpay":5476,"neft":758,"phonepay":6473}

out={}
for slist in all_trans:
    for trans in slist:
        # print(trans)
        m=trans["method"]
        amt=trans["amount"]
        if m in out:
          out[m]+=amt
        else:
          out[m]=amt

print(out)
print(max(out.items(),key=lambda i:i[1]))