import os
import time
from blessed import Terminal
from Register import register_account

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
            print(' Login coming soon!')
            time.sleep(1.5)
        elif command == 3:
            print(' Goodbye!')
            break
        else:
            print(' Invalid choice.')
            time.sleep(1)

if __name__ == "__main__":
    main()
