import sqlite3

def get_connection(db_name="weather.db"):
    """
    Creates and returns a connection to the SQLite database with Foreign Keys enabled.
    """
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def initialize_db(conn):
    """
    Creates the Stations and Observations tables if they do not exist.
    """
    cursor = conn.cursor()
    
    # Parent Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stations (
            station_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    
    # Child Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Observations (
            obs_id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id INTEGER NOT NULL,
            temperature REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (station_id) REFERENCES Stations (station_id) ON DELETE CASCADE
        )
    ''')
    conn.commit()