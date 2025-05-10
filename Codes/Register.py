from databse import insert_id_pass,personal_info

def register_account():
    print('--- Register New Account ---')
    print()
    name=input('name:').strip()
    username = input('Username: ').strip()
    password = input('Password: ').strip()
    location=input('location :')

    if not username or not password:
        print('Username and password cannot be empty.')
        return
    personal_info(name,username,location)
    insert_id_pass(username, password)
