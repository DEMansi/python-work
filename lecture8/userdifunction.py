#function with no argument & no return value.

def printline():
    print("*"*50)

printline()
print("welcom to user defined function in python.")
printline()

#function with argument but no return value.

def add(a,b):
    print("addition :",a+b)

printline()
x=int(input("enter value:"))
y=int(input("enter value:"))
add(x,y)
printline()

#function with argument & return value.

def sub(a,b):
    return a-b

printline()
x=int(input("enter value:"))
y=int(input("enter value:"))
#add=sub(x,y)
print("subtraction:",sub(x,y))
printline()
    
