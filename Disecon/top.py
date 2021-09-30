import sqlite3

class top:
    def __init__(self, place:int):
        self.place = place
        
    def user_ID(self):
        offset = self.place - 1
        
        conn =  sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET {offset}")
        
        items = c.fetchall()
        
        for item in items:
            user_ID = int(item[0])
            
        return user_ID

    def wallet(self):
        offset = self.place - 1
        
        conn =  sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET {offset}")
        
        items = c.fetchall()
        
        for item in items:
            wallet = int(item[2])
            
        return wallet
        
    def bank(self):
        offset = self.place - 1
        
        conn =  sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET {offset}")
        
        items = c.fetchall()
        
        for item in items:
            bank = int(item[4])
            
        return bank
    
    def net(self):
        offset = self.place - 1
        
        conn =  sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET {offset}")
        
        items = c.fetchall()
        
        for item in items:
            net = int(item[0])
            
        return net
