#single inheritance
class A:
    def func1(self):
        print("This is function 1 from class A")
    def func2(self):
        print("This is function 2 from class A")
class B(A):
    def func3(self):
        print("This is function 3 from class B")
    def func4(self):
        print("This is function 4 from class B")
obj=B()
obj.func1()
obj.func2()
obj.func3()
obj.func4()                