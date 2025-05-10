from blessed import Terminal
from databse import retrive_personal_info



def dashboard(username):
    term=Terminal()
    print(term.red('------------DASHBOARD------------------'))
    print()
    info =retrive_personal_info(username)
    print('Name :',info[0])
    print('username :',info[1])
    print('location :',info[2])