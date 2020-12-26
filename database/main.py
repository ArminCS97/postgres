from database.config import config
import psycopg2

def connect():
    conn = None
    try:
        db_params = config()

        conn = psycopg2.connect(**db_params)

        cursor = conn.cursor()

        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
