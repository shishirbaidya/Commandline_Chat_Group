import time,os
import sqlite3
from databse import retrieve_password


conn=sqlite3.connect('user_info.db ')
cursor=conn.cursor()

#
def check_user_DB(username,password):
    user=cursor.execute('''Select username,pass from user_info
                        where username=''')


def login_():
    os.system('clear')
    print('Login with user id and password,')
    
    username=input('Enter username :')
    password=input('Enter password :')

    if(retrieve_password(username)==password):
        return True,username
    else:
        return False