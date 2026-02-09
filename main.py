# main.py
import db

# 1. Setup
connection = db.get_connection(":memory:") # Use memory for a quick test
db.initialize_db(connection)

# 2. Seed
db.seed_data(connection)