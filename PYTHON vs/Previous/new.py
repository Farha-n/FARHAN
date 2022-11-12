#Take user input (string)
#if the len of string is greater than 3 add 'ing' as a  suffix in the orginal string 
#else print the same  string given by the user

a=str(input("Enter: "))
if len(a)>3:
     print(a+"ing")
else:
   print(a)


a=10
b=5
c=15
d=20
str="a = {2}, b= {0},c= {3},d= {1}"
print(str.format(c,d,b,a))

#While loop
a= 1

while a < 10:
    print(a)
    a = a+ 1

a=1
while a<10:
    a=a+1

    if a ==5 :
        continue
    print(a)


a=1
while a<10:
    a=a+1

    if a ==5 :
        break
    print(a)






