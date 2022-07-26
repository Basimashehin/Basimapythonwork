import json
with open("blog.json")as f:
    data=json.load(f)
    print(data)


#no:of post
print(len(data))

#no:of post by userid=1
pst=[pst for pst in data if int(pst["userId"])==1]
print(len(pst))
#no:of likes for post 6
pd=[len(pd["liked_by"]) for pd in data if int(pd["postId"])==6]
print(pd)

# no:of posts liked by user 2
# count=0
# for post in data:
#     lk=[post["liked_by"]
#     if 2 in lk:
#         count=count+1
#     else:
#         pass
# print(count)
lk=[post for post in data if 2 in post["liked_by"]]
print(len(lk))