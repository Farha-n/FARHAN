a = int(input())
for i in range(0,a+1):
    if i%5==0:
        continue
    print(i)


n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    