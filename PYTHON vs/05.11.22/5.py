def details(name,*data):
    print(name)
    print(data)


details("Rishita","Shimla",19,9596587890)

def details(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


details("Farhan",place="Kashmir",age=20,no=9682671112)


a=10

def func():
    a=15
    print(a)

func()
print(a)