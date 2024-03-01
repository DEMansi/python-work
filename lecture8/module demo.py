import UDF

while True:
    print("*"*50)
    print("1. oddeven")
    print("2. maxoftwo")
    print("3. maxofthree")
    print("4. fibonacci")
    print("5. prime")
    print("6. exit")
    print("*"*50)

    choice=int(input("enter your choice:"))
    print("*"*50)

    if choice==1:
         a=int(input("enter a value:"))
         UDF.oddeven(a)
         print("*"*50)
    elif choice==2:
         a=int(input("enter a value:"))
         b=int(input("enter a value:"))
         UDF.maxoftwoa()
         print("*"*50)
    elif choice==3:
         a=int(input("enter a value:"))
         b=int(input("enter a value:"))
         c=int(input("enter a value:"))
         UDF.maxofthree(a)
         print("*"*50)
    elif choice==4:
         a=int(input("enter a value:"))
         UDF.fibonacci(a)
         print("*"*50)
    elif choice==5:
         a=int(input("enter a value:"))
         UDF.prime(a)
         print("*"*50)
    elif choice==6:
         print("thank you for using our services..")
         print("*"*50)
         break
    else:
         print("invalid choice.please try again")
         print("*"*50)

         
           
         
                  
