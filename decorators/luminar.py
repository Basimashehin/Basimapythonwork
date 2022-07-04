class staff(object):
    id:int
    name:str
    role:str


    def __init__(self,*args,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")


    def __str__(self):
        return self.name
    

class addcourse(object):
    def set_course(self,course_name,user):
        self.course_name=course_name
        self.user=user
        
    def __str__(self):
        return self.course_name


user=staff(id=100,name="rahul",role="admin")
print(user)
course=addcourse()
course.set_course(course_name="django",user=user)
print(course)