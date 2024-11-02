#Banking Project:-
class account_details:
    def owner(self,name,accountt):
        self.name = name
        self.acountt = accountt
        self.balance = 0 
    
    def __str__(self):
        return f"Account Owner : {self.name}\nAccount Type : {self.acountt} Acc\nBalance : {self.balance}\n"
        
        

class account:
    #firstly initial
    def __init__(self,details):
        self.details = details
        self.balance = 0

    def credit(self,value):
        self.details.balance += value
        print(f"*Credit Money : +{value}\nCurrent Money : {self.details.balance}")
        
        
        
    
    def debit(self,value):
        if value <= self.details.balance:
            self.details.balance -= value
            print(f"\n*Debit Money :-{value}\nCurrent Money : {self.details.balance}\n")
        else:
            
            print("\n**Transcation Failed**\n**Insufficient Funds**\n")
        
    def __str__(self):
        return str(self.details)
        
    
        
l = account_details()
l.owner("Pushkar","saving")
print(l)

y = account(l)
y.credit(50)
y.debit(20)
print(y)
    