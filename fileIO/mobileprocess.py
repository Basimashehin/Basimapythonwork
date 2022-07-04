f=open("mobile.txt")
# lst=[lst.rstrip("\n") for lst in f]
# l=[l.split(",") for l in lst]
l=[l.rstrip("\n").split(",") for l in f]
# l.sort(key=lambda i:i[2],reverse=True)
# res=l[0]
res=max(l,key=lambda i:int(i[2]))
print(res)

fiveg=[fg for fg in l if fg[3]=="5g"]
print(fiveg)