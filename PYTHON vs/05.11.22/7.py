# print("Name:",name,"Salary:",salary)
#a=input("Name")
#my_func("ABC")

#recursion

def sum_recursion(num):
    if num==0:
        return num
    return num+sum_recursion(num-1)

ans = sum_recursion(4)
print(ans)

def fff(a):
    if a==0:
        return 1
    return a*(fff(a-1))
an=fff(5)
print(an)