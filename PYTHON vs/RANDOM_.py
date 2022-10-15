import random

print(random.randrange(0,55))


String="HELLO_WORLD"
print(String[2])
print(String[:-1])
print(String[3:-2])
print(String[-1:0])
print(String[:4])
print(len(String))


# ARRAY : SIMILAR DATA TYPE
#LIST : DIFFERENT DATA TYPE

#in

quote = "A quick brown fox jumps over the lazy dog"
if "quick" in quote:
    print("Yes")
else:
    print("No")


if "quick" not in quote:
    print("yay")
else:
    print("nay")