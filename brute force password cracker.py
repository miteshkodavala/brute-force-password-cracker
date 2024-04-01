import string
import random

password = input("enter the password : ")

char = list(string.printable)

# print character

while True:
    var=random.choices(char, k=len(password))
    print(">>>>>>>>>", var, "<<<<<<<<<")
    ps = "".join(var)
    if password == ps:
        print("your password is ", ps)
        break