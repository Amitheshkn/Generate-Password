import random 
import string

lower=string.ascii_lowercase
upper=string.ascii_uppercase
numbers="0123456789"
symbols="[]{}();/?,.-_!@#$%^&*:"
    
all=lower+upper+numbers+symbols
print("Enter the length of the password to be generated")
length=int(input())
password="".join(random.sample(all,length))
print(password)
