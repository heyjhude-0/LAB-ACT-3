from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, account_name, balance):
        self.__account_name = account_name  
        self._balance = balance             
    
    def log_transaction(self, transaction_type, payment_mode):
        self.transaction_type = transaction_type
        self.payment_mode = payment_mode
        print(f"\n{self.payment_mode} {self.transaction_type} Transaction")
        print(f"Account Name: {self.__account_name}")
        print(f"Remaining Balance: {self._balance}")

    def is_balance_sufficient(self, amount):
        return self._balance >= amount

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod   
    def refund(self, amount):
        pass

class GCash(PaymentMethod):
    def __init__(self, account_name, balance, phone_number, email):
        super().__init__(account_name, balance)
        self._phone_number = phone_number
        self._email = email

    def pay(self, amount):
        self.log_transaction("PAYMENT", "GCash")
        if self.is_balance_sufficient(amount):
            self._balance -= amount
            print(f"Paid ₱{amount} via GCash. New balance: ₱{self._balance}")
            print(f"Receipt sent to {self._email}")
        else:
            print("Payment error: Insufficient balance.")

    def refund(self, amount):
        self.log_transaction("REFUND", "GCash")
        self._balance += amount
        print(f"Refunded ₱{amount} via GCash. New balance: ₱{self._balance}")
        print(f"Details are sent to {self._email}")

class Maya(PaymentMethod):
    def __init__(self, account_name, balance, phone_number, email):
        super().__init__(account_name, balance)
        self._phone_number = phone_number
        self._email = email

    def pay(self, amount):
        self.log_transaction("PAYMENT", "Maya")
        if self.is_balance_sufficient(amount):
            self._balance -= amount
            print(f"Paid ₱{amount} via Maya. New balance: ₱{self._balance}")
            print(f"Receipt sent to {self._email}")
        else:
            print("Payment error: Insufficient balance.")

    def refund(self, amount):
        self.log_transaction("REFUND", "Maya")
        self._balance += amount
        print(f"Refunded ₱{amount} via Maya. New balance: ₱{self._balance}")
        print(f"Details are sent to {self._email}")

class CreditCard(PaymentMethod):
    def __init__(self, account_name, balance, credit_limit, email):
        super().__init__(account_name, balance)
        self._credit_limit = credit_limit
        self._email = email

    def pay(self, amount):
        self.log_transaction("PAYMENT", "Credit Card")
        available_credit = self._balance + self._credit_limit
        if amount <= available_credit:
            self._balance -= amount
            print(f"Charged ₱{amount} to credit card. New balance: ₱{self._balance}")
            print(f"More details are sent to {self._email}")
        else:
            print("Payment declined: Credit limit exceeded.")

    def refund(self, amount):
        self.log_transaction("REFUND", "Credit Card")
        self._balance += amount
        print(f"Refunded ₱{amount} to credit card. New balance: ₱{self._balance}")
        print(f"Details of your refund is sent to {self._email}")

class BankTransfer(PaymentMethod):
    def __init__(self, account_name, balance, account_number, bank_name):
        super().__init__(account_name, balance)
        self.__account_number = account_number
        self._bank_name = bank_name

    def pay(self, amount):
        self.log_transaction("PAYMENT", "Bank Transfer")
        if self.is_balance_sufficient(amount):
            self._balance -= amount
            print(f"Paid ₱{amount} via Bank Transfer from {self._bank_name}. New balance: ₱{self._balance}")
        else:
            print("Payment error: Insufficient balance.")

    def refund(self, amount):
        self.log_transaction("REFUND", "Bank Transfer")
        self._balance += amount
        print(f"Refunded ₱{amount} to Account Number #{self.__account_number}. New balance: ₱{self._balance}")

# GCash 
payment1 = GCash("J***el P.", 200, "09953167434", "kimjimuelperez@gmail.com")
payment1.pay(100)
payment1.refund(50)

# Maya
payment2 = Maya("Jhude Dagle", 500, "09123456789", "emailnijhude@gmail.com")
payment2.pay(200)
payment2.refund(45)

# Credit Card 
payment3 = CreditCard("Bacay, Kotnie", 500, 5000, "akosikotnie@gmail.com")
payment3.pay(1000)
payment3.refund(300)

# Bank Transfer
payment4 = BankTransfer("Mickhael Casanova", 6000, "009876", "BDO")
payment4.pay(1500)
payment4.refund(500)
