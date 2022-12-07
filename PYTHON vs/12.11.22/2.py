num=[1,2,3,4,5]
#Write a program to turn every item of list into its square
new = []
for i in num:
    i=i*i
    new.append(i)
print(new)

num=[1,2,3,4,5]
new_list=[x*x for x in num]
print(new_list)


numbers=[1,2,3,4,5,2,6]
indx=numbers.index(2)
numbers[indx] = 200
print(numbers)

numbers=[1,2,3,4,5,2,6]
num2=numbers.copy()
print(num2)



list1=["x","y","z"]
list2=[1,2,3]
#list3=list1 + list2
#print(list3)
#list1.append(list2)
#print(list1)


for x in list2:
    list1.append(x)
print(list1)


