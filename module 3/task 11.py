#Write a Python function that takes a list and returns a new list with unique 
#elements of the first list.

l=[1,2,3,4,5,6,7,8,9,10,4,5,6]
l1=[]

for i in l:
    if i not in l1:
        l.count(i)>1
        l1.append(i)
print(l)
print(l1)
