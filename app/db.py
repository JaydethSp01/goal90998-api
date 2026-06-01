import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = psycopg.connect(DATABASE_URL)
else:
    conn = None

# Implement fallback to in-memory storage or mock if needed
