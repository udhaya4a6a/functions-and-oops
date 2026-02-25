#hierarchical inheritance
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
class C(A):
    def func5(self):
        print("This is function 5 from class C")
    def func6(self):
        print("This is function 6 from class C")
obj1=B()
obj1.func1()
obj1.func2()
obj1.func3()
obj1.func4()
obj2=C()
obj2.func1()
obj2.func2()
obj2.func5()
obj2.func6()                