import sqlite3

class bank:
    def __init__(self, amount: int, user_ID):
        self.user_ID =  user_ID
        self.amount = amount
        
    def add(self):
        conn = sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM economy WHERE user_ID={self.user_ID}")
        
        items = c.fetchall()
        none = str(items)
        
        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ({self.user_ID}, 0 , {self.amount}, {self.amount})")
            
            conn.commit()
            conn.close()
            
            print("made") #test part#
            
        else:
            for item in items:
                wallet = int(item[2])
                bank = int(item[3])

                
            sum = self.amount + bank
            
            c.execute(f"""UPDATE economy SET bank = {sum}
                    WHERE user_ID = {self.user_ID}  
                """)
            
            conn.commit()
            
            net = sum + wallet
            
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
            c.execute(f"INSERT INTO economy VALUES ({self.user_ID}, 0 , 0, 0)")
            
            return None
        
        else:
            for item in items:
                pass