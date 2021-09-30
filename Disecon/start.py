import sqlite3

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
        
        pass
    
    except:
        print("table wrong")
        
    
    conn.commit()
    conn.close()