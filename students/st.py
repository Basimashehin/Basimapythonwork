class course:
     def post(self,**kwargs):
         self.course_name=kwargs.get("course_name")
         self.status=kwargs.get("status")

     def __str__(self):
         return self.course_name



class batch:
    def post(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code



class student:
    def post(self,**kwargs):
        self.st_name=kwargs.get("st_name")
        self.phone=kwargs.get("phone")
        self.gender=kwargs.get("gender")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.st_name

ms=course()
ms.post(course_name="MEARN",status=True)
dj=course()
dj.post(course_name="Django",status=True)
bj=course()
bj.post(course_name="Big data",status=True)
print(ms)
print(dj)
print(bj)

djb1=batch()
djb1.post(course=dj,batch_code="djangomay2k22",start_date="22-05-2022")
djb2=batch()
djb2.post(course=dj,batch_code="djangomay2_2k22",start_date="23-05-2022")
print(djb1)
print(djb2)
st1=student()
st1.post(st_name="rahul",phone="34697706",gender="male",batch=djb1)
print(st1)
print(st1.batch)