import sqlite3

class wallet:
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
            c.execute(f"INSERT INTO economy VALUES ({self.user_ID}, {self.amount} , 0, {self.amount})")
            
            conn.commit()
            conn.close()
            
            print("made") #test part#
            
        else:
            for item in items:
                wallet = int(item[1])
                bank = int(item[2])
            
            print("--------")    
            print(wallet)
            print(self.amount)
                
            sum = self.amount + wallet
            
            print(sum)
            print(self.user_ID)
            print("-------------")
            
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
            c.execute(f"INSERT INTO economy VALUES ({self.user_ID}, 0 , 0, 0)")
            
            return None
        
        else:
            for item in items:
                wallet = int(item[1])
                bank = int(item[2])
                
            if wallet >= self.amount:
                sum = wallet - self.amount
                net = sum + bank
                
                c.execute(f"""UPDATE economy SET wallet = {sum}
                        WHERE user_ID = {self.user_ID}  
                    """)
                
                conn.commit()
                
                c.execute(f"""UPDATE economy SET net = {net}
                        WHERE user_ID = {self.user_ID}
                    """)
                
                conn.commit()
                conn.close()
            
            elif wallet < self.amount:
                return None
            
            else:
                return None
