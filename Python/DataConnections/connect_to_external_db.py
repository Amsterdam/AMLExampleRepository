import psycopg2


# Enter database details and your username and password to connect
host = "xx.xxx.x.xx"
port = 5432
dbname = "example_db"
user = "username"
pw = "mypasswordisgreat"

conn = psycopg2.connect(dbname=dbname, user=user, password=pw, host=host, port=port)
cur = conn.cursor()

# Add your custom SQL query below
sql_query = "select version();"
cur.execute(sql_query)

# Don't forget to close the connection to the database when finished
cur.close()
conn.close()
