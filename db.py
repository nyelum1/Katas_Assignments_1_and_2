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

def insert_station(conn, name, location):
    """Inserts a new station and returns its ID."""
    query = "INSERT INTO Stations (name, location) VALUES (?, ?)"
    cursor = conn.cursor()
    cursor.execute(query, (name, location))
    conn.commit()
    return cursor.lastrowid

def insert_observation(conn, station_id, temp):
    """Inserts a weather observation linked to a station ID."""
    query = "INSERT INTO Observations (station_id, temperature) VALUES (?, ?)"
    cursor = conn.cursor()
    cursor.execute(query, (station_id, temp))
    conn.commit()


def update_station_name(conn, station_id, new_name):
    """Updates the name of an existing station."""
    query = "UPDATE Stations SET name = ? WHERE station_id = ?"
    conn.execute(query, (new_name, station_id))
    conn.commit()

def delete_observation(conn, obs_id):
    """Deletes a specific observation record by ID."""
    query = "DELETE FROM Observations WHERE obs_id = ?"
    conn.execute(query, (obs_id,))
    conn.commit()

def get_station_report(conn):
    """
    Joins Stations and Observations to return a list of 
    all readings with their corresponding station names.
    """
    query = '''
        SELECT s.name, o.temperature, o.timestamp
        FROM Stations s
        JOIN Observations o ON s.station_id = o.station_id
        ORDER BY o.timestamp DESC
    '''
    return conn.execute(query).fetchall()


def seed_data(conn):
    """Populates the database with sample stations and observations."""
    # Add Stations
    s1 = insert_station(conn, "North Pole Base", "90.0000 N")
    s2 = insert_station(conn, "Sahara Outpost", "23.4162 N")
    
    # Add Observations
    insert_observation(conn, s1, -35.5)
    insert_observation(conn, s1, -38.2)
    insert_observation(conn, s2, 45.1)
    print("Database seeded successfully.")