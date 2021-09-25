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

