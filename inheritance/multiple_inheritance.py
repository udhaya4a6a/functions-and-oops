#multiple inheritance.
#when a class is derived from more than one base class it is called multiple inheritance.
#syntax:
#class derived_class(base_class1,base_class2,...):
#    body of derived class
class Animal:  #base class1
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class pet:    #base class2
    def __init__(self,owner):
        self.owner=owner
class admin(Animal,pet): #Derrived class
    def __init__(self,name,age,owner):
        #instead of using super() to call the base/parent class we can directly call the required base class by its name because here we have more than 1 parent class.
        Animal.__init__(self,name,age)
        pet.__init__(self,owner)
    def Dog(self):
        print(f"hey this is {self.name} and its age is {self.age}")
        print(f"The Owner of this {self.name} Dog is {self.owner}.")
        print(" ")
        print("===============================")
        print(" ")
obj1=admin("pit bull",6,"virat kholi") #creating object1
obj1.Dog()

obj2=admin("German shippard",3,"udhaya") #creating object2
obj2.Dog()