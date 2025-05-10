import sqlite3

DB_NAME = 'user_info.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Logins (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def insert_id_pass(username, password):
    create_table()
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO Logins (username, password) VALUES (?, ?)', (username, password)
        )
        conn.commit()
        print('Account registered successfully!')
    except sqlite3.IntegrityError:
        print('Username already exists. Please choose another.')
    finally:
        conn.close()

def retrieve_password(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM Logins WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def personal_info(name, username,location):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS personal_info (
        name TEXT PRIMARY KEY,
        username TEXT ,
        location TEXT 
    )
    ''')
    conn.commit()
    cursor.execute( 'INSERT INTO personal_info (name, username,location) VALUES (?, ?,?)', (name, username,location))
    conn.commit()
    conn.close()

def retrive_personal_info(username):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM personal_info WHERE username=?',(username,))
    result=cursor.fetchone()
    return result