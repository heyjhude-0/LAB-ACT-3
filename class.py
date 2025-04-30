from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    
    def log_transaction(self, transaction_type, payment_mode):
        self.transaction_type = transaction_type
        self.payment_mode = payment_mode
        print(f"{self.payment_mode} {self.transaction_type} Transaction")
        print(f"Account Name: {self.account_name}")
        print(f"Remaining Balance: {self.balance}")

    def is_balance_sufficient(self):
        if self.balance > self.amount:
            return True
        else:
            return False

    def pay(self, amount):
        pass
        
    def refund(self, amount):
        pass

@abstractmethod
class GCash(PaymentMethod):
    def __init__(self, account_name, balance, phone_number):
        super().__init__(account_name, balance)
        self.phone_number = phone_number

    def pay(self, amount):
        self.log_transaction("PAYMENT", "GCash")
        if self.is_balance_sufficient:
            self.balance -= amount
            print(f"Paid {amount} via Gcash. Your new balance is {self.balance}")
        else:
            print(f"Payment Error, Insufficient Balance")



    
payment1 = GCash("Jhude Dagle", 200, "09814415993")
payment1.pay(50)