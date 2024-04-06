#Write a python program to find the longest words.

file=open("demo.txt","r")
print(max(file.read().split(),key=len))
file.close()
