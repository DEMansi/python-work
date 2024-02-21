s=input("Enter A String")



al=0
num=0
sp=0
uc=0
lc=0

for i in s:
    if i.isalpha():
         al=al+1
    elif i.isspace():
        sp=sp+1
    elif i.isnumeric():
        num=num+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("Total Number Of Alphabets :",al)
print("Total Number Of numericls :",num)
print("Total Number Of space :",sp)
print("Total Number Of upper case :",uc)
print("Total Number Of lower case :",lc)
