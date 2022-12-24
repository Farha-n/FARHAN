f = open("PYTHON vs/24.12.22/demo.txt","r")
# print(f.read())
# print(f.readline())
# # print(f.readline())

f1=open("PYTHON vs/24.12.22/demo.txt", "w")
# f1.write("hello\n")
# f1.write("this is  a random text")

for i in f:
    f1.write(i)
# f2=open("My Self.txt","w")
# f2.write("My name is Rishita Chauhan.\n")
# f2.write("I am from Shimla.\n")
# f2.write("I am a Student.\n")
# f2.write("I am doing B.Tech CSE.\n")
# try:
#     f=open("demo.txt")
#     #your codes goes here
# finally:
#     f.close()
#this way we are making sure that file is closed properly even if raised that cause the program flow to stop. 
# with open("demo.txt") as f:
#     f.read() #-->example
#     #your codes goes here
#tell
# print(f.tell())
# f=open("PYTHON vs/24.12.24.12.22/img.png","wb")
# print(f.read())
# for i in f:
#       f1.write(i)


import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("File does not exist")