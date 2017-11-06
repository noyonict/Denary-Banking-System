class DenaryBankingSystem:
    """
    Our Banking System
    """
    def __init__(self, name, phone, email, account_no, pin, address, cash=500):
        self.name = name
        self.phone = phone
        self.email = email
        self.ac_no = account_no
        self.pin = pin
        self.add = address
        self.cash = cash
        self.login()

    def login(self):
        account_no = input("Enter your account no: ")
        pin = input("Enter your pin: ")
        if account_no == self.ac_no and pin == self.pin:
            self.atm_service()
        else:
            print("Login Failed! \nInvalid Account No. or Pin.")

    def atm_service(self):
        print("Denary Banking System".center(50, '*'))
        print("     1 - Check Balance")
        print("     2 - Deposit ")
        print("     3 - Withdraw ")
        print("     4 - Change pin ")
        print("     5 - Balance Transfer ")
        print("     6 - Exit ")
        choice = int(input("   Enter your choice: "))
        self.user_choice(choice)

    def check_balance(self):
        print("Hello,", str(self.name).capitalize(), ". Your balance:", self.cash)
        self.atm_service()

    def deposit(self):
        try:
            taka = int(input('How many taka you want to deposit: '))
        except Exception as e:
            print(e)
            self.deposit()
        self.cash += taka
        print('Deposit Complete!')
        self.atm_service()

    def withdraw(self):
        try:
            taka = int(input('How many taka you want to withdraw: '))
        except Exception as e:
            print(e)
            self.withdraw()
        if self.cash > 500:
            self.cash -= taka
            print('Withdraw Complete!')
        else:
            print('Insufficient Balance!')
        self.atm_service()

    def change_pin(self):
        pre_pin = input('Enter your current pin: ')
        if self.pin == pre_pin:
            change_pin = input('Enter your new pin: ')
            self.pin = change_pin
        else:
            print('Wrong pin number!')
        self.atm_service()

    def user_choice(self, choice):
        if choice == 1:
            self.check_balance()
        elif choice == 2:
            self.deposit()
        elif choice == 3:
            self.withdraw()
        elif choice == 4:
            self.change_pin()
        elif choice == 5:
            pass
        elif choice == 6:
            print('Good bye', self.name)
            exit()
        else:
            print("Please enter a valid input.")
            self.atm_service()

shajib_account = DenaryBankingSystem("Md. Shajib", "01914758379", "smo@gmail.com", "123", "123", "Shantinogor, Dhaka")
noyon = DenaryBankingSystem("Md. Noyon", "0983498", 'ksjfkl@gami.com', "db153", "1234", 'Dhaka')
shajib_account.login()
