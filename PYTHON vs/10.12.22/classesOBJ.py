# class Laptop:
#     def __init__(self):
#         print("Hello World")
#     def config(self):
#         print("Asus","i7","1TB")

# Laptop1 = Laptop()
# Laptop2 = Laptop()
# Laptop().config(Laptop1)
# Laptop1.config()
# Laptop2.config()



# class Student:
#     def __init__(self,name,rollNo):
#             self.name = name
#             self.rollNo = rollNo
#     def info(self):
#         pass
#         print("name is : ", self.name,"and","rollNo is : " , self.rollNo)
# Student1 = Student("Shivam","34")
# Student2 = Student("IraM","30")
# Student1.info()
# Student2.info()
# class Person:
#     def __init__(self):
#         self.name = "Ishan"
#         self.number = 32
# p1 = Person()
# p2 = Person()


# print(p1.name,p1.number)
# print(p2.name,p2.number)






class Person:
    def __init__(self):
        self.name = "Ishan"
        self.number = 32

    def compare(self,other):
        if(self.number == other.number):
            return True
        else:
            return False

p1 = Person()
p2 = Person()
p2.number = 31
if p2.compare(p1):
    print("same")
else:
    print("diff")

print(p1.number)
print(p2.number)