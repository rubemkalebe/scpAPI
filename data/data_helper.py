import psycopg2

def create_connection():
    conn_string = '''
        host='localhost'
        port=5433
        dbname='scp'
        user='postgres'
        password='postgres'
    '''
    return psycopg2.connect(conn_string)

