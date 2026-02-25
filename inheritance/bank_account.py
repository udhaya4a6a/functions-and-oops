class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
class savings_account(Bankaccount):
    def add_interest(self,x):
        print("after adding Interest:",end=" ")
        self.balance=self.balance + (self.balance * x)
x=float(input("enter the percentage of interest: ")) /100
obj=savings_account("udhaya",5000)
obj.deposit(1000)
obj.add_interest(x)
print(obj.balance)
