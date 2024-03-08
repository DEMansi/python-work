
#Write a Python program to find the repeated items of a tuple.

l=(1,2,3,90,10,20,30,1,2,3,1,20,90)
l1=[]
for i in l:
    if i not in l1 and l.count(i)>1:
        l1.append(i)

print(l)
print(l1)
