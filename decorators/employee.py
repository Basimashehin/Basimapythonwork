def admin_only(fn):
     def wrapper(*args,**kwargs):
         user=kwargs.get("empy")
         if user.erole!="admin":
             print("admin permission required")
         else:
             return fn(*args,**kwargs)
     return wrapper


class employee():
    eid:int
    ename:str
    erole:str
    def __init__(self,*args,**kwargs):
        self.eid=kwargs.get("id")
        self.ename=kwargs.get("ename")
        self.erole=kwargs.get("erole")

    def __str__(self):
        return self.ename

class adddepartment():
    @admin_only
    def __init__(self,*args,**kwargs):
        self.dep_name=kwargs.get("dep_name")
        self.empy=kwargs.get("empy")

    def __str__(self)->str:
        return self.dep_name




emp=employee(id=100,ename="rahul",erole="hr")
print(emp)
dpt=adddepartment(dep_name="django",empy=emp)
print(dpt)
