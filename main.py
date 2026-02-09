# main.py
import db

# 1. Setup
connection = db.get_connection(":memory:") # Use memory for a quick test
db.initialize_db(connection)

# 2. Seed
db.seed_data(connection)


# 3. Query with Join
report = db.get_station_report(connection)
for row in report:
    print(f"Station: {row[0]} | Temp: {row[1]}°C | Time: {row[2]}")

connection.close()