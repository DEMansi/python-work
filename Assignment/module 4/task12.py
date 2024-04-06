#Python program to copy the contents of a file to another file

file1=open("demo.txt","r") 
file2=open("demo2.txt","a")

for i  in file1:
    file2.write(i)
file1.close()
file2.close()
