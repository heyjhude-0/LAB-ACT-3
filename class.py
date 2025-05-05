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

    def is_balance_sufficient(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod   
    def refund(self, amount):
        pass


class GCash(PaymentMethod):
    def __init__(self, account_name, balance, phone_number):
        super().__init__(account_name, balance)
        self.phone_number = phone_number

    def pay(self, amount):
        self.log_transaction("PAYMENT", "GCash")
        if self.is_balance_sufficient(amount):
            self.balance -= amount
            print(f"Paid {amount} via Gcash. Your new balance is {self.balance}")
        else:
           print(f"Payment Error, Insufficient Balance")

    def refund(self, amount):
        self.log_transaction("REFUND", "GCash")
        self.balance += amount
        print(f"Refunded {amount} via Gcash. Your new balance is {self.balance}")
        



    
payment1 = GCash("Juan Dela Cruz", 200, "09814415993")
payment1.pay(100)
