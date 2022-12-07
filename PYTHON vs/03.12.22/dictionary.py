#Dictionary used to store values in key:value pairs
myDictionary={
    "name":"Nikhil",
    "age":"22",
    "percent":"80.5"
}

print(myDictionary)
#ordered 
#changeable
#does not allow duplicate value
#get used for printing all the keys
#age=myDictionary.get("age")
#print(age)
#keys used for printing all the keys
#keys=myDictionary.keys()
#print(keys)
#values is used to print all the values 
#values=myDictionary.values()
#print(values)
#ITEMS PRINT THE LIST OF TUPPLES    
#items=myDictionary.items()
#print(items)
myDictionary["Roll_number"]=12
print(myDictionary)
myDictionary.update({"age":33})
print(myDictionary)
# POP REMOVE ITEM
#POPITEM REMOVES LAST ITEM
#
# myDictionary.pop("percent")
print(myDictionary)
myDictionary.popitem()
print(myDictionary)