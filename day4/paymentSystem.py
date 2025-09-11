class Payment:
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print("Payment of amount:",self.amount)

class CashPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid ₹{self.amount} in cash")

class CardPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid ₹{self.amount} using credit/debit card")

class UPIPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid ₹{self.amount} using UPI")


ca_pay = CashPayment(1000)
car_pay = CardPayment(1000)
up_pay = UPIPayment(1000)
payment_list = [ca_pay,car_pay,up_pay]
for p in payment_list:
    p.pay()