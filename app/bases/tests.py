from django.test import TestCase
import psycopg2

## Create your tests here.

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "municip_quilanga"
PSQL_PASS = "municip_quilanga"
PSQL_DB   = "dbemprendimientos_db"

try:
    connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
    conn = psycopg2.connect(connstr)

    cur = conn.cursor()

    sqlquery = "SELECT nombres from Emprendedor";
    cur.execute(sqlquery)

    row = cur.fetchone()

    cur.close()
    conn.close()

    username = row[1]

    print(username)

except:
    print("Error de base de datos")
