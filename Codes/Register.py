from Codes.databse import insert_id_pass

def register_account():
    print('--- Register New Account ---')
    username = input('Username: ').strip()
    password = input('Password: ').strip()

    if not username or not password:
        print('Username and password cannot be empty.')
        return

    insert_id_pass(username, password)
