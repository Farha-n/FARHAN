import re
value = "This is a string"
output=re.search("^this is .*string$",value )
print(output)


pattern = r"^(?=.*[a-z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"