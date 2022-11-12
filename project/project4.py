#import the necessary modules!
import random
import string

print('hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))
#define data 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine the data
all = lower + upper + num + symbols

#use randoms
temp = random.sample(all,length)

#create the password
password = "".join(temp)

#print the password
print("The Password is : " ,password)