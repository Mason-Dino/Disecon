import sqlite3

def start():
    conn = sqlite3.connect("economy.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE economy (
            user_ID text,
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
    def __init__(self, user_ID, amount):
        self.user_ID =  user_ID
        self.amount = amount
        
    def add(self):
        print(wallet.amount)
        
    def sub(self):
        wallet.amount = wallet.amount - 100
        print(wallet.amount)
        
    def sub_test(user_ID, amount):
        print(wallet.sub_test)
        print("hi")
        
wallet.sub_test(638092957756555291, 10)