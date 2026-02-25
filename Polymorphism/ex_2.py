class car:
    def move(self):
        print("car is moving!")
class person:
    def move(self):
        print("person driving a car")
def start_moving(obj):  #public function defiination and obj is the parameter
    obj.move()          #calling the move method of the object passed as parameter
start_moving(car())     #creating an instance of the car class and passing it to the start_moving function so obj.move is converted to car.move() and it will print "car is moving!"
start_moving(person())    