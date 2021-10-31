import inspect
import sqlite3
from inspect import getframeinfo
from inspect import stack

class view:
    def __init__(self, user_ID=None):
        self.user_ID = user_ID
        
    def wallet(self):                    
        conn = sqlite3.connect("economy.db")
        c = conn.cursor()
            
        c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
            
        items = c.fetchall()
        none = str(items)
            
        if none == "[]":
                return "0"
            
        else:
            for item in items:
                wallet = item[1]
                    
            return wallet        

    def bank(self):                    
        conn = sqlite3.connect("economy.db")
        c = conn.cursor()
            
        c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
            
        items = c.fetchall()
        none = str(items)
            
        if none == "[]":
                return "0"
            
        else:
            for item in items:
                bank = item[2]
                    
            return bank   
        
    def net(self):                    
        conn = sqlite3.connect("economy.db")
        c = conn.cursor()
            
        c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
            
        items = c.fetchall()
        none = str(items)
            
        if none == "[]":
                return "0"
            
        else:
            for item in items:
                net = item[3]
                    
            return net   