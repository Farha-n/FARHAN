colors=["red","blue","red"]
cars=["tata","nano","fortuner"]
players=["ishaan","messi","dravid"]
colors.replace(2,"white")
#colors.insert(2,"messi")
#colors.append("sid")
print(colors)
#cl=['Red','Green','Yellow','Blue','White']
#print(cl)
#b=['Red','Green','Yellow','Blue','White',12,13]
#print(b[0:4])
#l=['Red','Green','Yellow','Blue','White']
#l[3]=23
#print(l)
#l[1]="Black"
#print(l)
#colors=['Red','Blue','Red','Black',22]
#colors[0:2]=['Yellow','Pink']
#colors[0]='Yellow'
#colors[1]='Pink'
#######    INSERT OBJECT BEFORE INDEX
#colors=['Red','Blue','Red','Black',22]
#colors.insert(1,"Indigo")
#colors.append("BMw")

#print(colors+cars)
#colors.extend(cars)
#colors.extend(players)

#colors.remove("Red")
#colors.pop(1)
#colors.clear()
colors=['Red','Blue','Red','Black',22]
cars=['TATA','Nano','BMW',"Jeep","Alto"]
players=['Shreyas Iyer',"Rohit",'Neymar','Messi']
#for x in players:
 #   print(x)
#for x in range(len (players)):
 #   print(players [x] )
#x=0
#while x < len(players):
#    print(players[x])
#for direct     [print (x) for x in players]
newlist=[]
for i in cars:
    if 'A' in i:
        newlist.append(i)
print(newlist)