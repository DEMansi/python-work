class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello",self.cname,",your Account Number",self,acno,"Is Opened with",self.balance,"Rs.")
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Sorry you Need Another",amount-self.balance,"Rs.")
    def checkBalance(self):
        print("your Current Balance IS :",self.balance)
        
b1=Bank()
acno=int(input("Enter Account Number :"))
cname=(input("Enter Name Of Customer :"))
balance=int(input("Enter Initial Balance :"))

b1.openAccount(acno,cname,balance)

while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)

    choice=int(input("Enter Your Choice :"))
    print("*"*50)

    if choice==1:
        amount=int(input("Enter Deposit Amount :"))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount :"))
        b1.Withdraw(amount)
        print("*"*50)
    elif choice==3:
        amount=int(input("Enter Check Balance Amount :"))
        b1.CheckBalance()
        print("*"*50)
    elif choice==4:
        print("Thank You For Using Our Services.")
        print("*"*50)
        break
    else:
        print("Invalid Choice. Please Try Agin.")
        print("*"*50)
        
