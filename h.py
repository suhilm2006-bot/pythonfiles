class bankAccount:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited.")
        else:
            print("invalid amount.")
            
    def withdraw(self, amount):
        if amount <= 0:
            print("invalid amount.")
            
        elif amount > self.balance:
            print("Insufficent balance.")
            
        else:
            self.balance -= amount 
            print("amount withdrown.")
            
    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:",self.balance)
        
    
name = input("Enter your name:")

account = bankAccount(name)

while True:
    
    print("\n--- BANKING SYSTEM ---")
    print("1. Deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)
        
    if choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)
        
    elif choice =="3":
        account.show_balance()
    elif choice == "4":
        break
    
    else:
        print("invalid choice")
        