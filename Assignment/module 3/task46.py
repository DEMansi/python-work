#Write a Python program to create a dictionary from a string. 
#Note: Track the count of the letters from the string. 
#Sample string: 'w3resource'

a = input("Enter a string: ")

d1 = {}

for i in a:  
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

print(d1)
