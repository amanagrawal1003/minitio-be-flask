import os
import psycopg2.pool
import psycopg2.extras
from dotenv import load_dotenv
dotenv_path = '.env'
load_dotenv(dotenv_path)
class DbUtil:
    def getPostgresqlConnection(self):
        try:
            pool = psycopg2.pool.SimpleConnectionPool(
                int(os.getenv("POSTGRES_RENDER_DATABASE_MINCON")),
                int(os.getenv("POSTGRES_RENDER_DATABASE_MAXCON")),
                user=os.getenv("POSTGRES_RENDER_DATABASE_USER"),
                password=os.getenv("POSTGRES_RENDER_DATABASE_PASSWORD"),
                host=os.getenv("POSTGRES_RENDER_DATABASE_HOST"),
                port=os.getenv("POSTGRES_RENDER_DATABASE_PORT"),
                database=os.getenv('POSTGRES_RENDER_DATABASE_DB')
            )
            con = pool.getconn()
            con.autocommit = True
            cursor = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            return cursor
        except Exception as e:
            print(f"Problem with db connection: {e}")
            return None

    def closePostgresqlConnection(self, cursor):
        if cursor:
            cursor.close()
