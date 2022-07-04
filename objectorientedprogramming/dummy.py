class bottle:
    material:str
    capacity:str
    price:int
    colour:str

    # def set_bottle(self,**kwargs):
    def __init__(self,**kwargs):
        self.material=kwargs.get("material")
        self.colour=kwargs.get("colour")
        self.price=kwargs.get("price")
        self.capacity=kwargs.get("capacity")


    def open(self):
        print("open")

    def print_details(self):
        print(self.price,self.capacity,self.colour,self.material)



bt=bottle(material="plastic",capacity="800ml",price=150,colour="transparent")
# bt=bottle()
# bt.set_bottle(material="plastic",capacity="800ml",price=150,colour="transparent")
bt.open()
bt.print_details()