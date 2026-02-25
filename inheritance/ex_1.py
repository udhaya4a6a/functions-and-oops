#single inheritance example with car and BMW class where BMW is inheriting properties of car class and also has its own property is_selfdriving
class car:
    def __init__(self,windows,tiers,enginetype):
        self.windows=windows
        self.tiers=tiers
        self.enginetype=enginetype

    def drive(self,name):
        self.name=name
        print(f"{self.name} driving a {self.enginetype} car.")

class BMW(car):
    def __init__(self,windows,tiers,enginetype,is_selfdriving):
        super().__init__(windows,tiers,enginetype)
        self.is_selfdriving = is_selfdriving

    def selfdriving(self):
        print(f"BMW is self Driving: {self.is_selfdriving}")
        print("===================================================")

obj=BMW(6,8,"petrol",True)
obj.drive("udhaya")
obj.selfdriving()

obj2=BMW(16,18,"Electric",False)
obj2.drive("Paramu")
obj2.selfdriving()
