#Write a Python program to count the number of lines in a text file.

file=open("demo.txt","r")
a=len(file.read().split())
print("Total count line is : ",a)
file.close()
