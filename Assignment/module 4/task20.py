#program that user to enter only odd numbers, else will raise an exception.
    
num = int(input("Enter a number: "))
mod = num % 2  
if mod > 0:
    print("Odd Number")
else:
    print("Invalid Input")
