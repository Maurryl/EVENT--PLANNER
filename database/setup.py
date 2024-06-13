from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""  
            CREATE TABLE IF NOT EXISTS guests (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  phone INTEGER NOT NULL,
                  email TEXT NOT NULL,
                  created_at DATETIME NOT NULL,
                  
                  )
                  """)
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL,
                     
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
                   description TEXT NOT NULL,
                   date DATETIME NOT NULL,
                   location TEXT NOT NULL,
                   created_at DATETIME NOT NULL,
                   updated_at DATETIME NOT NULL,
                   
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event-venues (
            event_id INTEGER NOT NULL,
            venue_id INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (event_id, venue_id),
            FOREIGN KEY (event_id) REFERENCES events(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)  
            
                   
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event-guests (
            event_id INTEGER NOT NULL,
            guest_id INTEGER NOT NULL,
            rsvp BOOLEAN , 
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (event_id) REFERENCES events(id),
            FOREIGN KEY (guest_id) REFERENCES guests(id) 
           
            
                   
        )
    ''')
 
 
