#Money Management:-
from prettytable import PrettyTable
import time
class Node:
    def __init__(self,value,reason,mode):
        self.data = value
        self.date_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.reason = reason
        self.mode = mode
        self.next = None
        
class Linked_list:
    
    def __init__(self):
        self.head = None
        self.balance = 0

        
        
    def debit(self,value):
        #it's takes money
        
        if value > self.balance:
            return 'Insufficent Balance'
        
        
        
        self.balance -= value
        print("Reason:-\n(1) Groccery\n(2) Medical\n(3) Furniture\n(4) Personal")
        reason = ""
        while True:
            
            try:
                
                num = int(input(">>"))
                    
                if num == 1:
                    reason = "Groccery"
                elif num == 2:
                    reason = "Medical"
                elif num == 3:
                    reason = "Furniture"
                elif num == 4:
                    reason = "Personal"
                else:
                    print("valid number (1-4)")
                    continue
                break
                
            except ValueError:
                
                print(f"Enter valid details{num}")
                
                
        new_node = Node(value,reason,"Debit")
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next !=None:
                current = current.next
            current.next = new_node #end node  of attach  of address
            
            
            
            
        
            
    def credit(self,reason,value):
        self.balance += value 
        new_node = Node(value,reason,"Credit")
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next !=None:
                current = current.next
                
            current.next = new_node
            

        
                

        
        
        
    def stmnt(self):
        if self.head == None:
            return 'bank balance Null'
        
        #show statement in row & column form
        t = PrettyTable(["Reason","Date","Mode","Amount"])
        curr =self.head
        
        while curr!=None:
            
            t.add_row([curr.reason,curr.date_time,curr.mode,curr.data])
            
            curr = curr.next
            
        print(t)
            
            
            
l = Linked_list()
l.stmnt()
l.credit("Good",12000)
l.debit(2000)
l.stmnt()
            
        
        