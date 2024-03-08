
#Write a Python script to check if a given key already exists in a dictionary.

d={1:"Ridhi",2:"Mansi"}
n=int(input("enter value = "))
if d.get(n):
    print("exites in directry")
else:
    print("not exites in directrty")
