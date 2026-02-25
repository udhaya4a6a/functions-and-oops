# bank_account.py 
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def depposit(self,ammount):  #here self is used to refer to the instance of the class(balance variable ah self ndra keyword use panni indha function method ku ulla use pannikalam)
        self.balance+=ammount
        
    def withdraw(self,ammount):
        if self.balance > ammount:
            self.balance-=ammount
        else:
            print("insufficient balance")    
a=input("enter your name:")

acc=BankAccount(a,5000)
while True:
    print("\nenter 1 for check Balance: ")
    print("enter 2 for depposit: ")
    print("enter 3 for withdraw: ")
    print("enter 4 for Exit: ")

    choice = int(input("enter your choice: "))

    if choice == 1:
        print(f"Name : {acc.name} | Balance : {acc.balance}")
        print("=================================================")

    elif choice == 2:
        acc.depposit(int(input("enter the ammount to depposit: ")))
        print(f"Updated Balance : {acc.balance}")
        print("=================================================")

    elif choice == 3:
        acc.withdraw(int(input("enter the ammount to withdraw: ")))
        print(f"Updated Balance : {acc.balance}")
        print("=================================================")

    elif choice == 4:
        print("thank you")
        break

    else:
        print("Invalid choice, try again")
    
    

    
