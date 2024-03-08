'''
if:
  statement
else:
  ststement
'''

a=int(input("enter a:")) 
b=int(input("enter b:")) 
c=int(input("enter c:")) 

if a>b: 
    if a>c: 
        print(a,"is max number")
    else:
        print(c,"is max number")
elif b>c: 
    print(b,"is max number")
else:
    print(c,"is max number")
    
