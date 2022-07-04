class parent():
    def properties(self) ->str:
        self.prop={"mobile":"nokia","bike":"passionpro"}
        return self.prop

class child(parent) :
    def properties(self) ->str:
        prop=super().properties()
        prop["car"]="swift"
        return prop

ch=child()
print(ch.properties())

