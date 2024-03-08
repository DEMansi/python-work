
#Write a Python program to remove an empty tuple(s) from a list of tuples.

l1= [(),('.') ,('a', 'b'), ('9','6','3'), ('a', 'b', 'c'), ('d'), ('0')]
l1=[t for t in l1 if t]
print(l1)
