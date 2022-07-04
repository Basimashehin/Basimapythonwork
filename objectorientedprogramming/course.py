class course:
    c_id:str
    cname:str
    c_fee:int
    def __init__(self,**kwargs):
        print("hii")
        self.c_id=kwargs.get("c_id")
        self.cname=kwargs.get("cname")
        self.c_fee=kwargs.get("c_fee")

    def open(self):
        print("open")


    def print_course(self):
        print(self.cname,self.c_id,self.c_fee)

c1=course()
c=course(c_id="r345",cname="fullstack",c_fee=30000)
c.open()
c.print_course()