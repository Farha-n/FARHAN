colors=["Red","Blue","Red","Black"]
cars=["Tata","Nan0","Alto","Jeep"]
newlist=[x for x in cars if x == "Tata"]
print(newlist)

colors=["Red","Blue","Red","Black"]
cars=["Tata","Nano","Alto","Jeep"]
newlist=[x for x in cars if x != "Tata"]
print(newlist)


colors=["Red","Blue","Red","Black"]
cars=["Tata","Nano","Alto","Jeep"]
newlist=[x.lower() for x in cars]
print(newlist)


colors=["Red","Blue","Red","Black"]
cars=["Tata","Nano","Alto","Jeep"]
numbers=[1,2,3,4,6,42,10]
numbers.sort()

print(numbers)


colors=["Red","Blue","Red","Black"]
cars=["Tata","Nano","Alto","Jeep"]
numbers=[1,2,3,4,6,42,10]
numbers.sort(reverse=2)

print(numbers)



colors=["Red","Blue","Red","Black"]
cars=["Tata","Nano","Alto","Jeep"]
numbers=[1,2,3,4,6,42,10]
colors.sort(reverse=1)

print(numbers)
