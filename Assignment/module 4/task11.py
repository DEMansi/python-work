#Write a Python program to write a list to a file.

l=['abcd','efgh','ijkl']

file=open("myfile.txt","w")

for i in l:
    file.write(i+"\n")
    print(i)

file.close()
