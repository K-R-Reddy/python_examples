class a:
    b="CSE"
    __b="ECE"
    def dis(self):
        print(a.b)
        print(a.__b)
    def dis1(self):
        b=a.b
        self.c=a.__b
        print(b)
        print(self.c)
    def dis2(self):
        print(self.b)
        print(self.__b)
        print(self.c)
x=a()
x.dis()
x.dis1()
x.dis2()
print(x.c)