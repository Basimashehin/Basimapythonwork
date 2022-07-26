import json
with open("countries.json",encoding="utf_8") as f:
    data=json.load(f)
    # print(data)




# # print total number of country details
print(len(data))
# # print languages of ukrane
d=[d["languages"] for d in data if d["name"]=="Ukraine" ]
d=d[0]
print(d[0]["name"])
#india detail
india=[d for d in data if d["name"]=="India"]
print(india)
lan=[d["languages"] for d in data if d["name"]=="India"]
lan=lan[0]
for l in lan:
    print(l["name"])
# # print currency of china
curr=[d["currencies"] for d in data if d["name"]=="China"]
curr=curr[0]
for c in curr:
    print(c["name"])

# # print population of india
pp=[d["population"] for d in data if d["name"]=="India"]
print(pp)
# # print nigehbouring/ countries of australia
#
aus =[d.get("borders") for d in data if d["name"]=="Australia"]
print(aus)

#find country with alpha3code
code="AFG"
cn=[d["name"] for d in data if d["alpha3Code"]==code]
print(cn)
#
# ppc=[d["population"] for d in data ]
# mx=max(ppc)
# print(mx)
# cn_mx_pp=[d["name"] for d in data if d["population"]==mx]
# print({cn_mx_pp[0]:mx})

pp=max(data,key=lambda d:d.get("population"))
print(pp.get("name"))

pm=min(data,key=lambda d:d.get("population"))
print(pm.get("name"))