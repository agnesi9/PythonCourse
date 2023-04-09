#Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
#It should also have methods called deposit() and withdraw() that update the balance accordingly.

class BankAcc:
    def __init__(self, acc_number:int, balance:int, owner_name:str) -> None:
        self.acc_number = acc_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self,deposit_amount:int):
        self.balance += deposit_amount
        return self.balance
    
    def withdraw(self,withdraw_amount:int):
        self.balance -= withdraw_amount
        return self.balance
    
acc1 = BankAcc(234,2995,"Agne")
print(BankAcc.deposit(acc1,304))
print(acc1.withdraw(4))
