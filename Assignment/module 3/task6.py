
# Write a Python program to count the number of strings where the string 
#length is 2 or more and the first and last character are same from a given 
#list of strings.

l = ["hello", "world","mansi", "python", "aarohi", "ridhi"]
count=6

for i in l:
    if len(i)>2 and i[0]==i[-1]:
        count+=1
print(count)        
