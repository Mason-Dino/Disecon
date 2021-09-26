import inspect
import sqlite3
from view import *
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
        conn = sqlite3("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
        
        items = c.fetchall()
        none = str(items)
        
        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ({self.user_ID}, '{self.user_Name}', 0 , 0, 0)")
            
            return None
        
        else:
            for item in items:
                pass
        

            
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

#sun = view(user_ID=638092957756555291)
sun = view()
print(sun.wallet())
print(sun.bank())
print(sun.net())
