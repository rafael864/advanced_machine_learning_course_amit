class bank_account():
    def __init__(self,intial_balance):
        try:
            if  intial_balance <= 0:
                print('invalid negative numbers')
            elif intial_balance > 0:
                self.total_balance = intial_balance
        except:
            print('invalid character')
        
    def deposit(self,dep):
        try:
            if  dep <= 0:
                print('invalid negative numbers')
            elif dep > 0:
                self.total_balance += dep
        except:
            print('invalid character')
            
    def withdraw(self,draw):
        try:
            if  draw <= 0:
                print('invalid negative numbers')
            elif draw > 0:
                self.total_balance -= draw
        except:
            print('invalid character')
            
    def check_acount(self):
        print(self.total_balance)        
if __name__ == "__main__":        
    mina_account = bank_account(50)
    mina_account.deposit(10)
    mina_account.deposit(24)
    mina_account.deposit(15)
    mina_account.withdraw(12)
    mina_account.withdraw(36)
    mina_account.check_acount()
    mina_account.withdraw(17)
    mina_account.check_acount()