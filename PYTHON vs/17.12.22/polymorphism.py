# print(len("Hello"))
# print(len[10,20,30])

# def add(x,y,z = 0):
#     return x+y+z

# print(add(3, 4))
# print(add(3, 4, 5))
# def add(x,y,z=0):
#     return x+y+z

# class India:
#     def capital(self):
#         print("New Delhi")
#     def language(self):
#         print("Hindi")
#     def type(self):
#         print("Developing")
# class USA:
#     def capital(self):
#         print("Washington DC")
#     def language(self):
#         print("English")
#     def type(self):
#         print("Developed")
# obj1=India()
# obj2=USA()
# for i in (obj1,obj2):
#     i.capital()
#     i.language()
#     i.type()
# class Bird:
#     def wings(self):
#         print("Bird has two wings")
#     def eyes(self):
#         print("Bird has two eyes")
#     def fly(self):
#         print("Most of the birds can fly")
# class Sparrow(Bird):
#     def fly():
#         print("Saprrow can fly")
# class Ostrich(Bird):
#     pass
#     # def fly(self):
#     #     print("Ostrich can't fly")

# bird = Bird()
# Sparrow = Sparrow()
# ostrich = Ostrich()
# bird.eyes()
# bird.wings()
# bird.fly()
# ostrich.fly()

# Create a car class without any variables and methods
class car:
    pass
car1 =car()
class vehicle:
    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage

class BUS(vehicle):
     pass

obj = BUS("ABC",10)


print(obj.mileage, obj.name)