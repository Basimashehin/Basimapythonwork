class Editor:

    def functionalities(self) ->str:
        self.funs=["create new file","execute","save"]
        return self.funs


class pycharm(Editor):

     def functionalities(self) ->str:
         funs=super().functionalities()
         funs.append(["debug","versioncontrolling"])

         return funs


class vscode(Editor):

    def functionalities(self) ->str:
        funs=super().functionalities()
        funs.append(["more extension support"])
        return funs



pyc=pycharm()
print(pyc.functionalities())
vc=vscode()
print(vc.functionalities())