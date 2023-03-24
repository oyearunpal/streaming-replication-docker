import psycopg2
from os import environ as env
# Connect to the replica server
conn = psycopg2.connect(
    host=env.get("REPLICATE_FROM"),
    port="5432",
    dbname="postgres",
    user="postgres",
    password = 'postgres'
    # options="-c search_path=my_schema"
)

print("Connected")

# Create a test table
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

# Insert some test data
with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO test_table (name)
        VALUES ('John'), ('Jane'), ('Bob')
    """)
    conn.commit()

# Read the data
with conn.cursor() as cur:
    cur.execute("""
        SELECT * FROM test_table
    """)
    rows = cur.fetchall()
    print(rows)

# Close the connection
conn.close()
