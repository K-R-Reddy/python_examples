class A:
    def __init__(self):
        print("Object Created")
    def displayA(self):
        print("Class A")
    def __del__(self):
        print("Object Destroyed")
a=A()
a.displayA()
del a