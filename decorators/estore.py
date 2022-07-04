def admin_only(fn):
    def wrapper(*args,**kwargs):
        u_ser=kwargs.get("userr")
        if u_ser.role =="admin":
            return fn(*args,**kwargs)
        else:
            print("not accessable")
    return wrapper


class user:
    def __init__(self,*args,**kwargs):
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")
    def __str__(self):
        return self.name
class addproduct:
    @admin_only
    def post(self,*args,**kwargs):
        self.product_name=kwargs.get("p_name")
        self.user=kwargs.get("userr")

    def __str__(self):
        return self.product_name


user=user(name="john",role="admin")
print(user)
print(user.role)
pro1=addproduct()
pro1.post(p_name="laptop",userr=user)
print(pro1)