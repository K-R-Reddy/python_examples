class ParentA:
    def showA(self):
        print("ParentA Class")
class ChildA(ParentA):
    def showAA(self):
        print("Child Class of ParentA")
class ChildAA(ChildA):
    def showAAA(self):
        print("Child Class of ChildA")
ml=ChildAA()
ml.showA()
ml.showAA()
ml.showAAA()