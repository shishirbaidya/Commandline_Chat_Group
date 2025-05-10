import os
import time
from blessed import Terminal
from Register import register_account
from log_in import login_
from dashboard import dashboard







#-MODULES IMPORTS ENDS HERE !
#                           #
#                           #
#                           #
#FUNCTIONS STARTS FROM HERE #
def main():
    term=Terminal()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(term.red('--- Welcome to Commandline Chat ---'))
        print(term.green('1. Register'))
        print(term.blue('2. Login (coming soon)'))
        print(term.red('3. Logout / Exit'))
        print()

        try:
            command = int(input('$ '))
        except ValueError:
            print('Please enter a number.')
            time.sleep(1)
            continue

        if command == 1:
            os.system('clear' if os.name == 'posix' else 'cls')
            register_account()
            input('Press Enter to return to menu...')
        elif command == 2:
            if login_():
                dashboard(12)
                time.sleep(1)
            else:
                print('failed')
                time.sleep(1)
        elif command == 3:
            print(' Goodbye!')
            break
        else:
            print(' Invalid choice.')
            time.sleep(1)

if __name__ == "__main__":
    main()
