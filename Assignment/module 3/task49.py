#Write a Python function to check whether a number is perfect or not. 

a = int(input(" Please Enter any Number: "))
b = 0
for i in range(1, a):
    if(a % i == 0):
        b = b + i
if (b == a):
    print(a,"is a Perfect Number")
else:
    print(a,"is not a Perfect Number")
