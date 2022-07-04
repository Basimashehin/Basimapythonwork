f=open("movies.txt")
mov=[mov.rstrip("\n").split(",") for mov in f]

# number of moviews released in 2022
rel=[r for r in mov if r[1]==2022]
print(rel)
# number malayalam movies
m=[m for m in mov if m[3]=="malayalam"]
print(m)
print(len(m))

# theater released movies
t=[t for t in mov if t[-1]=="theater"]
print(t)

# list of movies whose rating > 5
r=[r for r in mov if int(r[2]) > 5]
print(r)

# {2022:,4,2021:6,2020:2}
out={}
for m in mov:
    year=m[1]
    l=[l for l in mov if int(l[1])==int(m[1])]
    movrel=len(l)
    if m[1] in out:
        pass
    else:
        out[m[1]]=movrel

print(out)
# 2021

mx=(max(out.items(),key=lambda i:i[1]))
print(mx)