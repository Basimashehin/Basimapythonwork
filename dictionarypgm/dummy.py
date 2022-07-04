dic={"k1":10,"k2":"hello","k3":True}


#print key value pair

for k,v in dic.items():
    print(k,v)

#print values from dic

for v in dic.values():
    print(v)


# k3 value
print(dic["k3"])
#this method generate error with invalid key so get method is better

print(dic.get("k2"))

dic.pop("k3")
print(dic)