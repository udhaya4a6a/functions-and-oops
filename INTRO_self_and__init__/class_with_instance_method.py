# class_with_instance_method.py
# Example of a class with instance methods using 'self'
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} says woof woof!")
    def get_age(self):
        print(f"{self.name} is {self.age} years old.")
dog1=dog("Buddy",3)
dog1.bark() , dog1.get_age()     
dog2=dog("Max",5)
dog2.bark() , dog2.get_age()           