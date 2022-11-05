#create a function to print your name and age

def name(a,b):
    print("my Name is:"+a,b)

name("Rishita",19)
name("chobey",18)
name("iram",18)

#write a program to create a fn using following conditions
#it should accept any employer
#if the salary is missing then assign the default value as 10000 to salary
#Ben(12000) mike(15000)#bob()

def may(name,salary=10000):
    print("The employee is :"+name)
    print("His salary is : ", int(salary))

may("ben",12000)
may("mike",15000)
may("bob")