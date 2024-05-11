class ATM:
    def __init__(self):
        self.users = {
            'krishna': {'password': 'abc123', 'pin': 1234, 'balance': 2000},
            'kumar': {'password': 'ab12', 'pin': 2345, 'balance': 2000},
            'kaushik': {'password': 'abc12', 'pin': 3456, 'balance': 2000}
        }
        self.current_user = None
        self.login_attempts = 0
        self.MENU_OPTIONS = {
            1: 'Withdraw',
            2: 'Deposit',
            3: 'Balance',
            4: 'Change Password',
            5: 'Exit'
        }

    def login(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("Invalid username")
            return
        password = input("Enter your password: ")
        if password != self.users[username]['password']:
            print("Invalid password")
            return
        self.current_user = username
        self.login_attempts = 0
        self.show_menu()

    def show_menu(self):
        print("\n")
        print("Menu:")
        for option, description in self.MENU_OPTIONS.items():
            print(f"{option} --> {description}")
        option = int(input("Enter your option: "))
        self.handle_option(option)

    def handle_option(self, option):
        if option == 1:
            self.withdraw()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.show_balance()
        elif option == 4:
            self.change_password()
        elif option == 5:
            self.exit()
        else:
            print("Invalid option")
            self.show_menu()

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        pin = int(input("Enter your PIN: "))
        if pin != self.users[self.current_user]['pin']:
            print("Invalid PIN")
            return
        if amount > self.users[self.current_user]['balance']:
            print("Insufficient balance")
            return
        self.users[self.current_user]['balance'] -= amount
        print("Withdrawal successful")
        self.show_menu()

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        pin = int(input("Enter your PIN: "))
        if pin != self.users[self.current_user]['pin']:
            print("Invalid PIN")
            return
        self.users[self.current_user]['balance'] += amount
        print("Deposit successful")
        self.show_menu()

    def show_balance(self):
        pin = int(input("Enter your PIN: "))
        if pin != self.users[self.current_user]['pin']:
            print("Invalid PIN")
            return
        print(f"Your balance is {self.users[self.current_user]['balance']}")
        self.show_menu()

    def change_password(self):
        pin = int(input("Enter your PIN: "))
        if pin != self.users[self.current_user]['pin']:
            print("Invalid PIN")
            return
        current_password = input("Enter your current password: ")
        if current_password != self.users[self.current_user]['password']:
            print("Invalid password")
            return
        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm your new password: ")
        if new_password != confirm_password:
            print("Passwords do not match")
            return
        self.users[self.current_user]['password'] = new_password
        print("Password changed successfully")
        self.show_menu()

    def exit(self):
        print("Thank you for using our ATM system")
        exit()

atm = ATM()
atm.login()
