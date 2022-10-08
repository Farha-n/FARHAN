a = 5
b = 10

if b < a:
    print("Yes")
else:
    print("No")

#Take x and y two variables and assign them value
#if x is less than y, print yayy
#else print nayy 
x = input("enter the number ")
y = input("enter the number_2 ")
if x < y:
    print("yayy")
else:
    print("nayy")


# Take values of length and breadth from user
# print if it is a square or not 
length = input("enter the value ")
breadth = input("enter the value_2 ")
if length == breadth:
    print("square")
else:
    print("rectangle")


# A company decided to give bonus of 1000Rs to
#employee if his/her service is more than 5 years 
#Ask user their salary and year of service and print
#the net bonus amount

salary = int(input("enter salary"))
years_of_service =int(input("enter years_of_service"))
if years_of_service > 5:
    addition = salary + 1000
    print(addition )
else:
    print(salary)


