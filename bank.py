

class Account:
    
    name=''
    number=0
    balance=0
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.balance = 0
        
    def get_balance(self):
        return self.balance
    
    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        