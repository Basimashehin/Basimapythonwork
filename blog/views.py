from blog.models import users,posts

session={}

def signinrequired(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("sign in required")
    return wrapper

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user

# print(authenticate(username="akhil",password="Password@123"))

class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print(session)


class PostListView:
    @signinrequired
    def get(self,*args,**kwargs):
        return posts
    @signinrequired
    def post(self,*args,**kwargs):
        data=kwargs.get("data")
        data["userId"]=session["user"]["id"]
        data["postId"]=posts[-1]["postId"]+1
        posts.append(data)
        print(posts[-1])
        print("posed succesfully")


class MyPostListView:
    @signinrequired
    def get(self,*args,**kwargs):
        u_id=session["user"]["id"]
        post=[post for post in posts if post["userId"]==u_id]
        return post

class Addlike:
    @signinrequired
    def post(self,*args,**kwargs):
        p_id=kwargs.get("post_id")
        u_id=session["user"]["id"]
        post=[post for post in posts if post["postId"]==p_id]
        if post:
           post=post[0]
        lst=post.get("liked_by")
        print(lst)
        lst.append(u_id)
        print(post)
log_in=LoginView()
log_in.post(username="richard",password="Password@123")
all_post=PostListView()
print(all_post.get())
pst={"title":"hello good morning","content":"my content","liked by":[]}
all_post.post(data=pst)
mypost=MyPostListView()
print(mypost.get())
ad=Addlike()
ad.post(post_id=1)