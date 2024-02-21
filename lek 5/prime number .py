n=int(input("enter n:"))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"is not prime")
            break
    else :
          print(n,"is prime")
else:
    print(n,"is not prime")
