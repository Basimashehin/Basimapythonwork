import json
import random
try:
   with open("../blog/users.json")as f:
       data=json.load(f)
       print(data)
       all_user=list(map(lambda d:d["id"],data))
       print(all_user)
       my_followings=[d["followers"] for d in data if d["username"]=="akhil"]
       my_followings=my_followings[0]
       print(my_followings)
       sugg=set(all_user)-set(my_followings)
       sugg.remove(1)
       print(sugg)
       out=random.sample(sugg,2)
       print(out)

except Exception as e:
    print(e)

