import os
import csv


class User:
    def __init__(self, name, pin_code, user_balance):
        self._name = name
        self._pin_code = pin_code
        self._user_balance = user_balance


class Atm:
    def __init__(self):
        self.__balance = 100000
        self.__list_user = []

    def verification(self, name, pin_code):
        if len(self.__list_user) == 0:
            print("-|There is no such account|-")
            print("-|You need to register|-")
        else:
            for user in self.__list_user:
                if user._name == name:
                    if user._pin_code == pin_code:
                        print(f"\t-|Account Confirmed|-\n"
                              f"\t\t-|Welcome|-\n")
                        while True:
                            print(f"\tMenu Atm\n"
                                  f"-|1.Check the balance\n"
                                  f"-|2.Withdraw money\n"
                                  f"-|3.Exit")
                            try:
                                choice = int(input("-|Enter the option: "))
                                print()
                                if choice == 1:
                                    print("\tCheck the balance")
                                    print(f"Your balance - {user._user_balance}\n")
                                elif choice == 2:
                                    print("\tWithdraw money")
                                    money = int(input("Enter the amount you want to withdraw: "))
                                    if money > user._user_balance:
                                        print("!Not enough money to withdraw!")
                                    elif money > self.__balance:
                                        print("There is not enough money at the ATM")
                                    else:
                                        user._user_balance -= money
                                        print("-|Money withdrawn|-")
                                        print("-|A good day|-")
                                        self.save_info_user(user, user._name)
                                elif choice == 3:
                                    print("-|Goodbye|-")
                                    return False

                            except ValueError as s:
                                print("Error value! Enter the number from 1 to 3")
                    else:
                        print("<|Incorrect pin code|>")
                        return False

            print("-|There is no such account|-")
            print("-|You need to register|-")
            return False

    def registration_user(self, name):
        while True:
            try:
                pin_code = None
                user_balance = None
                if pin_code is None:
                    pin_code = int(input("Enter a new pincode consisting of 6 digits: "))
                if len(str(pin_code)) != 6:
                    raise ValueError("The PIN code must consist of 6 characters")
                user_balance = int(input("Enter you balance: "))
                if user_balance > 100000:
                    raise ValueError("There can't be more than 100.000 on the account")
                self.__list_user.append(User(name, pin_code, user_balance))
                self.save_info_user(User(name, pin_code, user_balance), name)
                print()
                break
            except ValueError as s:
                print("Error of data")

    @staticmethod
    def save_info_user(user: object, file_name: str):
        if not file_name.endswith('.csv'):
            file_name = file_name + '.csv'
        header = ["Name", "PIN", "User Balance"]
        with open(file_name, "w+", newline='') as file:
            dict_write = csv.DictWriter(file, fieldnames=header)
            dict_write.writeheader()
            info = {"Name": user._name, "PIN": user._pin_code, "User Balance": user._user_balance}
            dict_write.writerow(info)

    def show_info(self):
        for i in self.__list_user:
            print(i.__dict__)

    def menu_atm(self):
        while True:
            print("\tMenu ATM")
            print("-|1.Withdraw money from the ATM\n"
                  "-|2.Create a new account\n"
                  "-|3.Exit")
            selection = input("-|Enter the option: ")
            print()
            if selection == '':
                print("Enter your choice from 1 to 3")
            elif int(selection) == 1:
                print("\tWithdraw money from the ATM")
                while True:
                    try:
                        name = input("-|Enter your name: ").lower()
                        pin_code = int(input("-|Enter your pin code: "))
                        self.verification(name, pin_code)
                        break
                    except ValueError as s:
                        print("Error")
            elif int(selection) == 2:
                print("\tCreate a new account")
                try:
                    name = input("-|Enter your name: ").lower()
                    if 1 >= len(name) or 20 < len(name):
                        raise ValueError("The name must be at least 1 and more than 20 characters")
                    else:
                        self.registration_user(name)
                except ValueError as s:
                    print("Error! Incorrect name...")
            elif int(selection) == 3:
                print("-|Exit|-")
                break
            else:
                print("Enter your choice from 1 to 3")


if __name__ == '__main__':
    atm = Atm()
    atm.menu_atm()