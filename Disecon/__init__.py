import inspect
import sqlite3
from inspect import getframeinfo
from inspect import stack

def debuginfo():
    caller = getframeinfo(stack()[1][0])
    
    return f"\n   File - {caller.filename} \n      Line - {caller.lineno}"

def start():
    conn = sqlite3.connect("economy.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE economy (
            user_ID int,
            user_name text,
            wallet int,
            bank int,
            net int
            
        )""")
        
        error = "The database was made."
        
    except:
        error = "The database was not made."
        
    
    conn.commit()
    conn.close()
    
    print(error)

class wallet:
    def __init__(self, amount: int, user_ID, user_Name):
        self.user_Name = user_Name
        self.user_ID =  user_ID
        self.amount = amount
        
    def add(self):
        conn = sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
        
        items = c.fetchall()
        none = str(items)
        
        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ({self.user_ID}, '{self.user_Name}', {self.amount} , 0, {self.amount})")
            print("made") #test part#
            
        else:
            for item in items:
                wallet = int(item[2])
                bank = int(item[3])

                
            sum = self.amount + wallet
            
            c.execute(f"""UPDATE economy SET wallet = {sum}
                    WHERE user_ID = {self.user_ID}  
                """)
            
            conn.commit()
            
            net = sum + bank
            
            c.execute(f"""UPDATE economy SET net = {net}
                      WHERE user_ID = {self.user_ID}
                """)
            
            conn.commit()
            conn.close()
        
    def sub(self):
        wallet.amount = wallet.amount - 100
        print(wallet.amount)
        
class view:
    def __init__(self, user_ID=None, user_Name=None):
        self.user_ID = user_ID
        self.user_Name = user_Name
        
    def wallet(self):
        #both don't work
        if self.user_ID == None and self.user_Name == None:
            print(f"Nothing is in the view function {debuginfo()}")
        
        #user name works but user ID doesn't work
        elif self.user_ID == None:
            print("user_ID")
        
        #user ID works but user Name doesn't    
        elif self.user_Name == None:            
            conn = sqlite3.connect("economy.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
            
            items = c.fetchall()
            none = str(items)
            
            if none == "[]":
                return "0"
            
            else:
                for item in items:
                    wallet = item[2]
                    
                return wallet        

    def bank(self):
        #both don't work
        if self.user_ID == None and self.user_Name == None:
            print(f"Nothing is in the view function {debuginfo()}")
        
        #user name works but user ID doesn't work
        elif self.user_ID == None:
            print("user_ID")
        
        #user ID works but user Name doesn't    
        elif self.user_Name == None:            
            conn = sqlite3.connect("economy.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
            
            items = c.fetchall()
            none = str(items)
            
            if none == "[]":
                return "0"
            
            else:
                for item in items:
                    bank = item[3]
                    
                return bank
        
    def net(self):
        #both don't work
        if self.user_ID == None and self.user_Name == None:
            print(f"Nothing is in the view function {debuginfo()}")
        
        #user name works but user ID doesn't work
        elif self.user_ID == None:
            print("user_ID")
        
        #user ID works but user Name doesn't    
        elif self.user_Name == None:            
            conn = sqlite3.connect("economy.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
            
            items = c.fetchall()
            none = str(items)
            
            if none == "[]":
                return "0"
            
            else:
                for item in items:
                    net = item[4]
                    
                return net
            
class top:
    def __init__(self, place:int):
        pass
        
start()

conn = sqlite3.connect("economy.db")
c = conn.cursor()

#c.execute(f"INSERT INTO economy VALUES (638092957756555291, 'LegosAndStuff#0501', 0 , 0, 0)")

conn.commit()
conn.close()
        
        
something = wallet(100, 638092957756555291, f"LegosAndStuff#0501")

#something.add()

sun = view(user_ID=638092957756555291)
print(sun.wallet())
print(sun.bank())
print(sun.net())
