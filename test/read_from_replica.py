import psycopg2
from os import environ as env

# Connect to the replica server
conn = psycopg2.connect(
    host=env.get("REPLICATE_TO"),
    port="5433",
    dbname="postgres",
    # user=env.get("REPLICA_POSTGRES_USER"),
    # password=env.get("REPLICA_POSTGRES_PASSWORD"),
    user="postgres",
    password = 'postgres'
    # options="-c search_path=my_schema"
)

# Execute a query to read data from a table
cur = conn.cursor()
cur.execute("SELECT * FROM test_table")
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

