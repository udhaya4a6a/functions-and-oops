class payment:
    def pay(self):
       print("payment making")
class card(payment):
    def pay(self):
        print("payment from credit card")
class UPI(payment):
    def pay(self):
        print("payment from UPI")
payments=[card() , UPI()]
for p in payments:
    p.pay()