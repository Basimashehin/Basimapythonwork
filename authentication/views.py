# for functionality

from authentication.models import users

def authenticate(**kwargs):
    uname=kwargs.get("username")
    pwd=kwargs.get("password")
    user=[user for user in users if user["username"]==uname and user["password"]==pwd]
    print(user)


authenticate(username="python",password="python@123")

    
