a = int(input("enter"))
if a%2==0:
    print("even")
else:
    print("odd")


years_of_service=int(input("Years"))
Salary=int(input("Add"))
Bonus=Salary + (10/100)*Salary
Bonus2=Salary + (8/100)*Salary
Bonus3=Salary + (5/100)*Salary


if years_of_service > 10:
      print(Bonus)
elif years_of_service>6 and  years_of_service <=10:
    print(Bonus2)
elif years_of_service<=6 and  years_of_service >0:
    print(Bonus3)
else:
    print(Salary)
