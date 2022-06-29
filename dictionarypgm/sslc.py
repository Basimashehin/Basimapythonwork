result=[
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90, "A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win": 95, "A+": 50000},
    {"district":"mpm","win": 90, "A+": 4500}

]
# sort result based on win in desc order
print(sorted(result,key= lambda res:res["win"],reverse=True))

# print dist with min win
print(min(result,key=lambda res:res["win"]))

# print result based on A+
print(sorted(result,key= lambda res:res["A+"]))

# print dist with min A+

print(min(result,key=lambda res:res["A+"]))

# find total no:of students got full A+

aplus=  [res["A+"] for res in result]
print(sum(aplus))