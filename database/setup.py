# database/setup.py

from connection import get_db_connection
import sqlite3

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create guests table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create venues table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create events table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            location TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create event_venues table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS event_venues (
            event_id INTEGER NOT NULL,
            venue_id INTEGER NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (event_id, venue_id),
            FOREIGN KEY (event_id) REFERENCES events(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        )
    """)

    # Create event_guests table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS event_guests (
            event_id INTEGER NOT NULL,
            guest_id INTEGER NOT NULL,
            rsvp BOOLEAN DEFAULT FALSE,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (event_id, guest_id),
            FOREIGN KEY (event_id) REFERENCES events(id),
            FOREIGN KEY (guest_id) REFERENCES guests(id)
        )
    """)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
