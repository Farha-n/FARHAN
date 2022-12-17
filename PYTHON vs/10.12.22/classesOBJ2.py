class car:
    wheels = 4
     #Instance Variables : value varies from object to object
     # Static Variable : shared by the  whole class
    def __init__(self):
        self.company = "BMW"
        self.mileage = 10
car1 = car()
car2 = car()
car.wheels = 5
print(car1.mileage,car1.wheels)
print(car2.mileage,car2.wheels)