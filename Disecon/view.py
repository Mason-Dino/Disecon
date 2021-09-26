import inspect
import sqlite3
from inspect import getframeinfo
from inspect import stack

#def debuginfo():
    #caller = getframeinfo(stack()[1][0])
    
    #return f"\n   File - {caller.filename} \n      Line - {caller.lineno}"

class view:
    def __init__(self, user_ID=None, user_Name=None):
        self.user_ID = user_ID
        self.user_Name = user_Name
        
    def wallet(self):
        #user ID has none
        if self.user_ID == None:
            print("user_ID")
        
        #User ID is there
        else:            
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