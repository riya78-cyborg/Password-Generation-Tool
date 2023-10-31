import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)

plength  = int(input("Enter the password length for pass generation: "))
print("Your new password is : ")
print("".join(s[0:plength]))
