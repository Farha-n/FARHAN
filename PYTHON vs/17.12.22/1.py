class Student:

    collegeName = "LPU"

    def __init__(self, python, web,math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
    def avg(self):
        return(self.subject1 + self.subject2 + self.subject3)/3
    # def get_subject1(self):
    #     return self.subject1

    # def set_marks(self,value):
    #     self.subject1 = value
    # Below is a class method
    @classmethod
    def collegeDetail(cls):
        return cls.collegeName 
    



Student1  = Student(90, 80, 95)
Student2 = Student(100, 85, 70)
print(Student1.avg())

print(Student.collegeDetail())
