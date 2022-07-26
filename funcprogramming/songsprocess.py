import json
import random
from functools import reduce
with open("songs.json") as f:
    data=json.load(f)
    print(data)
    # song which have max rating
    rat=list(map(lambda d:d["rating"],data))
    mx=max(rat)
    # mx_rat=[d["name"] for d in data if d["rating"]==mx]
    mx_rat=reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"]else s2,data)
    print("maximum rating is")
    print(mx_rat)
    # two random sad song
    sd=[d["name"] for d in data if d["mode"]=="sad"]
    sd_rand=random.sample(sd,2)
    print(sd_rand)
    # total album
    totalb=[d["album"] for d in data]
    print(len(set(totalb)))
    # no:of songs in album 1
    l=[d["name"] for d in data if d["album"]=="album1"]
    print(len(l))
    # album with max songs
    out={}
    for a in totalb:
        if a in out:
            out[a]+=1
        else:
            out[a]=1
    print(out)
    print(max(out.items(),key=lambda s:s[1]))
