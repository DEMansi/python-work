#Write a Python program to read a file line by line and store it into a list

l1=[]

file=open("demo.txt","r")

for i in file:
    print(i)
    l1.append(i)
print(l1)   
