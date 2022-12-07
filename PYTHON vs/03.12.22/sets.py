#•	Sets is a non-homogenous but stores in single variable
# •	Representation= {}
# •	no Duplicate element 
# •	unchangeable
#   unordered
#   we can add new item  & remove an item
set={"cars","boat","bike"}
print(set)
#no Duplicate element 
set1={"cars","boat","bike",1}
print(set1)
print(len(set))
if "bike" in set:
    print("True")
else:
    print("False")
#add new item
set.add("Cycle")
print(set)
#remove
set.remove('boat')
print(set)
myset1={1,2,3,4}
myset2=set1.union(myset1)#addition of two sets
print(myset2)
myset3=myset1.intersection(myset2)
print(myset3)
myset4=myset1.symmetric_difference(set1)
print(myset4)