#Write a Python program to read first n lines of a file. 

n = int(input("Enter Lines To Read : "))
file = open("demo.txt","r")
for i in range(n):
    print(file.readline())
