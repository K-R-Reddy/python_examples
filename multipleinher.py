class ParentA:
    def displayA(self):
        print("This is a ParentA class")
class ParentB:
    def displayB(self):
        print("This is a ParentB class")
class ChildAB(ParentA,ParentB):
    def displayAB(self):
        print("This is a ChildAB class")
m=ChildAB()
m.displayA()
m.displayB()
m.displayAB()