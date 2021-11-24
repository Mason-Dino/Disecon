import sqlite3

class results:
    class view:
        def __init__(self, user_ID:int):
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
                wallet = int(item[1])
                
            return wallet
            
        def bank(self):
            offset = self.place - 1
            
            conn =  sqlite3.connect("economy.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET {offset}")
            
            items = c.fetchall()
            
            for item in items:
                bank = int(item[2])
                
            return bank
        
        def net(self):
            offset = self.place - 1
            
            conn =  sqlite3.connect("economy.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET {offset}")
            
            items = c.fetchall()
            
            for item in items:
                net = int(item[3])
                
            return net 
