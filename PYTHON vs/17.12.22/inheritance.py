class A:
    def __init__(self):
        print("Init of class A")
    def method1(self):
        print("This is Method 1")

    def method2(self):
        print("This is Method 2")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init of class B")
    def method3(self):
        print("This is Method 3")
    def method4(self):
        print("This is Method 4")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("Init of class C")
    def method5(self):
            print("This is Method 5")



obj = C()

