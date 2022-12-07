def iseven(i):
    return i%2==0
def isodd(i):
    return i%2!=0
list1=[3,4,5,7,8,18,66,13,10,15]
evenNum=list(filter(iseven,list1))
print(evenNum)
oddNum=list(filter(isodd, list1))
print(oddNum)


list2=[5,6,24,25,12,75,8,7,5,3]
evNum=list(filter(lambda i : i%2==0, list2))
print(evNum)
odNum=list(filter(lambda i : i%2!=0, list2))
squareNum=list(map(lambda i : i**2, list1))
sqNum=list(map(lambda i : i**2, list2))
print(odNum)
print(squareNum)
print(sqNum)

list3=[10,20,30,40,50]
#triple the values of the list
triple=list(map(lambda i : i*3, list3))
print(triple)
#homework to convert lower case in upper case and vice versa
list4=["a","B","C","D","e","f"]
lower_case=list(map(lambda i: i.lower(), list4))
print(lower_case)


def div(a,b):
    print(a/b)
div(2,4)
div(4, 2)

def good_div(func):
    def inner_div(a,b):
        if a<b:
            a,b==b,a
        return func(a,b)

    return inner_div
div = good_div(div)
div(2,4)